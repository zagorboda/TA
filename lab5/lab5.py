import matplotlib.pyplot as plt
import random
import time

class HashTable:
    def __init__(self):
        self.size = 101
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
        hashvalue = self.hashfunction(key,self.size)
        index = self.slots[hashvalue]
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = data
        else:
            nextslot = hashvalue
            if nextslot >= self.size-1:
                nextslot -= self.size-1
            else:
                nextslot += 1
            while self.slots[nextslot] != None and self.slots[nextslot] != index:
                if nextslot >= self.size-1:
                    nextslot -= self.size
                else:
                    nextslot += 1

            if self.slots[nextslot] == None:
                self.slots[nextslot]=data
            if self.slots[nextslot] == index:
                self.slots[nextslot]=data

    def setitem(self,key,data):
        self.put(key,data)

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def find(self,key,data):
        index = key%self.size
        ex = True
        while self.slots[index] != data:
            if index >= self.size-1:
                index -= self.size-1
            else:
                index += 1
            if index == key%self.size:
                print("Element {} doesn't exist".format(data))
                ex = False
                break
        if ex:
            print("Element {} exists in hash table. Index : {}".format(data, index+1))

H=HashTable()

# start_time = time.time()
for i in range(100):
    a = random.randint(10, 10000)
    H.setitem(a%(i*123+1), a)
# time1 = time.time() - start_time

H.setitem(99, 234)
for i in range(len(H.slots)):
    print("Element [{}] : ".format(i+1), H.slots[i])
# print(H.slots)

# start_time = time.time()
H.find(99, 10000)
# print("time")
# print("--- %s seconds ---" % (time.time() - start_time))

# x = [10,20,30,40,50,60,70,80,90,100]
# y1 = [0.0016, 0.0024, 0.0035, 0.0044, 0.0058, 0.0067, 0.0081, 0.0093, 0.0105, 0.011]
# y2 = [0.0039, 0.0041, 0.0054, 0.0067, 0.0080, 0.0094, 0.012, 0.0125, 0.0129, 0.0137]
# plt.plot(x, y1, color="red")
# plt.plot(x, y2, color="blue")
# plt.xlabel("Заповненість таблиці у у відсотках")
# plt.ylabel("Час роботи у секундах")
# plt.legend(['Ділення','Метод Дженкінса'], loc='upper left')
# plt.show()

def hash2(elem, max_num):
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

# start_time = time.time()
size = 101
slots = [None]*size
for i in range(size):
    a = random.randint(10, 10000)
    k = hash2(a, size)
    if slots[k] == None:
        slots[k] = a
        pass
    else:
        while True:
            k += 1
            if k>=size:
                k -= size
            if slots[k] is None:
                slots[k] = a
                break
            if k == hash2(a, size):
                slots[k] = a
                break

data = 234
length = 101
k = hash2(data, length)
if slots[k] == None:
        slots[k] = data
        pass
else:
    while True:
        k += 1
        if k>=size:
            k -= size
        if slots[k] is None:
            slots[k] = data
            break
        if k == hash2(a, size):
            slots[k] = data
            break

# start_time = time.time()
index = hash2(10000, length)
ex = True
while slots[index] != 10000:
    if index >= length-1:
        index -= length-1
    else:
        index += 1
    if index == hash2(10000, length):
        ex = False
        break

# print("--- %s seconds ---" % (time.time() - start_time))

# if ex:
#     print("Element {} exists in hash table. Index : {}".format(data, index))
