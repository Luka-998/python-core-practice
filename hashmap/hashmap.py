class Hashmap:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0 #number of elements in the list
        self.buckets = [[] for _ in range(capacity)] 

    def __len__(self):
        return self.size

    def __contains__(self,key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k,v in bucket:
            if k == key:
                return True
        return False        

    def put(self,key,value):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[index].append((key,value))
        

    def get(self,key):
        pass
    def remove(self,key):
        pass
    def keys(self):
        pass
    def values(self):
        pass

    def items(self):
        pass
    def _hash_function(self,key):

        key_string = str(key)
        hash_result = 0

        for c in key_string:
            hash_result = (hash_result * 31 + ascii(c)) % self.capacity


z = Hashmap(5)
z.put('Luka',"jasovic")
