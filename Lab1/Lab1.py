import random
import time
import datetime

print("Program count number of zeroes in matrix")
while True:
    enter = input("Random - 1, manual - 2, file - 3")
    if (enter == '1') or (enter == '2') or (enter == '3'):
        break

a = []
b = []

if enter == '1':
    while True:
        m = input("Enter number of rows: ")
        try:
            m = int(m)
            if m < 0:   
                print("Input must be a positive integer")
                continue
            break
        except ValueError:
            print("Not an int!")

    while True:
        n = input("Enter a number of columns: ")
        try:
            n = int(n)
            if n < 0:
                print("Input must be a positive integer")
                continue
            break
        except ValueError:
            print("Not an int!")

    while True:
        while True:
            left = input("Enter left limit of generation: ")
            try:
                left = int(left)
                break
            except ValueError:
                print("Not an int!")

        while True:
            right = input("Enter right limit of generation: ")
            try:
                right = int(right)
                break
            except ValueError:
                print("Not an int!")

        if left < right:
            break
        else:
            print("Left limit must be smaller than right")

    start_time = datetime.datetime.now()
    for i in range(m):
        for j in range(n):
            b.append(random.randint(left, right))
        a.append(b)
        b = []
        print(a[i])

    count = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 0:
                count += 1
    print("Numbers of zeroes", count) 
    print("Algorithm takes %s microseconds to execute" % (datetime.datetime.now() - start_time).microseconds)

elif enter == '2':
    while True:
        m = input("Enter number of rows: ")
        try:
            m = int(m)
            if m < 0:
                print("Input must be a positive integer")
                continue
            break
        except ValueError:
            print("Not an int!")

    while True:
        n = input("Enter a number of columns: ")
        try:
            n = int(n)
            if n < 0:
                print("Input must be a positive integer")
                continue
            break
        except ValueError:
            print("Not an int!")
    for i in range(m):
        for j in range(n):
            b.append(input("A[%d][%d]" % (i, j)))
        a.append(b)
        b = []
    for i in range(len(a)):
        print(a[i])

    start_time = datetime.datetime.now()
    count = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == '0':
                count += 1
    print("Numbers of zeroes", count)
    print("Algorithm takes microseconds %s second to execute" % (datetime.datetime.now() - start_time).microseconds)

elif enter == '3':
    a = []
    while True:
        try:
            name = input("Enter filename: ")
            open(name)
            break
        except FileNotFoundError:
            print("Invalid name of file")
    start_time = datetime.datetime.now()
    j = 0
    with open(name) as f:
        lines = f.readlines()
        count = 0
        stop = False
        for j in range(len(lines)):
            if stop is False:
                if len(lines[j].split()) == len(lines[0].split()):
                    for word in lines[j].split():
                        if word == '0':
                            count += 1
                else:
                    print("Incorrect matrix in file")
                    stop = True
        if stop is False:
            print("Numbers of zeroes", count)
            print("Algorithm takes microseconds %s second to execute" % (datetime.datetime.now() - start_time).microseconds)

input()
