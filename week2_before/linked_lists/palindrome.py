'''
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:
- Expected solution is linear in time and constant in space.

For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param A : head node of linked list
# @return an integer
def lPalin(self, A):
    count = 0
    p = A

    while p:
        count += 1
        p = p.next

    mid = count / 2

    p = A

    i = 0
    while i < mid:
        i += 1
        p = p.next

    # reverse 2nd half
    prev = None
    while p:
        t = p
        p = p.next
        t.next = prev
        prev = t

    end = prev
    p = A

    while p and end:
        if p.next == None:
            return 1
        if p.val != end.val:
            return 0
        p = p.next
        end = end.next
    return 1