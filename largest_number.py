# @param A : tuple of integers
# @return a strings
def largestNumber(self, A):
    def compare(x, y):
        xy = str(x) + str(y)
        yx = str(y) + str(x)

        if xy > yx:
            return -1
        elif xy == yx:
            return 0
        else:
            return 1

    A = sorted(A, cmp=compare)

    while A[0] == 0 and len(A) > 1:
        A = A[1:]

    return ''.join(map(str, A))