# Graph of the dependencies between rules.
# For example,
# 2: 1 3 | 3 1 creates the entry
# 2 => [[1,3], [3, 1]]
graph = {}
# Map of the rule to the possible valid messages of that rule.
valid_msgs = {}
seen = set()

lines = []
with open("day19.txt", "r") as f:
    lines = f.readlines()

'''
The solution here is to first create a graph of dependencies
between the rules and then DFS it to get all of the possible
valid messages.
'''
for l in lines:
    if not (":" in l):
        break

    rule = int(l.split()[0][:-1])

    # If the rule contains a quotation mark then
    # it's a leaf in the graph, i.e. a single character.
    if("\"" in l):
        graph[rule] = []
        valid_msgs[rule] = [l.split()[1][1:-1]]
    # If the rule is dependent on other rules then create
    # a vertex which builds upon the neighbors, taking into
    # account pipes.
    else:
        graph[rule] = [[]]
        for c in l.split()[1:]:
            if c == '|':
                graph[rule].append([])
            else:
                graph[rule][-1].append(int(c))

print(graph)

'''
Given string_chunks [[s1, s2, ...], [t1, t2 ...], [u1, u2...] ...]

find all strings si + tj + uk + ....
'''
def find_all_strings(string_chunks):
    if string_chunks == []:
        return [""]

    output = []

    suffixes = find_all_strings(string_chunks[1:])
    for suffix in suffixes:
        for prefix in string_chunks[0]:
            output.append(prefix + suffix)

    return output

# Get all of the valid messages by DFSing down the graph from rule 0.
def dfs(root):
    global graph
    global seen
    global valid_msgs

    # If we've hit a leaf then return the single character.
    if(graph[root] == [] or (root in seen)):
        return valid_msgs[root]

    seen.add(root)

    # Go through each section of the pipe and get the valid
    # strings, and then permute them.
    valid_msgs[root] = []
    for section in graph[root]:
        # Get all possible valid strings for neighbors in the form
        # [dfs(nbr_1) ... dfs(nbr_n)] where the dfs call returns
        # the array of strings and find all permutations of
        # the strings in each dfs array combined.
        string_chunks = [dfs(nbr) for nbr in section]
        valid_msgs[root].extend(find_all_strings(string_chunks))


    return valid_msgs[root]

dfs(0)

# print(valid_msgs)
valid = set(valid_msgs[0])

print(valid_msgs[8])
print(valid_msgs[11])

'''
ct = 0
for l in lines:
    if not (":" in l):
        if l.strip() in valid:
            ct += 1
print(ct)
'''
