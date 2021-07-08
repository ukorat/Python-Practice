
#a = input("Enter Matrix A, commma separated \n ")
#b = input ("Enter Matrix B, comma separated \n ")

row = 3
col = 3

tempA = []
for i in range(0,row):
    for j in range(0,col):
        a = input("Enter Matrix A value for A[%d][%d]\n" % (i, j))
        tempA.append(int(a))
        
a = '1,2,3,4,5,6,7,8,9'
b = '7,8,9,4,5,6,1,2,3'

a = a.split(',')
b = b.split(',')

offset = 0
temp1 = []
temp2 = []
A = []
B = []
for i, j in zip(a, b):
    if offset < row :
        temp1.append(int(i))
        temp2.append(int(j))
        offset+= 1
        if offset == 2:
            A.append(temp1)
            B.append(temp2)
    else:
        temp1 = []
        temp2 = []
        temp1.append(int(i))
        temp2.append(int(j))
        offset = 1


C = []
temp = 0
tempL = []

for i in range(0,3):
    tempL = []
    for j in range(0,3):
        temp = 0
        for k in range(0,3):
            temp = temp + A[i][k] * B[k][j]
        tempL.append(temp)
    C.append(tempL)
