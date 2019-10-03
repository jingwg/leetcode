def findSubset(A, target):
    #stored the return values
    stored_dict = {}
    return rec(A, target, len(A)-1, stored_dict)
def rec(A, target, i, stored_dict):
    #set the key
    key = str(target) + ':' + str(i)
    if key in stored_dict:
        return stored_dict[key]
    #base cases
    if target == 0:
        return 1
    elif target < 0:
        return 0
    elif i < 0:
        return 0
    elif target < A[i]:
        temp = rec(A,target, i-1,stored_dict )
    else:
        temp = rec(A,target-A[i], i-1,stored_dict ) + rec(A,target, i-1,stored_dict )
    stored_dict[key] = temp
    return temp

assert findSubset([2,4,6,10], 16) == 2 #[6,10],[2,4,10]
assert findSubset([2,4,6,10], 0) == 1 #[6,10],[2,4,10]

#runtime : O(target+N)
