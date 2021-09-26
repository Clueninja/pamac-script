def poly(iteration,polygon):
    polygonalnumber = 1
    for n in range(iteration-1):
        polygonalnumber+=(polygon-1)+(polygon-2)*n
    return polygonalnumber
 
polygon = int(input("number of sides of polygon? "))
iteration = int(input("nth polygonal number? "))
print(poly(iteration,polygon))

