from collections import deque


class Node:
    def __init__(self, id):
        self.parent = None
        self.my_id = id
        self.localQueue = deque()

    def add_Parent(self, id):
        self.parent = id

    def rotate_parent(self):
        if len(self.localQueue) > 0:
            self.parent = self.localQueue.popleft()
            print("rotate {} with {}".format(self.my_id, self.parent))
            Nodes[self.parent].parent = None
            if len(self.localQueue) > 0:
                self.create_Request(self.my_id)

    def create_Request(self, id):
        if id not in self.localQueue:
            self.localQueue.append(id)

        if(self.parent != None):
            Nodes[self.parent].create_Request(self.my_id)

    def work(self):
        if len(self.localQueue) > 0:
            if self.parent == None:
                if self.localQueue[0] == self.my_id:
                    print("node {} enter CS".format(self.my_id))
                    global Request_counter
                    Request_counter = Request_counter-1
                    self.localQueue.popleft()
                    self.rotate_parent()

                else:
                    self.rotate_parent()


if __name__ == "__main__":
    number_of_Nodes = int(input("Number of nodes: "))
    Nodes = [Node(x) for x in range(number_of_Nodes)]

    print("Node[0] will be root!")

    for el in range(1, number_of_Nodes):
        parentId = int(input("Node[{}] parent is: ".format(el)))
        while(parentId >= number_of_Nodes or parentId < 0 or parentId == el):
            print("invalid node Id use range [0,{})".format(
                number_of_Nodes))
            parentId = int(input("Node[{}] parent is: ".format(el)))

        Nodes[el].add_Parent(parentId)

    Request_counter = int(input("How many Nodes make request: "))
    while(Request_counter < 0 or Request_counter >= number_of_Nodes):
        print("Wrong number of requests use value from range [0,{})".format(
            number_of_Nodes))
        Request_counter = int(input("How many Nodes make request: "))

    for i in range(Request_counter):
        requestNode = int(
            input("requesting node[0,{}): ".format(number_of_Nodes)))
        while(Request_counter < 0 or Request_counter >= number_of_Nodes):
            print("Wrong node ID")
            requestNode = int(
                input("requesting node[0,{}]: ".format(number_of_Nodes)))

        Nodes[requestNode].create_Request(requestNode)

    while(Request_counter > 0):
        for node in Nodes:
            node.work()
