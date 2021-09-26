(lambda PT,NR: [[(PT.append([1]+[ PT[-1][i]+PT[-1][i+1] for i in range(len(PT[-1])-1)]+[1]),print(PT[-1]),PT.pop(0)) for _ in range(NR)]] )([[1]],4000)

def pascals(PT, NR)
    for _ in range(NR):
        for i in range(len(PT[-1])-1):  # for each item in the previous row
            PT.append([1]+[ PT[-1][i]+PT[-1][i+1] #append 1 + the sum of the two numbers above it in the previous row 
        print(PT[-1]) # print the last row
        PT.pop(0) # pop the first row 
