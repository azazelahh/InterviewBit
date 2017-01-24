# @param A : string
# @return string
def reverseWords(self, A):
    if len(A) <= 1:
        return A

    result = ' '.join(reversed(A.split()))

    return result