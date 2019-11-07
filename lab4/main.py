
import copy
if __name__ == "__main__":
    Groups = [
        {
            0: (0, [1]),
            1: (1, [2]),
            2: (2, [])
        },
        {
            3: (0, [1]),
            4: (3, [0, 1]),
            5: (None, [])
        }
    ]

    nodes = 4
    graph = [[] for i in range(nodes)]

    for group in Groups:
        for val in group.values():
            resources, waiting_for_resource = val
            for node in waiting_for_resource:
                graph[node].append(resources)

    wait_sets = [set()for i in range(nodes)]

    for i in range(nodes):
        wait_sets[i].update(graph[i])

    for inserts in range(nodes):
        for el in range(nodes):
            new_wait_list = copy.deepcopy(wait_sets[el])
            for l in new_wait_list:
                wait_sets[el].update(wait_sets[l])

    cycle_detected = False
    cycle = []
    for i in range(nodes):
        if i in wait_sets[i]:
            cycle_detected = True
            cycle = copy.deepcopy(wait_sets[i])
            break

    if cycle_detected:
        print("detected cycle!")
        print(cycle)
    else:
        print("there is no cycle!")
