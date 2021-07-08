inData = [1,2,3,4,5,6,7,8,10,10,11,12,3,5,2343,54,33,23,545,32,5,5,3432,5,6,90,6,3,1]

change = 1
count = 0

while (change != 0):
    change = 0
    for i in range(0, len(inData)-1, 2):
        if inData[i] < inData[i+1]:
            change = 1
            inData[i], inData[i+1] = inData[i+1], inData[i]

    for i in range(1, (len(inData)-1), 2):
        if inData[i] < inData[i+1]:
            change = 1
            inData[i], inData[i+1] = inData[i+1], inData[i]

    if inData[0] < inData[len(inData)-1]:
        change = 1
        inData[0], inData[len(inData)-1] = inData[len(inData)-1], inData[0]
        
    count+=1
        
            
    
