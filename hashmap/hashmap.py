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
                bucket[i] = (key,value)
                break
        else:
            bucket.appned((key,value))
        

    def get(self,key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k,v in bucket.items():
            if k == key:
                return v
        raise KeyError
    def remove(self,key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i,(k,v) in enumerate(bucket.items()):
            if k == key:
                del bucket[i]
                self.size-=1
                break
        else:
            raise KeyError
                
    def keys(self):
        return[k for bucket in self.buckets for k,_ in bucket]
    def values(self):
        return[v for bucket in self.buckets for _,v in bucket]

    def items(self):
        return [(k,v) for bucket in self.buckets for (k,v) in bucket]
    def _hash_function(self,key):

        key_string = str(key)
        hash_result = 0

        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity


z = Hashmap(5)
z.put(1,'Luka')
z.put(2,'Luka')
