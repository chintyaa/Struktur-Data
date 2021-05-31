def myReverse(data):
    return [data[i] for i in range(len(data)-1, -1, -1)]

print(myReverse([5, 6, 7, 8, 9, 10, 11]))
