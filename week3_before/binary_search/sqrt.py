# @param A : integer
# @return an integer
def sqrt(self, A):
    if A == 0:
        return A
    if A < 4:
        return 1
    low = 0
    high = A
    while high - low > 1:
        mid = (low + high) / 2
        if mid * mid <= A:
            low = mid
        else:
            high = mid
    return low