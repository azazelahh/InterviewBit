# @param A : head node of linked list
# @param B : integer
# @return the head node in the linked list
def removeNthFromEnd(self, A, B):
    n = 0
    cur = A

    while cur:
        n += 1
        cur = cur.next
    if B >= n:
        A = A.next
        return A

    i = 0
    cur = A
    prev = None
    index = n - B

    while i < index:
        prev = cur
        cur = cur.next
        i += 1
    if prev != None and cur != None:
        prev.next = cur.next

    return A
