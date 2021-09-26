def fact(n):
    prod=1
    for num in range(n,0,-1):
        prod*=num
    return prod

def f(x,n):
    sum_of=0
    for r in range(0,n+1):
        sum_of+= fact(n)//(fact(n-r)*fact(r))*(x**r)*(1+x+x**2)**(n-r)
    return sum_of
target=1728**1728

def check(min,max):
    global target
    found=False
    n=min
    while n<max and found==False:
        n+=1
        if f(2,n)*f(3,n)==target:
            found=True
            print(n)

check(2000,3000)
#print(f(2,2592)*f(3,2592)==target)