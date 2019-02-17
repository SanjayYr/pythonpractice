class Node:
    
    def __init__(self, parent1=None, parent2=None):
        self._parent1 = parent1
        self._parent2 = parent2
    
    def parent1(self):
        return self._parent1
    
    def parent2(self):
        return self._parent2


def areBloodRelated(node1, node2):
    
    if node1 == None or node2 == None:
        return False
    
    ancestors = set()
    getAncestors(ancestors, node1)
    
    return commonAncestorPresent(ancestors, node2)

def getAncestors(ancestors, node1):
    
    if node1.parent1() != None:
        ancestors.add(node1.parent1())
        getAncestors(ancestors, node1.parent1())

    if node1.parent2() != None:
        ancestors.add(node1.parent2())
        getAncestors(ancestors, node1.parent2())    


def commonAncestorPresent(ancestors, node2):
    
    if node2 == None: 
        return False
    else:
        return (node2 in ancestors) or commonAncestorPresent(ancestors, node2.parent1()) or commonAncestorPresent(ancestors, node2.parent2())

node1 = Node()
node2 = Node()
node3 = Node(node1, node2)
node4 = Node(node1, node2)
node5 = Node()
node6 = Node(node4, node5)

print(areBloodRelated(node3, node5))

#    1   2
#      X 
#    3   4  5
#         X
#         6
