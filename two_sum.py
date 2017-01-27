def twoSum(self, A, B):
    d = dict()
    n = len(A)
    for i in range(n):
        if A[i] in d:
            return [d[A[i]] + 1, i + 1]
        elif B - A[i] not in d:
            d[B - A[i]] = i
    return []

[5, 5, 5]
0