# Build project
## Python version
This script uses python 3.7, please make sure that you use python 3 to run it.

It is good practice to run python scripts in virtual environment, but this one does not have any dependency, therefore it is not needed.

# User Input

There is no user input, the only way to modify data structure is to modify it in code.

structure *Groups* describes all input values as array of dictionaries, where each dictionary represents resourceID and tuple with resource holder, and waiting list for that resource

so lets consider single resource:

> 1: (0, [2,3])

In this example resource *1* is hold by node **0**  and nodes **2** and **3** are waiting for that resource

# Output

information of a dependency cycle will be printed to standard output. If such a cycle exists, it will be also shown as a list of nodes that create that cycle.

# Application in Zip
[Download zip file](https://github.com/robgal519/DistributedSystem/releases/download/v0.4/lab4.zip)