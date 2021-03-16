'''
Given a dictionary representing a grpah, find the shortest path between given start and end nodes
'''

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def findShortestPath(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    if not graph.get(start):
        return None

    shortest = None

    for node in graph[start]:
        if node not in path:
            newpath = findShortestPath(graph, node, end, path)

            if not shortest or len(newpath) < len(shortest):
                shortest = newpath

    return shortest

print(findShortestPath(graph, 'A', 'D'))