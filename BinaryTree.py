class Node:
    def __init__(self, value: int, leftChild, rightChild):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild


# left
oneNode = Node(1, None, None)
fiveNode = Node(5, oneNode, None)
# right
elevenNode = Node(11, None, None)
twentyNode = Node(20, None, None)
fourteenNode = Node(14, elevenNode, twentyNode)

rootTenNode = Node(10, fiveNode, fourteenNode)


def search(node: Node, searchValue: int):
    if node == None:
        return False
    if node.value == searchValue:
        return True
    else:
        return search(node=node.rightChild, searchValue=searchValue) | search(node=node.leftChild, searchValue=searchValue)


print(search(rootTenNode, 11))
