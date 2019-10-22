
neighbours = []
nodes = 0

def getVisitedElements(visitedNodes):
    coppy = visitedNodes.copy()
    for el in visitedNodes:
        id = 0
        for n in neighbours[el]:
            if n==1:
                coppy.add(id)
            id+=1
    return coppy

def checkNode(node):
    el = {node}
    while True:
        prevSize = len(el)
        el = getVisitedElements(el)
        newSize=len(el)
        if prevSize==newSize:
            break

    if len(el) == nodes:
        return True
    else:
        return False


if __name__ == "__main__":
    nodes = int(input("number of nodes:"))
    for i in range(nodes):
        n = input("node {} neighbours:".format(i)).split(",")

        nn = [0] * nodes
        for e in n:
            id = int(e)
            if(id<nodes):
                nn[id] = 1;
        neighbours.append(nn);
    # print(neighbours);

    for e in range(nodes):
       print("node {} can reach all other nodes : {}".format(e,checkNode(e)))