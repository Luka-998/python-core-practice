class Hashmap:
    def __init__(self,capacity):
        self.capacity = capacity
        self.buckets =[]
        for i in range(capacity):
            self.buckets.append([]*i)
        print(self.buckets)

    def put(self,key,value):
        for i in self.buckets:
            if self.buckets == []:
                self.buckets[(key,value)]
                return self.buckets
z = Hashmap(5)
z.put('Luka',"jasovic")
