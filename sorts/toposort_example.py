from toposort import toposort, toposort_flatten

graph1 = {2: {11}, 9: {11, 8, 10}, 10: {11, 3}, 11: {7, 5}, 8: {7, 3}}
graph2 = {2: [11], 9: [11, 8, 10], 10: [11, 3], 11: [7, 5], 8: [7, 3]}

print(list(toposort_flatten(graph1)))

print(type(graph1))



