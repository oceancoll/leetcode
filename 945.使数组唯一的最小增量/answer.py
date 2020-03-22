def minIncrementForUnique(A):
    """
    :type A: List[int]
    :rtype: int
    """
    A = sorted(A)
    num = 0
    for i in range(1, len(A)):
        if A[i] <= A[i-1]:
            tmpnum = A[i-1] - A[i] + 1
            num += tmpnum
            A[i] += tmpnum
    return num


print minIncrementForUnique([1,2,2])
print minIncrementForUnique([3,2,1,2,1,7])
