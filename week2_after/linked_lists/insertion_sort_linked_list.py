# @param A : head node of linked list
# @return the head node in the linked list
def insertionSortList(self, A):
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