# Kruskal's Algorithm (Minimum Spanning Tree)
# Time Complexity - O(E logV)

# Function to find the Parent/Root Node
def node_root(root,node):
    if node != root[node]:
        root[node] = node_root(root,root[node])
    return root[node]

# Function to create Graph from Subtrees
def join_graph(root, tree_size, x, y):
    root_x = node_root(root, x)
    root_y = node_root(root, y)
    if tree_size[root_x] < tree_size[root_y]:
        root[root_x] = root_y
    elif tree_size[root_x] > tree_size[root_y]:
        root[root_y] = root_x
    else:
        root[root_y] = root_x
        tree_size[root_x] += 1

# Function to Implement Kruskal's Algorithm
def kruskal_algo(edge_list,node_num,adj_mat):
    result=[]
    i,e=0,0
    root=[]
    tree_size=[]
    for node in range(node_num):
        root.append(node)
        tree_size.append(0)
    
    while e < (node_num - 1):

        # Finding Edge with Minimum Weight
        node1, node2, weight = edge_list[i]
        i = i + 1
        
        x = node_root(root, node1)
        y = node_root(root, node2)

        if x != y:
            e = e + 1
            result.append([node1, node2, weight])
            join_graph(root, tree_size, x, y)
    
    # Finding Minimum Cost of the MST
    new_edge_list = []
    path_cost = 0
    for edge in result:
        new_edge_list.append((edge[0],edge[1],edge[2]))
        path_cost += edge[2]
    
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

    kruskal_algo(edge_list, edge_count, adj_mat)

# Function to give Hard-Coded Input
def hard_input():
    edge_list = [[0, 1, 1], [2, 3, 1], [0, 4, 2], [2, 4, 2],
                 [1, 2, 3], [1, 4, 3], [3, 4, 3], [0, 2, 4]]
    adj_mat = [[0, 1, 0, 4, 2],
               [1, 0, 3, 0, 3],
               [0, 3, 0, 1, 2],
               [4, 0, 1, 0, 3],
               [2, 3, 2, 3, 0]]
    kruskal_algo(edge_list, 5, adj_mat)

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
