import tensorflow as tf
from Loadfile_Pickle import Loadfile_Picker
from Transformer import Transformer
from underthesea import word_tokenize
from CustomSchedule import CustomSchedule
import os
import pandas as pd
# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)


class Transformer_model():
    def __init__(self):
        super(Transformer_model, self).__init__()
        self.word2id_question = Loadfile_Picker(
            'Trained/Vocab/').load_word2id('word2id_question')
        self.word2id_answer = Loadfile_Picker(
            'Trained/Vocab/').load_word2id('word2id_answer')
        self.id2word_question = Loadfile_Picker(
            'Trained/Vocab/').load_word2id('id2word_question')
        self.id2word_answer = Loadfile_Picker(
            'Trained/Vocab/').load_word2id('id2word_answer')

        # self.question_embedding_matrix = Loadfile_Picker(
        #     'Trained/Vocab/').load_question_embedding_matrix('question_embedding_matrix')
        # self.answer_embedding_matrix = Loadfile_Picker(
        #     'Trained/Vocab/').load_answer_embedding_matrix('answer_embedding_matrix')

        self.batch_size = 50
        self.units = 1024
        self.embedding_dim = 300
        self.max_words_question = 58
        self.max_words_answer = 247

        self.num_layers = 4
        self.d_model = 300
        self.dff = 512
        self.num_heads = 5
        self.dropout_rate = 0.1
        self.pe_input = 1000
        self.pe_target = 1000


        self.input_vocab_size = len(self.word2id_question)
        self.target_vocab_size = len(self.word2id_answer)

        self.transformer = Transformer(self.num_layers, self.d_model, self.num_heads, self.dff, self.input_vocab_size,
                                       self.target_vocab_size, self.pe_input, self.pe_target, self.dropout_rate)
        
        self.learning_rate = CustomSchedule(self.d_model)

        self.optimizer = tf.keras.optimizers.Adam(self.learning_rate, beta_1=0.9, beta_2=0.98,
                                                  epsilon=1e-9)

        # self.checkpoint_dir = './Trained/Model'
        # self.checkpoint_prefix = os.path.join(self.checkpoint_dir, "ckpt")
        # self.checkpoint = tf.train.Checkpoint(optimizer=self.optimizer,
        #                                       transformer=self.transformer)

        # self.checkpoint.restore(
        #     tf.train.latest_checkpoint(self.checkpoint_dir))

        self.checkpoint_path = './Trained/Model_Transformer'

        self.ckpt = tf.train.Checkpoint(transformer=self.transformer,
                                        optimizer=self.optimizer)

        self.ckpt_manager = tf.train.CheckpointManager(self.ckpt, 
                                                    self.checkpoint_path, 
                                                    max_to_keep=5)

        # if a checkpoint exists, restore the latest checkpoint.
        if self.ckpt_manager.latest_checkpoint:
            self.ckpt.restore(self.ckpt_manager.latest_checkpoint)
            print('Latest checkpoint restored!!')

    def create_padding_mask(self, seq):
        seq = tf.cast(tf.math.equal(seq, 0), tf.float32)

        # add extra dimensions to add the padding
        # to the attention logits.
        return seq[:, tf.newaxis, tf.newaxis, :]  # (batch_size, 1, 1, seq_len)

    def create_look_ahead_mask(self, size):
        mask = 1 - tf.linalg.band_part(tf.ones((size, size)), -1, 0)
        return mask  # (seq_len, seq_len)

    def create_masks(self, inp, tar):
        # Encoder padding mask
        enc_padding_mask = self.create_padding_mask(inp)

        # Used in the 2nd attention block in the decoder.
        # This padding mask is used to mask the encoder outputs.
        dec_padding_mask = self.create_padding_mask(inp)

        # Used in the 1st attention block in the decoder.
        # It is used to pad and mask future tokens in the input received by
        # the decoder.
        look_ahead_mask = self.create_look_ahead_mask(tf.shape(tar)[1])
        dec_target_padding_mask = self.create_padding_mask(tar)
        combined_mask = tf.maximum(dec_target_padding_mask, look_ahead_mask)

        return enc_padding_mask, combined_mask, dec_padding_mask


    def acronyms_processing(self, sentence):
        acronyms_path = "./static/Acronyms/Acronyms.csv"
        names = ["keys", "meanings"]
        acronyms = pd.read_csv(acronyms_path, names=names)
        new_sentence = []
        temp = []
        keys = [key.lower() for key in acronyms['keys'].values.tolist()]
        meanings = [meaning.lower() for meaning in acronyms['meanings'].values.tolist()]
        for word in sentence:
            if word in keys:
                temp = [word for word in word_tokenize(meanings[keys.index(word)])]
                for i in temp:
                    new_sentence.append(i)
                temp = []
            else:
                new_sentence.append(word)
        return new_sentence

    def word_processing_question(self, sentence):
        sentence = [word for word in word_tokenize(sentence.lower())]
        sentence = self.acronyms_processing(sentence)
        return [word for word in sentence if word != ""]

    def preprocess_sentence(self, sentence):
        new_sentence = ['<start>']
        for word in sentence:
            new_sentence.append(word)
        new_sentence.append('<end>')
        return new_sentence

    def padding(self, s, max_words):
        s_s = s.copy()
        for i in range(max_words-len(s)):
            s_s.append("[Pad]")
        return s_s
    
    def evaluate(self, input_sentence, max_length=247):
        # inp sentence is portuguese, hence adding the start and end token

        sentence = self.word_processing_question(input_sentence)
        sentence = self.preprocess_sentence(sentence)
        inputs = self.padding(sentence, self.max_words_question)
        inputs = [[self.word2id_question[i] for i in inputs]]

        inputs = tf.convert_to_tensor(inputs)

        encoder_input = inputs

        result = ''

        output = tf.cast(tf.expand_dims(
            [self.word2id_answer['<start>']], 0), dtype=tf.int64)

        for i in range(max_length):
            enc_padding_mask, combined_mask, dec_padding_mask = self.create_masks(
                encoder_input, output)

            # predictions.shape == (batch_size, seq_len, vocab_size)
            predictions, attention_weights = self.transformer(encoder_input,
                                                        output,
                                                        False,
                                                        enc_padding_mask,
                                                        combined_mask,
                                                        dec_padding_mask)

            # select the last word from the seq_len dimension
            predictions = predictions[:, -1:, :]  # (batch_size, 1, vocab_size)

            predicted_id = tf.argmax(predictions, axis=-1)


            # return the result if the predicted_id is equal to the end token
            id = tf.reshape(predicted_id,()).numpy()

            if self.id2word_answer[id] == '<end>':
                break

            result += self.id2word_answer[id] + ' '
            # concatentate the predicted_id to the output which is given to the decoder
            # as its input.
            output = tf.concat([output, predicted_id], axis=-1)

        result = result.split()
        result2 = ''
        punctuation = ['.', ')', '-']


        for i, word in enumerate(result):
            if word == '-':
                result2 += '\n' + word + ' '
            else:
                if (word.isnumeric() or (word>='a' and word<='z' and (len(word)==1))) and (result[i+1] in punctuation):
                    result2 += '\n' + word + ' '
                else:
                    result2 += word + ' '

        return result2.strip(), input_sentence

    def answering(self, sentence):
        result, sentence = self.evaluate(sentence)
        print('-')
        print('Input: %s' % (sentence))
        print('Predicted the answer: {}'.format(result))