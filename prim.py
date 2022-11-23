# Prim's Algorithm (Minimum Spanning Tree)
# Time Complexity - O(V^2)

# Function to Implement Prim's Algorithm
def prim_algo(edge_list, node_count, adj_mat):
    max_weight = edge_list[len(edge_list)-1][2]+1 # Taking Last Weight as MAX (after Sorting)
    cost = [max_weight] * node_count
    previous = [None] * node_count
    tree_list = [False] * node_count
    cost[0] = 0
    previous[0] = -1

    # Adding the Closest Edge to the MST
    for i in range(node_count):

        min = max_weight

        for i in range(node_count):
            if cost[i] < min and tree_list[i] == False:
                min = cost[i]
                index_min = i
        closest = index_min

        tree_list[closest] = True

        for j in range(node_count):
            if (adj_mat[closest][j] > 0) and (tree_list[j] == False) and (cost[j] > adj_mat[closest][j]):
                cost[j] = adj_mat[closest][j]
                previous[j] = closest

    # Finding Minimum Cost of the MST
    path_cost = 0
    new_edge_list = []
    for i in range(len(previous)):
        if previous[i] != -1:
            new_edge_list.append((i, previous[i], cost[i]))
            path_cost += adj_mat[i][previous[i]]

    # Printing Cost and Edge List
    print("Cost of Minimum Spanning Tree: ", path_cost)
    print("Edge List (Start, End, Weight): ", new_edge_list)

    return edge_list

# Function to take User Input 
def custom_input():
    node_count = int(input("Enter the Number of Nodes:\n"))
    edge_count = int(input("Enter the Number of Edges:\n"))
    print("--------------------------------------------------------------------------")

    # Check for validity of edges
    if(edge_count > (node_count*(node_count-1)/2)):
        print("Invalid Input for Nodes")
        exit(1)

    # Generating Input for Function
    edge_list = []
    adj_mat = [([0]*node_count) for i in range(node_count)]

    for i in range(edge_count):

        edge_prop = []

        start_node = int(input("Enter Starting Node: "))
        end_node = int(input("Enter Ending Node: "))

        if start_node < node_count and end_node < node_count:
            if start_node > end_node:
                edge_prop.append(end_node)
                edge_prop.append(start_node)
            else:

                edge_prop.append(start_node)
                edge_prop.append(end_node)
        else:
            print("Invalid Input for Edges")
            exit(1)

        # Weight of node
        edge_weight = int(input("Weight of Edge: "))
        print("\n")

        # Creating Edge List
        edge_prop.append(edge_weight)
        edge_list.append(edge_prop)

        # Creating Adjacency Matrix
        adj_mat[start_node][end_node] = edge_weight
        adj_mat[end_node][start_node] = edge_weight

    # Sorting the Edge List according to Weights
    edge_list = sorted(edge_list, key=lambda x: x[2])

    prim_algo(edge_list, edge_count, adj_mat)

# Function to give Hard-Coded Input
def hard_input():
    edge_list = [[0, 1, 1], [2, 3, 1], [0, 4, 2], [2, 4, 2],
                 [1, 2, 3], [1, 4, 3], [3, 4, 3], [0, 2, 4]]
    adj_mat = [[0, 1, 0, 4, 2],
               [1, 0, 3, 0, 3],
               [0, 3, 0, 1, 2],
               [4, 0, 1, 0, 3],
               [2, 3, 2, 3, 0]]
    prim_algo(edge_list, 5, adj_mat)

# Function to Choose Input Method
def choice():
    print("--------------------------------------------------------------------------")
    choice = int(input("Enter a Choice:\n1.User Input\n2.Pre-defined Input\n\n"))
    print("--------------------------------------------------------------------------")
    if(choice == 1):
        custom_input()
    else:
        hard_input()

# Automatically Calls Function
if __name__ == "__main__":
    choice()
