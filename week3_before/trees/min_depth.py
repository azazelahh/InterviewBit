# @param A : root node of tree
# @return an integer
def minDepth(self, A):
    h = self.min_height(A)
    return h


def min_height(self, node):
    if node == None:
        return 0
    left = self.min_height(node.left)
    right = self.min_height(node.right)

    min_height = 0
    if right == 0 and left == 0:
        min_height = 0
    elif right == 0:
        min_height = left
    elif left == 0:
        min_height = right
    else:
        min_height = min(left, right)

    return min_height + 1