def rec_search(alist, item):
    mid = len(alist)//2
    if not len(alist):
        return False
    if (item<alist[mid]):
        return rec_search(alist[0:mid], item)
    elif(item>alist[mid]):
        return rec_search(alist[mid+1:], item)
    elif (item == alist[mid]):
        return True
def bin_search(alist, item):
    
    start = 0
    end = len(alist)
    mid = len(alist)//2
    found = False
    while (end-start>1):
        mid = (end+start)//2
        if alist[mid] == item:
            return True
        if item<alist[mid]:
            end = mid
        elif item>alist[mid]:
            start = mid
    return False


def main():
    alist = [(2*a+1)**2 for a in range(0,50)]
    print(alist)
    print(rec_search(alist, 1))
    
if __name__ == "__main__":
    main()
