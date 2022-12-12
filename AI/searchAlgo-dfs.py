def dfs(graph, closed, open, start_node, goal_node):
    path = []
    open.append(start_node)

    while open:
        extracted_node = open.pop(0)
        path.append(extracted_node)
        print(extracted_node)

        if extracted_node == goal_node:
            closed.append(extracted_node)
            return f'Goal reached with path : {path}', open, closed

        open = graph[extracted_node] + open
        closed.append(extracted_node)
        print('Current open list :' ,open)
        print('Current closed list :' ,closed)

        for neighbour_node in graph[extracted_node] :
            if neighbour_node not in graph.keys():
                return (f'The node {neighbour_node} does not exist')
                
    return "Goal node does not exist"

graph1 = {
5 : [3, 7],
3 : [2, 4],
7 : [8],
2 : [],
4 : [8],
8 : []
}
closed1 = []
open1 = []
ans = dfs(graph1, closed1, open1, 5, 8)
print(ans[0])
print('Final open list is : ',ans[1])
print('Final open list is : ',ans[2])