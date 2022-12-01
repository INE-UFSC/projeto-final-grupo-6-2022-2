import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    def __init__(self, datasource):
        self.datasource = datasource
        self.objectCache = {}
        try:
            self.load()
        except FileNotFoundError:
            self.dump()
    
    def dump(self):
        pickle.dump(self.objectCache, open(self.datasource, 'wb'))
    
    def load(self):
        self.objectCache = pickle.load(open(self.datasource, 'rb'))

    def add(self, key, obj):
        self.objectCache[key] = obj
        self.dump()

    def get(self, key):
        try:
            return self.objectCache[key]
        except KeyError as e:
            print(e)

    def remove(self, key):
        pass
    
    def get_all(self):
        return self.objectCache.values()