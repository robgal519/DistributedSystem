
import random

cycle_detected = False
class Node:
    def __init__(self, private):
        self.id = private
        self.private = 0
        self.public = 0
        self.parents = []
        self.childs = []
    
    def addParent(self, parent):
        self.parents.append(parent)
        nodes[parent].childs.append(self.id)
        # set private key
        self.setNewPrivateKey(int(random.random()*2*number_of_nodes))
        
        new_value = max(nodes[parent].public, self.public) + 1
        self.setNewPrivateKey(new_value)

        self.propagatePublicKey(self.public)

    
    def setNewPrivateKey(self, value):
        self.private = value
        self.public = value

    
    def propagatePublicKey(self, key):
        for parent in self.parents:
            if nodes[parent].public == key and nodes[parent].private == key:
                print("detected cycle!")
                global cycle_detected
                cycle_detected = True
            else:
                nodes[parent].public = max(nodes[parent].public, key)
                nodes[parent].propagatePublicKey(key)


if __name__ == "__main__":
    

    graph = {
        0:[1],
        1:[2],
        2:[3],
        3:[4],
        4:[5],
        5:[]
  
    }

    number_of_nodes = len(graph)

    nodes = [Node(i) for i in range(number_of_nodes)]



    for parent, childs in graph.items():
        for child in childs:
            nodes[child].addParent(parent)
            if cycle_detected:
                break
    
    if not cycle_detected:
        print("There is no cycle!")
