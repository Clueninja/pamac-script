import random
def rand_search(alist, item):
    used = []
    while len(used) != len(alist):
        while (val := random.randint(0, len(alist)-1)) in used:
            continue
        
        if alist[val] == item:
            return True
        used.append(val)
    return False

if __name__ == "__main__":
    alist = [a for a in range(0,50)]

    print(rand_search(alist, 51))

        
