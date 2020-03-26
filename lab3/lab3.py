visited = []
start = 0
path_1 = []
temp_path = []

# G = [[0, 1, 1, 1, 0],
#      [1, 0, 1, 0, 0],
#      [1, 1, 0, 0, 1],
#      [1, 0, 0, 0, 0],
#      [0, 0, 1, 0, 0],]

# G = [[0, 1, 1, 1],
#      [1, 0, 1, 1],
#      [1, 1, 0, 0],
#      [1, 1, 0, 0],]

# G = [[0, 1, 0, 0, 0],
#      [1, 0, 0, 1, 0],
#      [1, 0, 0, 0, 1],
#      [1, 0, 0, 0, 0],
#      [0, 0, 1, 0, 0]]

G = [[0, 1, 0, 0],
     [1, 0, 0, 1],
     [1, 0, 0, 0],
     [1, 0, 0, 0]]

# G = [[0,1,0],
#      [0,0,1],
#      [1,0,0]]

# G = [[0, 1, 0, 0, 0, 0],
#      [1, 0, 0, 1, 0, 0],
#      [1, 0, 0, 0, 1, 0],
#      [1, 0, 0, 0, 0, 0],
#      [0, 0, 1, 0, 0, 1],
#      [0, 0, 0, 0, 1, 0]]

# G = [[0, 1, 1, 0, 1, 1],
#      [1, 0, 1, 1, 0, 0],
#      [1, 1, 0, 0, 1, 0],
#      [0, 1, 0, 0, 0, 1],
#      [1, 0, 1, 0, 0, 1],
tops = []
Gt = [[G[j][i] for j in range(len(G))] for i in range(len(G[0]))] 
n = len(G)
for i in range(n):
    tops.append(i)
# for i in range(n):
#     print(Gt[i])
comp = []
strong = []
adj = []
rev = True
test_visited = []
count = 0

def dfs_mini(g, visited, start):
    global adj,end_path # adj = [] # TODO тримати всі суміжні вершини і видаляти пройдені ??
    # print("----- DFS -----")
    temp = []
    visited.append(start)
    # print("------ top ", start)
    # print("visited = ", visited)
    for k in range(n):
        # print(end_path)
        if (g[start][k] == 1) and (k not in end_path):
            temp.append(k)
            # print(k)
    # print("temp = ", temp)
    # print("adj = ", adj)
    for k in range(len(temp)):
        adj.insert(k, temp[k])
    path_1.append(start)
    # print("visited dfs = ", visited)
    # print("adj = ", adj)
    # print("p1 = ", path_1)
    # adj = list(set(adj))
    # print("adj = ", adj)
    # print("v0 = ", visited[0])
    # if visited[0] in adj:
    #     print("strong")
    #     strong.append(path_1)
    if(len(adj) > 0):
        for k in range(len(adj)):
            if adj[k] not in visited:
                next = adj[k]
                # print("adj k = ", adj[k])
                dfs_mini(g, visited, next)
    path_1.clear()

def dfs_test(g, visited, start):
    global adj # adj = [] # TODO тримати всі суміжні вершини і видаляти пройдені ??
    # print("----- DFS -----")
    temp = []
    visited.append(start)
    i = 0
    while i < len(adj):
        if adj[i] in visited:
            del adj[i]
            i -= 1
        i += 1 
    # print("------ top ", start)
    # print("visited = ", visited)
    for k in range(n):
        # print(g[start][k])
        if (g[start][k] == 1) and (k not in visited):
            temp.append(k)
    # print("temp = ", temp)
    # print("adj = ", adj)
    for k in range(len(temp)):
        adj.insert(k, temp[k])
    adj = list(set(adj))
    # print("visited = ", visited)
    # print("adj = ", adj)
    # print("v0 = ", visited[0])
    # if visited[0] in adj:
    #     print("strong")
    #     strong.append(path_1)
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
    #     print(visited)
    #     print("fuck")
    #     return None


def dfs(g, visited, start):
    global adj, rev, test_visited, count # adj = [] # TODO тримати всі суміжні вершини і видаляти пройдені ??
    # print("----- DFS -----")
    temp = []
    before = []
    visited.append(start)
    test_visited.append(start)
    i = 0
    count += 1
    if count > len(g):
        print("END COUNT")
        return 0
    while i < len(adj):
        if adj[i] in visited:
            del adj[i]
            i -= 1
        i += 1 
    # print("------ top ", start)
    print("visited = ", visited)
    for k in range(n):
        if (g[start][k] == 1) and (k not in visited):
            temp.append(k)
    # print("temp = ", temp)
    # print("adj = ", adj)
    for k in range(len(temp)):
        adj.insert(k, temp[k])
    adj = list(set(adj))
    print("adj = ", adj)
    # print("visited = ", visited)
    # print("adj = ", adj)
    # print("v0 = ", visited[0])
    # if visited[0] in adj:
    #     print("strong")
    #     strong.append(path_1)
    if(len(adj) == 0):
        print("ZERO")
        print("VISITED = ", visited)
        # # #
        # rev = True
        before = visited
        print("FECU BFORE = ", before)
        test = [x for x in tops if x not in visited]
        print(test)
        dfs1(G, test_visited[:], test_visited[-1])
        visited = before
        if len(visited) == len(g):
            return 0
        print("BEFORE = ", test_visited)
        # # #
        # visited.clear()
        test_visited.clear()
        print("TEST = ", test)
        next = test[0]
        dfs(g, visited, next)
        return 0
    else:
        # for k in range(len(adj[:])):    
        next = adj[0]
        print("RETURN")
        print("VISITED = ", visited)
        dfs(g, visited, next)
        return 0
    #     print(visited)
    #     print("fuck")
    #     return None


def dfs1(g, path, start):
    print(path)
    print(start)
    if path.index(start) == 0:
        print("---END--_")
        return 0
    print("----- DFS1 -----")
    print("start = ", start)
    global adj, count, visited, g_path, rev
    print("path = ", path)
    print("visited = ", visited)
    # count += 1
    temp_path = []
    # if count > len(g):
    #     print("END COUNT")
    #     return 0
    print(path[0])
    print(start)
    # print("g = ", g[start][path[0]])
    # if rev is False:
    #     elem = g[path[0]][start]
    # else:
    #     elem = g[start][path[0]]
    elem = G[path[0]][start]
    print("g = ", elem)
    print(G[path[0]][start], Gt[start][path[0]])
    if G[path[0]][start] == 1 or Gt[start][path[0]] == 1:
        for i in range(path.index(start)+1):
            temp_path.append(path[i])
        print("Comp += ", temp_path)
        strong.append(temp_path[:])
        print("strong = ", strong)
        for k in range(path.index(start)+1):
            del path[0]
        visited = [x for x in visited if x not in path]
        print("visited = ", visited)
        print("path = ", path)
        # if len(path) <= 1:
        #     # TODO return
        #     start = visited[-1]
        #     dfs1(G, visited, start)
        #     return 0
        # else:
        if len(path) <= 1:
            return 0
        start = path[-1]
        dfs1(G, path, start)
        return 0
    else:
        print(path)
        if len(path) <= 1:
            return 0
            # visited = visited[visited.index(start) - 1]
            # dfs1(Gt, visited, start)
            # return 0
        else:
            print("HERE!!!")
            start = path[path.index(start)-1]
            dfs1(G, path, start)
            return 0
    

    # sc = []
    # temp = []
    # # visited0 = visited
    # print(visited)
    # print("------ top ", start)
    # print("path = ", path)
    # for k in range(n):
    #     if g[start][k] == 1:
    #         temp.append(k)
    # print("temp = ", temp)
    # print(path)
    # if path[0] in temp:
    #     path0 = list(set(visited) - set(path))
    #     print("path0 = ", path0)
    #     print("visited = ", visited)
    #     for k in range(path.index(start)+1):
    #         sc.append(path[0])
    #         del path[0]
    #         print(path)
    #     strong.append(sc)
    #     print("strong = ", strong)
    #     # print(path[path.index(start) - 1])
    #     print(start)
    #     # path = visited0
    #     # if(len(path)>0):
    #     # start = path[-1]
    #     # visited.remove(start)
    #     # visited = visited0
    #     if count >= len(G) or len(visited) == 0:
    #         return 0
    #     else:
    #         start = visited[-1]
    #         dfs1(Gt, visited, start)
    # else:
    #     start = path[path.index(start) - 1]
    #     print("index = ", path.index(start))
    #     if path.index(start) <= 1:
    #         print("END")
    #         return 0
    #     else:
    #         dfs1(Gt, path, start)


        # visited.remove(start)
    # for k in range(len(temp)):
    #     adj.insert(k, temp[k])
    # print("adj = ", adj)
    # if t0 in temp and len(visited) > 1:
    #     strong.append(visited[:])
    #     print("fuck")
    #     print("strong = ", strong)
    # if len(adj) > 0:
    #     for k in range(len(adj)):
    #         if adj[k] not in visited:
    #             next = adj[k]
    #             dfs1(g, visited, next)

# for i in range(len(G)):
#     visited.clear()
#     adj.clear()
#     print(" ---------- New start top : ", i, " ---------- ")
#     dfs(G, visited, i)
#     global_path = visited
#     print("Path = ", visited)
print("\n"*2)
ref = False
if G == Gt:
    visited.clear()
    dfs(G, visited, start)
    print("Strong component : ", visited)
else:
    strong1 = []
    strong2 = []
    while True:
        strong = strong1
        end_path = []
        visited = []
        s = 3
        dfs_test(G, visited, s)
        # print("VISITED = ", visited)
        while len(visited) > 0:
            s = visited[-1]
            temp_vis_1 = []
            adj.clear()
            dfs_mini(Gt, temp_vis_1, s)
            # print("TEMP = ", temp_vis_1)
            strong.append(temp_vis_1)
            for k in range(len(temp_vis_1)):
                end_path.append(temp_vis_1[k])
            visited = [x for x in visited if x not in temp_vis_1]
            # print("VISITED = ", visited)


        strong = strong2
        end_path = []
        visited = []
        adj.clear()
        dfs_test(G, visited, s)
        # print("VISITED = ", visited)
        while len(visited) > 0:
            s = visited[-1]
            temp_vis_1 = []
            adj.clear()
            dfs_mini(Gt, temp_vis_1, s)
            # print("TEMP = ", temp_vis_1)
            strong.append(temp_vis_1)
            for k in range(len(temp_vis_1)):
                end_path.append(temp_vis_1[k])
            visited = [x for x in visited if x not in temp_vis_1]
            # print("VISITED = ", visited)
        print("Strong components = ", strong2)
        break
    # dfs_test(G, visited, s)
    # print("VISITED1 = ", visited)
    # v0 = visited[-1]
    # path = visited
    # visited.clear()
    # adj.clear()
    # dfs_test(G, visited, v0)
    # print("VISITED2 = ", visited)
    # visited.reverse()
    # if path == visited:
    #     print("REVERSED")
    #     rev = True
    # else:
    #     print("NOT REVERSED")
    #     rev = False

    # visited.clear()
    # adj.clear()
    # dfs(G, visited, s)
    # print(visited)
    # path = []
    # adj = []
    # v0 = visited[0]
    # print(v0)
    # visited = []
    # # dfs_test(Gt, visited, v0)
    # print(visited)
    # # dfs_test(Gt, path, visited[0])
    # # comp.append(path)
    # print("VVisited = ", path)
    # # g_path = path
    # # visited1 = path
    # # count = 0
    # # temporary_path = path
    # # dfs1(G, path, path[-1])
    # # print("Path = ", path)
    # # visited1 = [x for x in visited if x not in path]
    # # print(visited1)

    # print("- All components -")
    # for i in range(len(comp)):
    #     print(comp[i])
