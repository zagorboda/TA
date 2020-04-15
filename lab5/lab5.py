import random

class HashTable:
    def __init__(self):
        self.size = 101
        self.slots = [None] * self.size
        # self.data = [None] * self.size

    def put(self,key):
        hashvalue = self.hashfunction(key,len(self.slots))
        index = self.slots[hashvalue]
        if self.slots[hashvalue] == None:
            # print("KEY!!!!!")
            self.slots[hashvalue] = key
            # self.data[hashvalue] = data
        else:
            # if self.slots[hashvalue] == key:
            #     self.data[hashvalue] = data  #replace
            # else:
            #  and self.slots[nextslot] != index
            # nextslot = self.rehash(hashvalue,len(self.slots))
            nextslot = hashvalue
            # print("index = ", nextslot)
            # print(self.slots[self.size-1])
            # while self.slots[nextslot] != None and self.slots[nextslot] != index:
            if nextslot >= self.size-1:
                nextslot -= self.size-1
                # nextslot += 1
            else:
                nextslot += 1
            while self.slots[nextslot] != None and self.slots[nextslot] != index:
                # nextslot = self.rehash(nextslot,len(self.slots))
                # print("slot = ", self.slots[nextslot])
                # print("i1 = ", nextslot)
                if nextslot >= self.size-1:
                    nextslot -= self.size
                else:
                    nextslot += 1
                # print("i2 = ", nextslot)
                # if self.slots[nextslot] == index:
                #     print("------- INDEX -------")

            if self.slots[nextslot] == None:
                # print("YES!!!")
                self.slots[nextslot]=key
            if self.slots[nextslot] == index:
                self.slots[nextslot]=key
            # print("slot = ", self.slots[nextslot])
                # self.data[nextslot]=data
            # else:
            #     self.data[nextslot] = data #replace

    def setitem(self,key):
        self.put(key)

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def find(self,key):
        print(key%self.size)

H=HashTable()

for i in range(101):
    a = random.randint(10, 10000)
    print(a)
    H.setitem(a)

# H.setitem(999)
# H.setitem(1111)
# H.setitem(777)
# find
# Знаходимо хеш, перевіраємо елемент, якщо ні - беремо наступний елемент і продовжуємо так само

# H.find(999)
# H.find(1111)
# H.find(777)

# if 999 in H.slots:
#     print("YES 999")
# if 1111 in H.slots:
#     print("YES 1111")
# if 777 in H.slots:
#     print("YES 777")

print(H.slots)
print(len(H.slots))
print(len(set(H.slots)))

if None in H.slots:
    print("None value")

def hash2(elem, max_num):
    # Хеш-функція Дженкінса
    ret = 0
    elem = str(elem)
    for char in elem:
        ret += ord(char)
        ret += (ret << 10)
        ret ^= (ret >> 6)
    ret += (ret << 3)
    ret ^= (ret >> 11)
    ret += (ret << 15)
    return ret % max_num


size = 101
slots = [None]*size
slot = []
for i in range(size):
    k = hash2(i, size)
    if slots[hash2(i, size)] == None:
        slots[hash2(i, size)] = i
        pass
    else:
        while True:
            k += 1
            if k>=size:
                k -= size
            if slots[k] is None:
                slots[k] = i
                break
            if k == hash2(i, size):
                slots[k] = i
                break
# l = [i for i in slots if i != None]
# print(sorted(l))
# print(slots)
