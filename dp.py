MOD = 10**9 + 7

def count_ways(m, g_nodes, g_from, g_to):
    # Create a graph adjacency list
    graph = {}
    for i in range(len(g_from)):
        if g_from[i] not in graph:
            graph[g_from[i]] = set()
        if g_to[i] not in graph:
            graph[g_to[i]] = set()
        graph[g_from[i]].add(g_to[i])
        graph[g_to[i]].add(g_from[i])

    # Initialize a 2D array dp
    dp = [[0] * m for _ in range(g_nodes)]
    
    # Initialize the first city with all types of monuments
    for i in range(m):
        dp[0][i] = 1
    
    # Iterate over each city
    for i in range(1, g_nodes):
        # Iterate over each type of monument for the current city
        for j in range(m):
            # Initialize the count of ways to build monuments
            dp[i][j] = 0
            
            # Iterate over the types of monuments for the previous city
            for l in range(m):
                if j != l:  # Ensure different types of monuments for adjacent cities
                    dp[i][j] = (dp[i][j] + dp[i-1][l]) % MOD
            
            # Consider the case where the city is not connected to any other city
            if i+1 not in graph:
                dp[i][j] = (dp[i][j] * (m-1)) % MOD
    
    # Sum up the count of ways to build monuments in the last city
    total_ways = sum(dp[-1]) % MOD
    
    return total_ways

# Example usage
m = 4
g_nodes = 3
g_from = [1, 1]
g_to = [2, 3]
print(count_ways(m, g_nodes, g_from, g_to))  # Output: 6
