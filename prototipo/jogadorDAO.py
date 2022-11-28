import pickle

class JogadorDAO:
    def __init__(self):
        self.datasource = 'jogador.pkl'
        self.objectCache = {}
        try:
            self.load()
        except FileNotFoundError:
            self.dump()

    def dump(self):
        pickle.dump(self.objectCache, open(self.datasource, 'wb'))

    def load(self):
        self.objectCache = pickle.load(open(self.datasource, 'rb'))

