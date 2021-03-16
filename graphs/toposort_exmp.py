vertices = 6
adj = [[] for i in range(vertices)]
visited = [False for i in range(vertices)]
output = []

def set_edge(vertex_no, node_no):
    globals()
    adj[vertex_no].append(node_no)

def toposort(i):
    globals()
    visited[i] = True
    for each in adj[i]:
        if not visited[each]:
            toposort(each)
    output.append(i)


set_edge(5,2)
set_edge(5,0)
set_edge(4,0)
set_edge(4,1)
set_edge(2,3)
set_edge(3,1)

for item in range(vertices):

    if not visited[item]:
        toposort(item)

print(output)