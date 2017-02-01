# @param A : head node of linked list
# @return the head node in the linked list
def deleteDuplicates(self, A):
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