# @param A : head node of linked list
# @param m : integer
# @param n : integer
# @return the head node in the linked list
def reverseBetween(self, A, m, n):
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