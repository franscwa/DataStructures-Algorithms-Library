class HashTable(object):
    def __init__(self):
        self.table = {}
 
    def insert(self, key, value):
        self.table[key] = value
 
    def retrieve(self, key):
        return self.table[key]
 
    def delete(self, key):
        del self.table[key]
 
    def display(self):
        print(self.table)