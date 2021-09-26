

def compute_hcf(x, y):
# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i     
    return hcf
    
number = 0
for x in range(1,1000):
    for y in range(1,1000):
        if x<y:
            if compute_hcf(x,y) ==1:
                if (x**2+y**2)**(1/2) in [i for i in range(0,1500)]:
                    number+=1
                    print(x,"^2 +",y,"^2","=",(x**2+y**2)**(1/2),"^2")

print (number)



