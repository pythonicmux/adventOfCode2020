lines = []

with open("./day7.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

graph = {}

for line in lines:
    node_string, neighbors_string = line.split('contain')[0], line.split('contain')[1]
    # Get the node.
    node = ""
    for word in node_string.split():
        if(word.startswith('bag')):
            break
        node += word

    if(node not in graph):
        graph[node] = []

    # Get the neighbors of the node.
    found_neighbor = False
    neighbor = ""
    num = -1
    for word in neighbors_string.split():
        if word.startswith('bag'):
            found_neighbor = False
            if neighbor != "":
                graph[node].append((neighbor, num))
            neighbor = ""
            num = -1
        elif word.isdigit():
            found_neighbor = True
            num = int(word)
        elif found_neighbor:
            neighbor += word

print(graph)

seen = {}

def dfs(root):
    global seen

    ct = 0

    for nbr, num in graph[root]:
        if nbr not in seen:
            ct += num * (1 + dfs(nbr))
        else:
            ct += num * (1 + seen[nbr])

    seen[root] = ct
    return ct


print(dfs('shinygold'))
