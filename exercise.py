import sys
import random


def prettyPrint(A):
    len_x = 2 * A - 1
    x = [[0] * len_x for _ in range(len_x)]

    for i in range(0, len_x):
        for j in range(0, len_x):
            top = j
            bot = (len_x - 1) - j
            left = i
            right = (len_x - 1) - i

            sub = min([top, bot, left, right])

            x[i][j] = A - sub
    return x


def kthsmallest(A, k):
    rand = random.randint(0, len(A) - 1)
    less = []
    greater = []
    equal = []
    pivot = A[rand]

    for i in A:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)
        elif i == pivot:
            equal.append(i)

    if len(less) >= k:
        return kthsmallest(less, k)
    elif len(less) + len(equal) >= k:
        return equal[0]
    else:
        adjusted_k = k - (len(less) + len(equal))
        return kthsmallest(greater, adjusted_k)


def nextGreater(A):
    result = []

    for i in range(0, len(A)):
        if i + 1 <= len(A) - 1:
            for j in range(i + 1, len(A)):
                if A[j] > A[i]:
                    result.append(A[j])
                    break
                elif j == len(A) - 1:
                    result.append(-1)
        else:
            result.append(-1)
    return result


def longestConsecutive(A):
    pairs = dict.fromkeys(A)
    cur_len = 0
    max_len = 0

    for i in A:
        if i - 1 in pairs:
            pairs[i - 1] = i

    for key, val in pairs.items():
        if key in pairs and key - 1 not in pairs:
            cur_len = 1
            while val in pairs:
                cur_len += 1
                val = pairs[val]
            if max_len < cur_len:
                max_len = cur_len
    return max_len


def reverseWords(A):
    if len(A) <= 1:
        return A

    result = ''
    i = -1
    start = -1
    end = -1
    whitesp = False

    while i >= -len(A):
        if i == -len(A):
            if result == '':
                result += A
            else:
                result += A[0: end].strip()
            break
        if A[i] == ' ':
            if whitesp == False:
                whitesp = True
                if result == '':
                    start = i + 1
                    result += A[start:] + ' '
                else:
                    start = i + 1
                    result += A[start: end] + ' '
            end = i
        else:
            whitesp = False
        i -= 1

    return result


def atoi(A):
    integer = 0
    int_began = False
    negative = False
    for i in A:
        if i.isdigit():
            if int_began == False:
                int_began = True
            integer *= 10
            integer += int(i)
        else:
            if int_began:
                break
            else:
                if i == '-':
                    negative = True
    if negative:
        return 0 - integer
    return integer


def maxLength(a, k):
    mlen = 0
    clen = 0
    sum = 0

    for i in range(0, len(a)):
        for j in range(i, len(a)):
            tmp_sum = sum + a[j]
            if tmp_sum <= k:
                clen += 1
                sum += a[j]
        if clen > mlen:
            mlen = clen
        clen = 0
        sum = 0
        tmp_sum = 0
    return mlen


# @param B : integer
# @return a list of integers
def twoSum(A, B):
    d = dict()
    n = len(A)
    for i in range(n):
        if A[i] in d:
            return [d[A[i]]+1,i+1]
        elif B-A[i] not in d:
            d[B-A[i]]=i
    return []


def minWindow(S, T):
    ts = dict.fromkeys(T, -1)
    count = 0
    windows = {}

    for i in range(0, len(S)):
        if S[i] in ts:
            if ts[S[i]] == -1:
                count += 1
                ts[S[i]] = []
            ts[S[i]] += [i]
        if (len(ts) > 1 and count == len(ts)) or (len(ts) == 1 and count == len(T)) or (len(ts) == 1 and len(T) > 0 and ts[T[0]] != -1 and len(ts[T[0]]) == len(T)):
            min_val = len(S) + 1
            min_list = []
            max_val = -1
            max_list = []
            for k, v in ts.items():
                for val in v:
                    if val <= min_val:
                        min_val = val
                        min_list = v
                    if val >= max_val:
                        max_val = val
                        max_list = v
                ts[k] = -1
            if min_list == max_list:
                indxs = min_list[0: len(T)]
                if len(indxs) == 1:
                    return S[indxs[0]]
                return S[indxs[0]: indxs[-1] + 1]
            if len(windows) == 0:
                windows[max_val - min_val] = [min_val, max_val]
            elif max_val - min_val < windows.items()[0][0]:
                windows = {}
                windows[max_val - min_val] = [min_val, max_val]
            count = 0

    if len(windows) == 0:
        return ''

    inds = windows.items()[0][1]

    return S[inds[0]: inds[1] + 1]


def anagrams(A):
    d = {}
    n = len(A)
    solutions = []

    for i in range(n):
        seti = set(A[i])
        for j in range(i + 1, n):
            setj = set(A[j])
            if seti == setj:
                solutions += [[i + 1, j + 1]]

    return solutions

# Main function
def main():
    A = [ 'cat', 'dog', 'god', 'tca' ]
    B = 0

    #prettyPrint(A)
    #ksmallest(A, k)
    #nextGreater(A)
    #longestConsecutive(A)
    #reverseWords(A)
    #atoi(A)
    #maxLength(A, k)
    #twoSum(A, B)
    #minWindow(A, B)
    anagrams(A)

if __name__ == '__main__':
    main()