def bfs(graph, closed, open, start_node, goal_node):
    path = []
    open.append(start_node)

    while open:
        extracted_node = open.pop(0)
        path.append(extracted_node)
        closed.append(extracted_node)
        print(extracted_node)

        if extracted_node == goal_node:
            return f'Goal reached with path : {path}', open, closed

        for neighbour_node in graph[extracted_node]:
            if neighbour_node not in graph.keys():
                print(f'The node {neighbour_node} does not exist')
                continue
            if neighbour_node not in closed:
                open.append(neighbour_node)
        print('Current open list :' ,open)
        print('Current closed list :' ,closed)
    return "Goal node does not exist"

graph1 = {
5 : [3, 7],
3 : [2, 9, 4],
7 : [8],
2 : [],
4 : [2],
8 : []
}
closed1 = []
open1 = []
ans = bfs(graph1, closed1, open1, 5, 8)
print(ans[0])
print('Final open list is : ',ans[1])
print('Final open list is : ',ans[2])