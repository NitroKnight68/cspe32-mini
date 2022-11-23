# Approximation of Minimum Hamiltonian Cycle (using Triangle Inequality)
# Time Complexity - O(E logV)

from kruskal import kruskal_algo

# Function to Implement DFS
def dfs(graph, node, node_num, vis=None):

    if vis is None:
        vis = set()
    vis.add(node)

    for next in graph[node] - vis:
        dfs(graph, next, node_num, vis)
    return vis

# Function to find Minimum Hamilton Cycle (approximately)
def hamilton_cycle(edge_list,node_count,adj_mat):
   
    # Finding MST using Kruskal's
    tree_edge_list = kruskal_algo(edge_list,node_count,adj_mat)

    # Finding Neighbours for DFS
    neighbours = {}
    for i in range(node_count):
        neighbours[i] = set()
    for edge in tree_edge_list:
        neighbours[edge[0]].add(edge[1])
        neighbours[edge[1]].add(edge[0])
    
    # Storing the DFS Path
    path = dfs(neighbours,0,node_count)

    order = []
    for vertex in path:
        order.append(vertex)
    
    new_edge_list = []

    # Finding Minimum Cost of the Hamiltonian Path
    path_cost = 0
    for i in range(node_count-1):
        new_edge_list.append((order[i],order[i+1],adj_mat[order[i]][order[i+1]]))
        path_cost += adj_mat[order[i]][order[i+1]]
    new_edge_list.append((order[0],order[node_count-1],adj_mat[order[0]][order[node_count-1]]))
    path_cost += adj_mat[order[0]][order[node_count-1]]
    
    # Printing Minimum Cost and Edge List
    print("\nCost of Minimum Hamiltonian Path: ", path_cost)
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

    hamilton_cycle(edge_list, edge_count, adj_mat)

# Function to give Hard-Coded Input
def hard_input_1():
    edge_list = [[0, 1, 10],[0, 4, 10],[2, 4, 10],[0, 3, 12],[1, 3, 12],[1, 2, 12],[2, 3, 14],[0, 2, 14],[1, 4, 16],[3, 4, 16]]
    adj_mat = [[0,10,14,12,10],
                [10,0,12,12,16],
                [14,12,0,14,10],
                [12,12,14,0,16],
                [10,16,10,16,0]]
    hamilton_cycle(edge_list,5,adj_mat)

# Function to give Hard-Coded Input
def hard_input_2():
    edge_list = [[2, 3, 8],[1, 2, 10],[0, 2, 11],[0, 3, 12],[1, 3, 15],[0, 1, 18]]
    adj_mat = [[0,18,11,12],
                [18,0,10,15],
                [11,10,0,8],
                [12,15,8,0]]
    hamilton_cycle(edge_list,4,adj_mat)

# Function to Choose Input Method
def choice():
    print("--------------------------------------------------------------------------")
    choice = int(input("Enter a Choice:\n1.User Input\n2.Pre-defined Input Case 1\n3.Pre-define Input Case 2\n\n"))
    print("--------------------------------------------------------------------------")
    if(choice == 1):
        custom_input()
    elif(choice == 2):
        hard_input_1()
    else:
        hard_input_2()

# Automatically Calls Function
if __name__ == "__main__":
    choice()