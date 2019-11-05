# Build project
## Python version
This script uses python 3.7, please make sure that you use python 3 to run it.

It is good practice to run python scripts in virtual environment, but this one does not have any dependency, therefore it is not needed.


# User Input

On the first input application ask how many nodes will the tree have.
next it will ask to fill the dependencies between nodes by pointing what node is the parent for the node in question.
Pease make sure that the parent of the node is not the same node because node can not be parent to itself.

# Output

On the output we can find log of the application. Events that are logged are rotations between two nodes and enter to Critical section.
on the rotations the first id is the previous root, and second is the new one.

The algorithm ends when all requested nodes enter to CS


# Application in Zip
[Download zip file](https://github.com/robgal519/DistributedSystem/releases/download/v0.3/lab3.zip)