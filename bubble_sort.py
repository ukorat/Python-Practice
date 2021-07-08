#bubble sort

data = [1,2,3,4,5,6,7,8,10,10,11,12,3,5,2343,54,33,23,545,32,5,5,3432,5,6,90,6,3,1]


for i in range(0, len(data)-1):
    for j in range(i, len(data)):
        if data[i] < data[j]:
            data[i], data[j] = data[j], data[i]
