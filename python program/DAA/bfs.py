from collections import deque

class Solution:
    def bfs(self, adj):
        total_len = len(adj)      
        src = 0                  
        
        visited = [False] * total_len
        queue = deque()
        result = []

        
        visited[src] = True
        queue.append(src)

        while queue:
            node = queue.popleft()
            result.append(node)

            
            for i in adj[node]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)

        return result
# Example usage:
if __name__ == "__main__":
    adj = [
        [1, 2],
        [0, 3, 4],
        [0, 4],
        [1],
        [1, 2]
    ]
    solution = Solution()
    print("BFS Traversal:", solution.bfs(adj))

