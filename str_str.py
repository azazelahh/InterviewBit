# @param haystack : string
# @param needle : string
# @return an integer
def strStr(self, haystack, needle):
    if len(needle) == 0 or len(haystack) == 0:
        return -1

    for i in range(0, len(haystack)):
        for j in range(0, len(needle)):
            if len(haystack) - i < len(needle):
                break
            if needle[j] != haystack[i + j]:
                break
            if j == len(needle) - 1:
                return i
    return -1