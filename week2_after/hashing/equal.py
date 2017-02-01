# @param A : list of integers
# @return a list of integers
def equal(self, A):
    if all(x == A[0] for x in A):
        return [0, 1, 2, 3]
    sums = {}

    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            sumij = A[i] + A[j]

            if sumij not in sums:
                sums[sumij] = []
            if len(sums[sumij]) == 0:
                sums[sumij] += [i, j]
            if len(sums[sumij]) == 2:
                sum_inds = sums[sumij]
                A1 = sum_inds[0]
                B = sum_inds[1]
                C = i
                D = j

                if A1 < B and C < D and A1 < C and B != D and B != C:
                    sums[sumij] += [i, j]
    ls = []
    for s, inds in sums.items():
        if len(inds) == 4:
            ls += [inds]

    return sorted(ls)[0]