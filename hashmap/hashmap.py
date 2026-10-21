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
    import matplotlib
    import matplotlib.pyplot as plt
    import random
    z = HashMap(10)

    z.put('M', 10)
    z.put('M', 20)  # Update
    z.put('N', 30)  # new key

    print(z.get('M'))  # 20
    print(z.size)      #  2

    z.delete('M')

    print(z.size)      #  1
    print('M' in z)    #  False

    x = []
    y = []


    for i, bucket in enumerate(z.buckets):
        x.append(i)
        y.append(len(bucket))

    plt.bar(x=x, height=y)
    plt.xlabel("Bucket Index")
    plt.ylabel("Number of Items (Collision Count)")
    plt.title("HashMap Bucket Distribution")
    plt.xticks(range(10))
    plt.show()