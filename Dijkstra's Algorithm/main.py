
#take selected nodes and it's cost list to find the minimum node among selected nodes  
def get_min_node(cost_list, selected_node):
    min_node = -1
    min_val = float('inf')

    for i, node in enumerate(cost_list):
        if min_val > node:
            if i not in selected_node:
                min_node = i
                min_val = cost_list[i]
    return min_node

#to get the adjacent nodes of the minimum node
def get_adjacent_nodes(G, min_node):
    adj_nodes = []
    for i, node in enumerate(G[min_node]):
        if node != 0:
            adj_nodes.append(i)
    return adj_nodes

#applying Dijkstra's algorithm to get the minimum cost and path to the end_node

def dijkstra(G, start_node, end_node):

    cost_list = [float('inf') for i in range(len(G))]
    selected_node = set()

    cost_list[start_node] = 0           #initializing starting node to 0 in cost list
    paths = [[] for k in range(len(G))]         #to store the paths with minimum cost
    paths[start_node].append(start_node)
    min_node = start_node           #initially starting node will be minimum node
    
    #traversing the loop until we achieve the length of graph
    while len(selected_node) < len(G):
        selected_node.add(min_node)
        adj_nodes = get_adjacent_nodes(G, min_node)

        #for comparing and storing the minimum cost
        for node in adj_nodes:
            if cost_list[min_node] + G[min_node][node] < cost_list[node]:
                cost_list[node] = cost_list[min_node] + G[min_node][node]
                paths[node] = paths[min_node] + [node]
        min_node = get_min_node(cost_list, selected_node)

    return cost_list[end_node], paths[end_node]

#read the text file and get data in formatted way
def read_input(filename):
    G = []
    for lines in open(filename).readlines():
        G.append([int(num.strip()) for num in lines.split("\t")[-1].split(",")])
    return G


G = read_input("Data.txt")
for (start_node, end_node) in zip([54, 49, 94, 40, 2],[49, 94, 40, 2, 25]):
    cost, path = dijkstra(G, start_node, end_node)
    with open(f"{start_node}_to_{end_node}_output.txt", "w") as f:
        print(start_node, end_node, file=f)
        print(*path, file=f)
        print(cost, file=f)
        # print(start_node, end_node)
        # print(*path)
        # print(cost)

#TESTING on TOY example
# G = read_input("Toy.txt")
# start_node, end_node = 1, 6
# print(start_node, end_node)
# cost, path = dijkstra(G, start_node, end_node)
# print(*path)
# print(cost)