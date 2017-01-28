from week2_challenges.linked_list import LinkedListNode

# For each element in linked list iterate over remaining
#elements in the list ~ O(n) * O(n) ~ O(n^2)
def remove_duplicates(head):
    i = head

    while i:
        j = i.getNext()
        prev = i
        while j:
            if i.getValue() == j.getValue():
                prev.setNext(j.getNext())
                prev = j.getNext()
            j = j.getNext()
        i = i.getNext()
    return head

# Start with an empty hashset. For each element in linked list,
# if node value is in the hashset, remove that node from list.
# If node value is not in the hashset, add it ~ O(n) * O(1) ~  O(n)
def remove_duplicates_with_hash(head):
    hset = set()
    cur = prev = head

    while cur:
        if cur.getValue() in hset:
            prev.setNext(cur.getNext())
        else:
            hset.add(cur.getValue())
        prev = cur
        cur = cur.getNext()
    return head


def main():
    head = None
    listValues = [1, 1, 2, 3, 3, 4, 4]

    head = LinkedListNode()
    head.setValuesFromArray(listValues)

    remove_duplicates(head)

    print(head.getNext().getValue() == 2)

    head.setValuesFromArray(listValues)

    remove_duplicates_with_hash(head)

    print(head.getNext().getValue() == 2)


if __name__ == '__main__':
    main()