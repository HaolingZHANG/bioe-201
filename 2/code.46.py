def function(edges: list):
    graph = {}
    for edge in edges:
        former, latters = edge.split(" -> ")
        graph[int(former)] = list(map(int, latters.split(",")))

    # Initialize data structures
    visited, result = set(), []

    def dfs(sample):
        if sample not in visited:
            for neighbor in graph.get(sample, []):
                dfs(neighbor)
            visited.add(sample)
            result.append(sample)

    # Perform DFS from each unvisited vertex.
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    # The result list needs to be reversed to get the topological order.
    return result[::-1]


if __name__ == "__main__":
    p_1 = [
        "0 -> 16,17,2,24,3,6",
        "1 -> 11,27,5",
        "10 -> 30",
        "11 -> 29",
        "13 -> 18,23,24,33,34",
        "14 -> 17,24",
        "15 -> 17,18,26,28,34",
        "16 -> 17,26",
        "17 -> 19,23",
        "18 -> 20",
        "19 -> 28",
        "2 -> 21,26,29,6,8",
        "20 -> 28",
        "22 -> 27,28",
        "23 -> 32",
        "25 -> 26,29,30,31",
        "26 -> 33",
        "27 -> 28,30,31",
        "3 -> 10,15",
        "4 -> 25",
        "5 -> 12,17,19,20",
        "6 -> 19,21,8",
        "7 -> 16,18,28,34",
        "8 -> 13,15,18,22,26,34",
        "9 -> 14,19,22,29,34"
    ]
    print(str(function(edges=p_1))[1:-1])
