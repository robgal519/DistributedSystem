import _thread
N = 0
Entered_to_CS = 0
GlobalNodes = []


class Node:

    def __init__(self, id):
        self.ack_list = {}
        self.waiting_for_my_ACK = []
        self.id = id
        self.TS = 0
        self.TS_of_my_request = 0
        self.in_CS_counter = 3
        self.in_CS = False
        self.request_queue = []

    def triger_CS_request(self):
        self.ack_list[self.id] = 1
        self.TS += 1
        self.TS_of_my_request = self.TS
        print("{} Broadcast request".format(self.id))
        global GlobalNodes
        for node in GlobalNodes:
            if node.get_id() != self.id:
                node.handle_request(self, self.TS)

    def ack(self, node, TS):
        print("{} got ACK from {}".format(self.get_id(), node.get_id()))
        self.TS += 1
        if self.TS < TS:
            self.TS = TS+1
        self.ack_list[node.get_id()] = 1
        global N
        if(len(self.ack_list) == N):
            print("node {} enter CS".format(self.get_id()))
            self.in_CS = True
            global Entered_to_CS
            Entered_to_CS += 1

    def get_id(self):
        return self.id

    def handle_request(self, node, TS):
        self.request_queue.append([node, TS])

    def send_response(self):
        if self.in_CS:
            self.in_CS_counter -= 1
            if self.in_CS_counter == 0:
                self.in_CS = False
                print("node {} exit CS".format(self.id))
                self.ack_list = {}
                for node in self.waiting_for_my_ACK:
                    self.TS += 1
                    node.ack(self, self.TS)

        for node, TS in self.request_queue:
            if len(self.ack_list) > 0:
                # I also wait for CS
                if(TS < self.TS_of_my_request):
                    # the other has precedence
                    self.TS += 1
                    node.ack(self, self.TS)
                elif (TS == self.TS_of_my_request):
                    # equal TS check id
                    if self.get_id() < node.get_id():
                        self.waiting_for_my_ACK.append(node)
                    else:
                        self.TS += 1
                        node.ack(self, self.TS)
                else:
                    # I go first
                    self.waiting_for_my_ACK.append(node)
            else:
                self.TS += 1
                node.ack(self, self.TS)
        self.request_queue = []

    def print_ack_list(self):
        print(self.ack_list)


if __name__ == "__main__":
    nodes = int(input("number Of Nodes:"))
    number_of_requests = int(input("number of requests:"))

    GlobalNodes = [Node(x) for x in range(nodes)]
    N = len(GlobalNodes)

    enterToCS = [-1]*nodes
    for k in range(number_of_requests):
        line = input("node [0 {}] and time of request:".format(
            nodes-1)).split(',')
        for node, time in [line]:
            enterToCS[int(node)] = int(time)

    i = 0
    while(Entered_to_CS < 3):

        for e in range(N):
            if enterToCS[e] == i:
                GlobalNodes[e].triger_CS_request()

        for node in GlobalNodes:
            node.send_response()
        i += 1
