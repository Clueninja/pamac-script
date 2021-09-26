#! /bin/python
def rec(alist, item):
    if not len(alist):
        return False
    mid = len(alist)//2
    if alist[mid]==item:
        return True
    
    elif alist[mid]>item:
        return rec(alist[0:mid], item)
    
    elif alist[mid]<item:
        return rec(alist[mid+1:-1], item)
        


def main():
    alist = [a*2 for a in range (1,50)]
    print(rec(alist, int(input())))
    

if __name__ == "__main__":
    main()
