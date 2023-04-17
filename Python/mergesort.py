def merge(left, right):
    l = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def mergeSort(l):
    if len(l) < 2:
        return l
    else:
        m = len(l)//2
        left = mergeSort(l[:m])
        right = mergeSort(l[m:])
        return merge(left, right)

l = [2,4,7,3,7,5,8,3,10]
print(mergeSort(l))
