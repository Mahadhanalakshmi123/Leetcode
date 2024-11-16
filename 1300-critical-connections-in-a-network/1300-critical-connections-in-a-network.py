class Solution(object):
    def criticalConnections(self, n, connections):
        graph = {i: [] for i in range(n)}
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        disc = [-1] * n
        low = [-1] * n
        parent = [-1] * n
        result = []
        time = [0]
        
        def dfs(u):
            disc[u] = low[u] = time[0]
            time[0] += 1
            
            for v in graph[u]:
                if disc[v] == -1:
                    parent[v] = u
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        result.append([u, v])
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
        
        for i in range(n):
            if disc[i] == -1:
                dfs(i)
        
        return result
