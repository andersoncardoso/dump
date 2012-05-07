

class ModelBase():
    """
    Any model who inherits from model base must define collection and _fields
    """
#    def __init__(self):
#        if not 'collection' in self.__dict__:
#            self.collection = None
#        if not '_fields' in  self.__dict__:
#            self._fields = []
    
    def save(self):
        self._id = self.collection.insert({field:getattr(self, field) for field in self._fields})

    def all(self,):
        return self.collection.find()

    def get(self, query):
        return self.collection.find_one(query)

    def filter(self, query):
        return self.collection.find(query)

    

