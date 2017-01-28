'''
Challenge 1 - Implement a Linked List
Implement a simple linked list in Java without using any collections classes.
The list should be implemented using a single class such that each instance
represents a single node in the list, encapsulating the node's value and
a reference to the following node, as well as a convenience method to initialize
a whole list from an array of values. The class should implement the following
interface:

public interface LinkedListNode<E> {

    /* getter/setter for this node's value */
    E getValue();
    void setValue(E value);

    /* getter/setter for the subsequent node, or null if this is the last node */
    LinkedListNode<E> getNext();
    void setNext(LinkedListNode<E> next);

    /**
     * Initialize this node and all of its subsequent nodes from
     * an array of values, starting with the head value at index 0
     *
     * @param listValues - the ordered values for the whole list
     */
    void setValuesFromArray(E[] listValues);

}
'''

class LinkedListNode:

    def __init__(self, x=None):
        self.value = x
        self.next = None

    def getValue(self):
        return self.value

    def setValue(self, x):
        self.value = x

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

    def setValuesFromArray(self, listValues):
        n = len(listValues)
        if n > 0:
            self.setValue(listValues[0])
        prev = self
        for i in range(1, n):
            node = LinkedListNode(listValues[i])
            prev.setNext(node)
            prev = node



def main():
    head = None
    listValues = [1, 2, 3]

    head = LinkedListNode()
    head.setValuesFromArray(listValues)

    if listValues[0] == head.getValue() and head.getNext() != None and listValues[1] == head.getNext().getValue() and head.getNext().getNext() !=  None and listValues[2] == head.getNext().getNext().getValue() and head.getNext().getNext().getNext() == None :
        print('Success')
    else:
        print('Fail')




if __name__ == '__main__':
    main()

