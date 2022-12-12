def iterative_deepening_dfs(graph, start, target):
    depth = 1
    bottom_reached = False

    while not bottom_reached:
        result, bottom_reached = iterative_deepening_dfs_rec(graph, start, target, 0, depth)

        if result is not None:
            return result

        depth *= 2
        print("Increasing depth to " + str(depth))

    return None

def iterative_deepening_dfs_rec(graph, node, target, current_depth, max_depth):
    print("Visiting Node " + str(node))
    
    if node == target:
        print("Found the node we're looking for!")
        return node, True

    if current_depth == max_depth:
        print("Current maximum depth reached, returning...")

        if len(graph[node]) > 0:
            return None, False
        else:
            return None, True

    bottom_reached = True

    for i in range(len(graph[node])):
        result, bottom_reached_rec = iterative_deepening_dfs_rec(graph, graph[node][i], target, current_depth + 1, max_depth)

        if result is not None:
            return result, True

        bottom_reached = bottom_reached and bottom_reached_rec
        
    return None, bottom_reached

graph1 = {
5 : [3, 7],
3 : [2, 4],
7 : [8],
2 : [],
4 : [8],
8 : []
}
iterative_deepening_dfs(graph1,5,8)