import sys
import random
from decimal import Decimal

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


# @param A : head node of linked list
# @param B : head node of linked list
# @return the head node in the linked list
def addTwoNumbers(self, A, B):
    r = head = prev = None
    a = A
    b = B
    carry = 0

    while a or b:
        val_a = 0
        val_b = 0
        if a:
            val_a = a.val
        if b:
            val_b = b.val

        sumab = val_a + val_b + carry
        carry = 0
        if sumab > 9:
            sumab = sumab - 10
            carry = 1
        node = ListNode(sumab)
        if r == None:
            r = node
            head = r
        else:
            prev = r
            r.next = node
            r = node
        if sumab == 0 and (a == None or a.next == None) and (b == None or b.next == None):
            if carry == 1:
                node = ListNode(carry)
                r.next = node
            else:
                prev.next = None
            return head
        if a:
            a = a.next
        if b:
            b = b.next
    return head


def maxPoints(A, B):
    if len(A) == 0:
        return 0
    max_slopes = 0

    for i in range(0, len(A)):
        x1 = A[i]
        y1 = B[i]
        point_slopes = {}
        dups = 1
        for j in range(i + 1, len(A)):
            if i != j:
                x2 = A[j]
                y2 = B[j]
                y = y2 - y1
                x = x2 - x1
                slope = 0
                if x1 == x2 and y1 == y2:
                    dups += 1
                else:
                    if y == 0:
                        slope = 'y'
                    elif x == 0:
                        slope = 'x'
                    else:
                        slope = Decimal(y2 - y1) / (x2 - x1)
                    if slope not in point_slopes:
                        point_slopes[slope] = 0

                    point_slopes[slope] += 1
        if dups == len(A):
            return dups
        slope_count = 0
        if len(point_slopes) > 0:
            slope_count = max(point_slopes.values())
        slope_count += dups
        if slope_count > max_slopes:
            max_slopes = slope_count

    return max_slopes


# @param A : list of integers
# @return a list of integers
def equal(A):
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


def convert_bullshit(string):
    nums = string.split(" ")
    is_x = True
    x = list()
    y = list()
    for num in nums:
        if is_x:
            x.append(int(num))
        else:
            y.append(int(num))
        is_x = not is_x
    return x, y


# @param A : string
# @return an integer
def lengthOfLongestSubstring(A):
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


# @param A : head node of linked list
# @return the head node in the linked list
def insertionSortList(A):
    unsorted = A
    head = None
    while unsorted:
        current = unsorted
        unsorted = unsorted.next
        if not head or current.val < head.val:
            current.next = head;
            head = current;
        else:
            find = head;
            while find and find.next and current.val > find.next.val:
                find = find.next
            current.next = find.next
            find.next = current
    return head


# @param A : head node of linked list
# @return the head node in the linked list
def deleteDuplicates(A):
    cur = nextn = A

    while cur and cur.next:
        if cur == nextn:
            nextn = cur.next
        if cur.val == nextn.val:
            cur.next = nextn.next
            nextn = cur.next
        else:
            cur = cur.next
            nextn = nextn.next

    return A


# @param A : head node of linked list
# @param m : integer
# @param n : integer
# @return the head node in the linked list
def reverseBetween(A, m, n):
    i = 1
    cur = A
    prev = before = after = start = end = None

    if cur.next == None:
        return A

    while cur:
        if i > n:
            break
        if i == m:
            before = prev
            start = cur
        if i == n:
            if cur.next != None:
                after = cur.next
            end = cur
        if i > m and i <= n:
            if prev == A:
                A = cur
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        else:
            prev = cur
            cur = cur.next
        i += 1
    if before != None:
        before.next = end
    start.next = after

    return A


# Main function
def main():
    node0 = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    node5 = ListNode(6)
    A = node0
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    m = 3
    n = 5
    #B = node3
    #A = [ 3, 4, 7, 1, 2, 9, 8 ]
    #B = [-17, -16, -17, -4, -13, 20]


    bullshit = "-4 2 -17 16 -4 0 -5 -10 -15 12 10 17 -5 -10 -17 -3 -2 -11 2 -15 5 -20 -14 -5 7 -14 14 10 4 -10 -9 -12 -10 -3 -10 -11 20 7 -10 -20 4 -14 -20 -14 -16 -8 -3 4 5 16 -11 -12 18 16 -17 -10 -2 -14 16 -5 -14 3 -6 11 6 7 3 2 -3 1 2 17 -20 -10 8 -5 -20 17 12 0 18 9 -19 -3 14 4 17 -9 -15 -3 4 -6 -5 10 1 7 -5 14 15 6 14 -10 -16 11 -11 -9 16 14 0 11"


    #prettyPrint(A)
    #ksmallest(A, k)
    #nextGreater(A)
    #longestConsecutive(A)
    #reverseWords(A)
    #atoi(A)
    #maxLength(A, k)
    #twoSum(A, B)
    #minWindow(A, B)
    #anagrams(A)
    #addTwoNumbers(A, B)
    #points = convert_bullshit(bullshit)
    #maxPoints(points[0], points[1])
    #equal(A)
    #lengthOfLongestSubstring(A)
    #insertionSortList(A)
    reverseBetween(A, m, n)

if __name__ == '__main__':
    main()


