def create_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        edge = input("Enter edge (node1 node2): ").split()
        if len(edge) > 1:# Check if edge has at least 2 elements (node1 and node2)
            node1, node2 = edge[0], edge[1]# Add nodes to the graph if they don't exist yet
            graph.setdefault(node1, []).append(node2)  # Add node1 if it doesn't exist
            graph.setdefault(node2, []).append(node1)  # Add node2 if it doesn't exist
        else:
            print("Invalid edge input. Please enter two space-separated nodes.")
    return graph

found = False  # global variable to indicate whether the target node has been found

def dfs(visited, graph, node, target):
    global found
    if node not in visited and not found:
        print(node)
        if node == target:
            found = True
            return# Early return if target is found
        visited.add(node)
        for adjacent in graph[node]:# Handle non-existent nodes gracefully
            dfs(visited, graph, adjacent, target)

def bfs(visited, graph, node, target):
    visited.add(node)
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")
        if current_node == target:
            print("Node Found")
            return# Early return if target is found
        for adjacent in graph[current_node]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
    print("Node not Found")

graph = create_graph()
start_node = input("Enter the start node: ").strip()
target_node = input("Enter the target node: ").strip()
print("Following is the DFS:")
dfs(set(), graph, start_node, target_node)
if found:
    print("Node Found")
else:
    print("Node not Found")
print("\nFollowing is the BFS:")
bfs(set(), graph, start_node, target_node)
