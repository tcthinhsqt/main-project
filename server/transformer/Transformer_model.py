import tensorflow as tf
from transformer.LoadPickleFile import LoadPickleFile
from transformer.Transformer import Transformer
from underthesea import word_tokenize
from transformer.CustomSchedule import CustomSchedule
import os
import pandas as pd
import string
import emoji
import regex as re
from bs4 import  BeautifulSoup

# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)


class Transformer_model():
    def __init__(self):
        super(Transformer_model, self).__init__()
        self.word2id_question = LoadPickleFile('trained/vocab/').load_word2id('word2id_question')
        self.word2id_answer   = LoadPickleFile('trained/vocab/').load_word2id('word2id_answer')
        self.id2word_question = LoadPickleFile('trained/vocab/').load_word2id('id2word_question')
        self.id2word_answer   = LoadPickleFile('trained/vocab/').load_word2id('id2word_answer')

        # self.question_embedding_matrix = Loadfile_Picker(
        #     'Trained/Vocab/').load_question_embedding_matrix('question_embedding_matrix')
        # self.answer_embedding_matrix = Loadfile_Picker(
        #     'Trained/Vocab/').load_answer_embedding_matrix('answer_embedding_matrix')

        self.batch_size         = 64
        self.units              = 1024
        self.embedding_dim      = 256
        self.max_words_question = 56
        self.max_words_answer   = 908
        self.num_layers         = 4
        self.d_model            = 256
        self.dff                = 512
        self.num_heads          = 8
        self.dropout_rate       = 0.05
        self.pe_input           = 1000
        self.pe_target          = 1000


        self.input_vocab_size  = len(self.word2id_question)
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

        self.checkpoint_path = './trained/model_transformer'

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

    def word_processing_question(self, sentence):
        sentence = [word for word in word_tokenize(sentence)]
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

    #CHUẨN HÓA DỮ LIỆU ĐẦU VÀO
    # Loại bỏ teen code
    def taoTuDienTeenCode(self, filename):
        teencode_header     = ['Teencode', 'NormalLanguage']
        teencode            = pd.read_csv(filename, names = teencode_header)
        teencode_dictionary = {}
        for i in range(len(teencode)):
            teencode_dictionary[teencode.iloc[i,0]] = teencode.iloc[i,1]
        return teencode_dictionary

    def loai_bo_teencode(self, text, teencode_dictionary):
        text2 = ''
        pre_text = []
        words = text.split(' ')
        for word in words:
            if word in teencode_dictionary:
                pre_text.append(teencode_dictionary[word])
            else:
                pre_text.append(word)
            text2 = ' '.join(pre_text)
        return text2

    # Loại bỏ các từ lặp lại
    def clear_repeat_word(self, word, vn_dictionary):
        repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)')
        match_substitution = r'\1\2\3'
        while True:
            if word in vn_dictionary:
                break
            new_word = repeat_pattern.sub(match_substitution, word)
            if new_word != word:
                word = new_word
                continue
            else:
                break
        return word.strip()

    def taoTuDienTiengViet(self, filename):
        with open(filename, 'r') as f:
            vn_dictionary = f.readlines()
        for i in range(len(vn_dictionary)):
            vn_dictionary[i] = vn_dictionary[i].lower().replace('\n','')
        return vn_dictionary

    def clear_repeat_in_text(self, text, vn_dictionary):
        text2 = ''
        pre_text = []
        words = text.split(' ')
        for word in words:
            pre_text.append(self.clear_repeat_word(word, vn_dictionary))
            text2 = ' '.join(pre_text)
        return text2

    # Loại bỏ các từ nhiều hơn 7 ký tự
    def remove_outsize(self, text):
        s = ''
        words = text.replace('_',' ')
        words = words.split(' ')
        for w in words:
            w = w.strip()
            if (len(w)) < 8 and len(w) > 0:
                s += w + ' '
        return s

    # Xóa icon
    def remove_icon(self, text):
        return emoji.get_emoji_regexp().sub(u'', text)

    # Loại bỏ từ viết tắt
    def taoTuDienVietTat(self, filename):
        abbreviation_header     = ['ChuVietTat','ChuDayDu']
        abbreviation            = pd.read_csv(filename,names=abbreviation_header)
        abbreviation_dictionary = {}
        for i in range(len(abbreviation)):
            abbreviation_dictionary[abbreviation.iloc[i,0]] = abbreviation.iloc[i,1]
        return abbreviation_dictionary

    def loai_bo_chu_viet_tat(self, text, abbreviation_dictionary):
        text2 = ''
        pre_text = []
        words = text.split(' ')
        for word in words:
            if word in abbreviation_dictionary:
                pre_text.append(abbreviation_dictionary[word])
            else:
                pre_text.append(word)
            text2 = ' '.join(pre_text)
        return text2

    # Chuẩn hóa dấu câu tiếng việt
    uniChars = "àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶÈÉẺẼẸÊỀẾỂỄỆĐÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴÂĂĐÔƠƯ"
    unsignChars = "aaaaaaaaaaaaaaaaaeeeeeeeeeeediiiiiooooooooooooooooouuuuuuuuuuuyyyyyAAAAAAAAAAAAAAAAAEEEEEEEEEEEDIIIOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUYYYYYAADOOU"

    def loaddicchar(self):
        dic = {}
        char1252 = 'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ'.split(
            '|')
        charutf8 = "à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ".split(
            '|')
        for i in range(len(char1252)):
            dic[char1252[i]] = charutf8[i]
        return dic

    def convert_unicode(self, txt):
        dicchar = self.loaddicchar()
        return re.sub(r'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ',
            lambda x: dicchar[x.group()], txt)

    bang_nguyen_am = [['a', 'à', 'á', 'ả', 'ã', 'ạ', 'a'],
                  ['ă', 'ằ', 'ắ', 'ẳ', 'ẵ', 'ặ', 'aw'],
                  ['â', 'ầ', 'ấ', 'ẩ', 'ẫ', 'ậ', 'aa'],
                  ['e', 'è', 'é', 'ẻ', 'ẽ', 'ẹ', 'e'],
                  ['ê', 'ề', 'ế', 'ể', 'ễ', 'ệ', 'ee'],
                  ['i', 'ì', 'í', 'ỉ', 'ĩ', 'ị', 'i'],
                  ['o', 'ò', 'ó', 'ỏ', 'õ', 'ọ', 'o'],
                  ['ô', 'ồ', 'ố', 'ổ', 'ỗ', 'ộ', 'oo'],
                  ['ơ', 'ờ', 'ớ', 'ở', 'ỡ', 'ợ', 'ow'],
                  ['u', 'ù', 'ú', 'ủ', 'ũ', 'ụ', 'u'],
                  ['ư', 'ừ', 'ứ', 'ử', 'ữ', 'ự', 'uw'],
                  ['y', 'ỳ', 'ý', 'ỷ', 'ỹ', 'ỵ', 'y']]
    bang_ky_tu_dau = ['', 'f', 's', 'r', 'x', 'j']

    nguyen_am_to_ids = {}

    for i in range(len(bang_nguyen_am)):
        for j in range(len(bang_nguyen_am[i]) - 1):
            nguyen_am_to_ids[bang_nguyen_am[i][j]] = (i, j)

    def vn_word_to_telex_type(self, word):
        dau_cau = 0
        new_word = ''
        for char in word:
            x, y = self.nguyen_am_to_ids.get(char, (-1, -1))
            if x == -1:
                new_word += char
                continue
            if y != 0:
                dau_cau = y
            new_word += self.bang_nguyen_am[x][-1]
        new_word += self.bang_ky_tu_dau[dau_cau]
        return new_word

    def vn_sentence_to_telex_type(self, sentence):
        words = sentence.split()
        for index, word in enumerate(words):
            words[index] = self.vn_word_to_telex_type(word)
        return ' '.join(words)

    def chuan_hoa_dau_tu_tieng_viet(self, word):
        if not self.is_valid_vietnam_word(word):
            return word

        chars = list(word)
        dau_cau = 0
        nguyen_am_index = []
        qu_or_gi = False
        for index, char in enumerate(chars):
            x, y = self.nguyen_am_to_ids.get(char, (-1, -1))
            if x == -1:
                continue
            elif x == 9:  # check qu
                if index != 0 and chars[index - 1] == 'q':
                    chars[index] = 'u'
                    qu_or_gi = True
            elif x == 5:  # check gi
                if index != 0 and chars[index - 1] == 'g':
                    chars[index] = 'i'
                    qu_or_gi = True
            if y != 0:
                dau_cau = y
                chars[index] = self.bang_nguyen_am[x][0]
            if not qu_or_gi or index != 1:
                nguyen_am_index.append(index)
        if len(nguyen_am_index) < 2:
            if qu_or_gi:
                if len(chars) == 2:
                    x, y = self.nguyen_am_to_ids.get(chars[1])
                    chars[1] = self.bang_nguyen_am[x][dau_cau]
                else:
                    x, y = self.nguyen_am_to_ids.get(chars[2], (-1, -1))
                    if x != -1:
                        chars[2] = self.bang_nguyen_am[x][dau_cau]
                    else:
                        chars[1] = self.bang_nguyen_am[5][dau_cau] if chars[1] == 'i' else self.bang_nguyen_am[9][dau_cau]
                return ''.join(chars)
            return word

        for index in nguyen_am_index:
            x, y = self.nguyen_am_to_ids[chars[index]]
            if x == 4 or x == 8:  # ê, ơ
                chars[index] = self.bang_nguyen_am[x][dau_cau]
                # for index2 in nguyen_am_index:
                #     if index2 != index:
                #         x, y = nguyen_am_to_ids[chars[index]]
                #         chars[index2] = bang_nguyen_am[x][0]
                return ''.join(chars)

        if len(nguyen_am_index) == 2:
            if nguyen_am_index[-1] == len(chars) - 1:
                x, y = self.nguyen_am_to_ids[chars[nguyen_am_index[0]]]
                chars[nguyen_am_index[0]] = self.bang_nguyen_am[x][dau_cau]
                # x, y = nguyen_am_to_ids[chars[nguyen_am_index[1]]]
                # chars[nguyen_am_index[1]] = bang_nguyen_am[x][0]
            else:
                # x, y = nguyen_am_to_ids[chars[nguyen_am_index[0]]]
                # chars[nguyen_am_index[0]] = bang_nguyen_am[x][0]
                x, y = self.nguyen_am_to_ids[chars[nguyen_am_index[1]]]
                chars[nguyen_am_index[1]] = self.bang_nguyen_am[x][dau_cau]
        else:
            # x, y = nguyen_am_to_ids[chars[nguyen_am_index[0]]]
            # chars[nguyen_am_index[0]] = bang_nguyen_am[x][0]
            x, y = self.nguyen_am_to_ids[chars[nguyen_am_index[1]]]
            chars[nguyen_am_index[1]] = self.bang_nguyen_am[x][dau_cau]
            # x, y = nguyen_am_to_ids[chars[nguyen_am_index[2]]]
            # chars[nguyen_am_index[2]] = bang_nguyen_am[x][0]
        return ''.join(chars)

    def is_valid_vietnam_word(self, word):
        chars = list(word)
        nguyen_am_index = -1
        for index, char in enumerate(chars):
            x, y = self.nguyen_am_to_ids.get(char, (-1, -1))
            if x != -1:
                if nguyen_am_index == -1:
                    nguyen_am_index = index
                else:
                    if index - nguyen_am_index != 1:
                        return False
                    nguyen_am_index = index
        return True

    def chuan_hoa_dau_cau_tieng_viet(self, sentence):
        sentence = sentence.lower()
        words = sentence.split()
        for index, word in enumerate(words):
            cw = re.sub(r'(^\p{P}*)([p{L}.]*\p{L}+)(\p{P}*$)', r'\1/\2/\3', word).split('/')
            # print(cw)
            if len(cw) == 3:
                cw[1] = self.chuan_hoa_dau_tu_tieng_viet(cw[1])
            words[index] = ''.join(cw)
        return ' '.join(words)

    def clean_text(self, text, teencode_dictionary, vn_dictionary, abbreviation_dictionary):
        # Loại bỏ thẻ html
        text = BeautifulSoup(text).get_text()
        # Xóa icon
        text = self.remove_icon(text)
        # Chuyển về chữ thường
        text = text.lower()
        # Loại bỏ TeenCode
        text = self.loai_bo_teencode(text, teencode_dictionary)
        # Loại bỏ dấu câu
        text = ''.join([i for i in text if i not in string.punctuation])
        # Chuẩn hóa dấu câu tiếng việt
        text = self.chuan_hoa_dau_cau_tieng_viet(text)
        # Thay thế một số từ viết tắt thông dụng
        text = self.loai_bo_chu_viet_tat(text, abbreviation_dictionary)
        # Loại các từ có ký tự lặp lại nhiều lần
        text = self.clear_repeat_in_text(text, vn_dictionary)
        # Loại bỏ các từ nhiều hơn 7 ký tự
        text = self.remove_outsize(text)
        # Loại bỏ khoảng trắng không cần thiết
        text = ' '.join(text.split())
        return text

    def sliceIndex(self, x):
        i = 0
        for c in x:
            if c.isalpha():
                i = i + 1
                return i
            i = i + 1

    def upperFirst(self, x):
        i = self.sliceIndex(x)
        return x[:i].upper() + x[i:]

    def isHaveOtherCharacter(self, x):
        for c in x.split('.')[0]:
            if c.isdigit() == False:
                if c.isalpha() & (len(c.strip()) < 1):
                    return False
                return True
        return False

    def addDownLineBeforeListing(self, sentence):
        if self.isHaveOtherCharacter(sentence):
            return sentence
        return '\n' + sentence

    def processing_output(self, sentence):
        punctuationUpper    = ['.', '?', ':', '!']
        punctuationLower    = [';']
        punctuationDownLine = ['-', '+', '*']

        for i in punctuationUpper:
            sentence = ('{} '.format(i)).join([self.upperFirst(i.strip()) if len(i.strip()) > 1 else i.strip() for i in sentence.split(i)])
        for i in punctuationLower:
            sentence = ('{} '.format(i)).join([i.strip() for i in sentence.split(i)])
        for i in punctuationDownLine:
            sentence = ('\n{} '.format(i)).join([self.upperFirst(i.strip()) for i in sentence.split(i)])

        sentence = ' '.join([self.addDownLineBeforeListing(i.strip()) if '.' in i and len(i.strip()) <= 3 else i.strip() for i in sentence.split(' ')])

        return sentence.strip()

    def evaluate(self, input_sentence, max_length=247):
        # Load các từ điển
        teencode_dictionary     = self.taoTuDienTeenCode('./static/teencode/teencode.csv')
        vn_dictionary           = self.taoTuDienTiengViet('./static/vn_dictionary/vn_dictionary.txt')
        abbreviation_dictionary = self.taoTuDienVietTat('./static/acronyms/Acronyms.csv')

        # Chuẩn hóa từ viết tắt
        input_sentence = sentence = self.clean_text(input_sentence, teencode_dictionary, vn_dictionary, abbreviation_dictionary)

        # inp sentence is portuguese, hence adding the start and end token
        sentence = self.word_processing_question(sentence)
        new_sentence = []
        for i in sentence:
            if i in self.word2id_question:
                new_sentence.append(i)
        if len(new_sentence) < 1:
            raise Exception()
        sentence = self.preprocess_sentence(new_sentence)
        inputs   = self.padding(sentence, self.max_words_question)
        new_inputs = []
        for i in inputs:
            new_inputs.append(self.word2id_question[i])

        inputs   = [[i for i in new_inputs]]

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

        result = self.processing_output(result)

#         result = result.split(' ')
#         result = ' '.join(result)

        return result, input_sentence

    def answering(self, sentence):
        result, sentence = self.evaluate(sentence)
        print('-')
        print('Input: %s' % (sentence))
        print('Predicted the answer: {}'.format(result))
