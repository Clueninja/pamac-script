import pyplot
data=[[454,1316], [449,1259],[330,1007],[538, 1634],[525, 1535],[636, 1763],[516, 1363],[621,1814],[420, 1212],[474, 1340]]
def find_mean(coord, data):
    sumof =0
    if coord =="x":
        for item in data:
            sumof+=item[0]
    if coord =="y":
        for item in data:
            sumof+=item[1]
    return sumof/len(data)

meanx = find_mean("x", data)
meany = find_mean("y", data)
Sxy = 0
for item in data:
    Sxy += (item[0]-meanx)* (item[1]-meany)

Sxx = 0
for item in data:
    Sxx += (item[0]-meanx)*(item[0]-meanx)
print(Sxx, Sxy)
gradient = Sxy/Sxx

yintercept = meany-gradient*meanx

print("y=",gradient,"x +",yintercept)
