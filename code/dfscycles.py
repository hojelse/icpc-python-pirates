import sys
sys.setrecursionlimit(10**6)
def is_cyclic(g):

    def dfs(v, path, seen):
        if v in seen: 
            return False

        seen.add(v)
        for u,w in g[v].items():
            # if we took u -> v then discard v -> u : undirected edge
            if len(path) > 1 and u == path[-2]: 
                continue
            if u in path: 
                return True 

            path.append(u)
            if dfs(u, path, seen): 
                return True
            path.pop()

        return False
    
    seen = set()
    return any([dfs(v, [v], seen) for v in g])