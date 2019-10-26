# Build project
## Python version
This script uses python 3.7, please make sure that you use python 3 to run it.

It is good practice to run pythoin scripts in virtual environment, but this one does not have any dependency, therefore it is not needed.


# User Input
On the first prompt user has to provide number of nodes used in graph. next input is number of nodes that would like to request access to Critical Section.
After those inputs the user would have to provide number of the node and moment in time when the node will request access.
This time is not Event timer hold inside each node, but rather global snapshot when the graph is analysed.

# Algorithm

to simulate distributed system in single threaded application, the concept of snapshots has been created.
On this snapshot all nodes create their requests ( which are treated like happening in the same time) after the request section, there is response section. All nodes respond to the collected requests, and the cycle repeats. It can be treated as discreet time in real distributed system from outside perspective.

# Output

As the output we can see the log with state of the system. nodes raport when they enter CS and when they leave. Every ACK and request is also reported.

