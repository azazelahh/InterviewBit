# @param A : string
# @return an integer
def lengthOfLongestSubstring(self, A):
    if len(A) == 1:
        return 1
    letters = {}
    max_count = 0
    i = 0
    start = 0

    while i < len(A):
        if A[i] not in letters:
            letters[A[i]] = i
            i += 1
        else:
            if i - start > max_count:
                max_count = i - start
            i = start = letters[A[i]] + 1
            letters = {}
    if i - start > max_count:
        max_count = i - start
    return max_count