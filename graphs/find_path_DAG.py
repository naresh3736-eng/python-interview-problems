'''
Given a dictionary representing a grpah, print the path for a given start and end nodes
'''

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def findPath(graph, start, end, path=[]):
    path = path + [start]
    #print path

    if start == end:
        return path

    if not graph.has_key(start):
        return None

    for node in graph[start]:
        print 'node is ' +node
        if node not in path:
            newpath = findPath(graph, node, end, path)

            if newpath:
                return newpath

    return None


print findPath(graph, 'A', 'D')
#print graph['A']