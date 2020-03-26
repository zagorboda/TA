visited = []
path_1 = []

G = [[0, 1, 0, 0, 0],
     [1, 0, 0, 1, 0],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 0],
     [0, 0, 1, 0, 0]]

# G = [[0, 1, 1, 0, 0, 0, 0],
#      [1, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0],
#      [1, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 1, 1],
#      [0, 0, 0, 0, 1, 0, 1],
#      [0, 0, 0, 0, 1, 1, 0]]

tops = []
Gt = [[G[j][i] for j in range(len(G))] for i in range(len(G[0]))] 
n = len(G)
for i in range(n):
    tops.append(i)

def dfs_mini(g, visited, start):
    global adj, end_path
    temp = []
    visited.append(start)
    for k in range(n):
        if (g[start][k] == 1) and (k not in end_path):
            temp.append(k)
    for k in range(len(temp)):
        adj.insert(k, temp[k])
    path_1.append(start)
    if(len(adj) > 0):
        for k in range(len(adj)):
            if adj[k] not in visited:
                next = adj[k]
                dfs_mini(g, visited, next)
    path_1.clear()

def dfs_test(g, visited, start):
    global adj
    temp = []
    visited.append(start)
    i = 0
    while i < len(adj):
        if adj[i] in visited:
            del adj[i]
            i -= 1
        i += 1 
    for k in range(n):
        if (g[start][k] == 1) and (k not in visited):
            temp.append(k)
    for k in range(len(temp)):
        adj.insert(k, temp[k])
    adj = list(set(adj))
    if len(visited) == len(g):
        return 0
    if(len(adj) == 0):
        test = [x for x in tops if x not in visited]
        next = test[0]
        dfs_test(g, visited, next)
        return 0
    else:
        for k in range(len(adj[:])):    
            next = adj[k]
            dfs_test(g, visited, next)
            return 0

start = 3
while True:
    s = start
    strong1 = []
    strong2 = []
    strong = strong1
    end_path = []
    visited = []
    adj = []
    dfs_test(G, visited, s)
    while len(visited) > 0:
        s = visited[-1]
        temp_vis_1 = []
        adj.clear()
        dfs_mini(Gt, temp_vis_1, s)
        strong.append(temp_vis_1)
        for k in range(len(temp_vis_1)):
            end_path.append(temp_vis_1[k])
        visited = [x for x in visited if x not in temp_vis_1]
    for i in range(len(strong1)):
        strong1[i] = sorted(strong1[i])
    strong1 = sorted(strong1)

    strong = strong2
    end_path = []
    visited = []
    adj = []
    dfs_test(Gt, visited, s)
    while len(visited) > 0:
        s = visited[-1]
        temp_vis_1 = []
        adj.clear()
        dfs_mini(Gt, temp_vis_1, s)
        strong.append(temp_vis_1)
        for k in range(len(temp_vis_1)):
            end_path.append(temp_vis_1[k])
        visited = [x for x in visited if x not in temp_vis_1]
    for i in range(len(strong2)):
        strong2[i] = sorted(strong2[i])
    strong2 = sorted(strong2)
    if strong1 == strong2:
        break
    else:
        start += 1
        if start >= len(G):
            start = 0
print("SCC is ", strong2)