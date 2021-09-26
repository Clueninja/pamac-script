def bubble_sort(array):
    size = len(array)-1
    for i in range(size):
        flag = False
        for j in range(size):
            if array[j]<array[j+1]:
                flag=True
                array[j], array[j+1] = array[j+1], array[j]
        if not flag:
            return array
    return array


def mergesort(array):
    if len(array)==1:
        return array
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    left = mergesort(left)
    right = mergesort(left)
    
    
    temp = []
    p_left = 0
    p_right = 0
    print(len(left), len(right))
    notsorted = True
    while notsorted:
        if p_left<len(left):
            temp.append(right[p_right])
            return temp
        elif (p_right<len(right)):
            temp.append(left[p_left])
            return temp
        elif left[p_left]<right[p_right]:
            temp.append(left[p_left])
            p_left+=1
        elif left[p_left]>right[p_right]:
            temp.append(right[p_right])
            p_right+=1
    return temp
    
    
print(mergesort([23,21,43,21,45,6,76,563,21]))
        
        
        
