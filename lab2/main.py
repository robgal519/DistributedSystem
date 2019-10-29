nodes_got_CS = 0


class Node:
    def __init__(self, id):
        self.id = id
        self.next = None
        self.out_queue = []
        self.in_queue = []
        self.in_CS = False
        self.CS_request_queue = []
        self.in_cs_count = 3

    def set_next(self, next):
        self.next = next

    def get_id(self):
        return self.id

    def input_queue(self, *messages):
        self.in_queue.extend(messages)

    def send_token(self, node, queue):
        if self.id == node:
            # received token for me!
            print("node {} got to CS".format(self.id))
            self.in_CS = True
            self.CS_request_queue = queue
            global nodes_got_CS
            nodes_got_CS += 1
        else:
            self.next.send_token(node, queue)

    def send_request(self):
        if(self.in_CS):
            self.send_token(self.id, [])
        else:
            self.next.out_queue.append(self.id)
            print("{} send request".format(self.id))

    def run(self):
        if(self.in_CS):
            self.CS_request_queue.extend(self.out_queue)
            self.out_queue = []

            self.in_cs_count -= 1
            if(self.in_cs_count == 0):
                if(len(self.CS_request_queue) > 0):
                    self.in_CS = False
                    self.send_token(
                        self.CS_request_queue[0], self.CS_request_queue[1:])
                    self.CS_request_queue = []
                else:
                    self.in_cs_count = 1
        else:
            self.next.input_queue(*self.out_queue)
            self.out_queue = []

    def in_to_out(self):
        out_queue_local = self.out_queue.copy()
        self.out_queue = self.in_queue.copy()
        self.in_queue = []
        self.out_queue.extend(out_queue_local)


if __name__ == "__main__":

    size_of_nodes = int(input("How many nodes are in the loop: "))

    nodes = [Node(i) for i in range(size_of_nodes)]
    for i in range(len(nodes)-1):
        nodes[i].set_next(nodes[i+1])
    nodes[-1].set_next(nodes[0])

    nodes[0].in_CS = True

    how_many_nodes_require_CS = int(
        input("How many nodes will want to enter CS: "))
    requests = [-1]*size_of_nodes

    for i in range(how_many_nodes_require_CS):
        single_entry = input("node_ID [0,{}) , time of entry: ".format(
            how_many_nodes_require_CS)).split(",")
        node_id = int(single_entry[0])
        time_of_entry = int(single_entry[1])
        requests[node_id] = time_of_entry
    i = 0
    while(how_many_nodes_require_CS > nodes_got_CS):
        for node in range(len(nodes)):
            if(requests[node] == i):
                nodes[node].send_request()
            nodes[node].run()
        for n in nodes:
            # pass frame to next node
            n.in_to_out()
        i += 1
