'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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