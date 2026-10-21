class HashMap:
    def __init__(self,size,capacity):
        self.size = size
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def __repr__(self):
        return f"{self.__class__.__name__} has {len(self.buckets)} slots!"

    def _list(self):
        for i,(k,v) in enumerate(self.buckets):
            print(f'Bucket number: {i}\nKeys: {k}\nValues: {v}')

    def put(self,key,value):
        index = self.get_hash(key)
        bucket = self.buckets[index]

        for k,v in bucket:
            if k == key:
                bucket=(k,value)
        else:
            bucket = (key,value)
        print(bucket)
        

    def get_hash(self,key):
        hash_key = str(key)
        current_hash =0

        for c in hash_key:
            current_hash = (current_hash * 31) +ord(c)
        return current_hash % self.capacity

z = HashMap(0,10)
z.put('Luka',12)
z.put('Luka',14)
