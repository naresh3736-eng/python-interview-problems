'''
Given a dictionary representing a grpah, find all paths between given start and end nodes
'''

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def findAllPaths(grpah, start, end, path= []):
    path = path + [start]

    if start == end:
        return [path]

    if not graph.get(start):
        return None

    paths = []

    for node in graph[start]:
        if node not in path:
            newpaths = findAllPaths(grpah, node, end, path)

            for newpath in newpaths:
                paths.append(newpath)

    return paths


print(findAllPaths(graph, 'A', 'D'))