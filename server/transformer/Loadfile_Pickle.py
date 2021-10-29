import pickle

class Loadfile_Picker():
    def __init__(self, duongdan):
        super(Loadfile_Picker, self).__init__()
        self.duongdan=duongdan
    def load_word2id(self, name):
        with open(self.duongdan + name + '.pkl', 'rb') as f:
            return pickle.load(f)
    def load_id2word(self, name):
        with open(self.duongdan + name + '.pkl', 'rb') as f:
            return pickle.load(f)
    def load_question_embedding_matrix(self, name):
        with open(self.duongdan + name + '.pkl', 'rb') as f:
            return pickle.load(f)
    def load_answer_embedding_matrix(self, name):
        with open(self.duongdan + name + '.pkl', 'rb') as f:
            return pickle.load(f)
