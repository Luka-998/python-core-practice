class HashMap:
    def __init__(self,capacity):
        self.size = 0 # number of k,v pairs per bucket
        self.capacity = capacity # number of slots / buckets 
        self.buckets = [[] for _ in range(capacity)]

    def __repr__(self):
        return f"{self.__class__.__name__} has {len(self.buckets)} slots!"

    def __contains__(self,key):
        index = self.get_hash(key)
        bucket = self.buckets[index]

        for k,v in bucket:
            if k ==key:
                return True
        return False

    def put(self,key,value):

        index = self.get_hash(key)
        bucket = self.buckets[index]

        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                break
        else:
            bucket.append((key,value))
            self.size+=1
    def get(self,key):
        index = self.get_hash(key)
        bucket = self.buckets[index]

        for k,v in bucket:
            if k == key:
                return v
        
        raise KeyError("Key not found!")

    def delete(self,key):
        index = self.get_hash(key)
        bucket = self.buckets[index]

        for i,(k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                break
        else:
            raise KeyError(key)

    def keys(self):
        return [k for bucket in self.buckets for (k,_) in bucket]

    def values(self):
        storage = []
        for bucket in self.buckets:
            for _,v in bucket:
                storage.append(v)
        return storage

    def get_hash(self,key):
        hash_key = str(key)
        current_hash =0
        for c in hash_key:
            current_hash = (current_hash * 31) +ord(c)
        return current_hash % self.capacity

if __name__ == "__main__":
    z = HashMap(10)

    z.put('M', 10)
    z.put('M', 20)  # ažuriranje
    z.put('N', 30)  # novi ključ

    print(z.get('M'))  # očekuješ 20
    print(z.size)      # očekuješ 2

    z.delete('M')

    print(z.size)      # očekuješ 1
    print('M' in z)    # očekuješ False