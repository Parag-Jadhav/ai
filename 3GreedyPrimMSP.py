import sys
def prim(graph, vertices):
    visited = [0]*vertices
    visited[0] = True
    num_of_edges = 1
    while num_of_edges < vertices:
        minn = sys.maxsize
        x = 0
        y = 0
        for i in range(vertices):
            if visited[i]:
                for j in range(vertices):
                    if ((not visited[j]) and graph[i][j]):
                        if minn > graph[i][j]:
                            minn = graph[i][j]
                            x = i
                            y = j
        print(f"Edge : {x} - {y} : {graph[x][y]}")
        visited[y] = True
        num_of_edges += 1
def main():
    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))
    graph = [[0]*vertices for _ in range(vertices)]
    print("Enter the edges with weights (format: source destination weight):")
    for _ in range(edges):
        source, destination, weight = map(int, input().split())
        graph[source-1][destination-1] = weight
        graph[destination-1][source-1] = weight
    prim(graph, vertices)
if __name__ == "__main__":
    main()
