def merge(left, right):
    l = 0
    r = 0
    res = []
    while len(left) > l and len(right) > r:
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    while len(left) > l:
        res.append(left[l])
        l += 1
    while len(right) > r:
        res.append(right[r])
        r += 1
    return res

def merge_sort(l):
    if len(l) < 2:
        return l
    else:
        mid = len(l) // 2
        left = merge_sort(l[:mid])
        right = merge_sort(l[mid:])
        res = merge(left, right)
        return res

l = [5,9,1,3,4,6,6,3,2]
print(merge_sort(l))
