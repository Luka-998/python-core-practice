    
class DictMethods:
    def __init__(self,slots):
        self.slots = slots
        self.buckets = [[] for _ in range(slots)]

    def __repr__(self):
        return f"Number of slots: {self.slots}"

    def _list(self):
        pass

    def put(self,key,value):
        pass

    def _get_hash(self,key):
        key_str = str(key)
        hash_result = 0

        for s in key_str:
            hash_result = (hash_result * 31 + ascii(s)) % self.slots
        print(hash_result)


p = DictMethods(10)
p._get_hash("Name")