# @param A : list of integers
# @return a list of integers
def plusOne(self, A):
    for i in range(len(A) - 1, -1, -1):
        if A[i] == 9:
            A[i] = 0
            if i == 0:
                A = [1] + A
        else:
            A[i] = A[i] + 1
            break

    for i in A:
        if i > 0:
            break
        else:
            A = A[1:]
    return A