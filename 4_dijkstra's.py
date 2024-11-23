import heapq
import collections

def networkDelayTime():
    N = int(input("Enter the number of nodes (N): "))
    M = int(input("Enter the number of edges (M): "))
    print("Enter the edges (ul, vl, wl) for each edge:")
    times = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        times.append((u, v, w))

    K = int(input("Enter the starting node (K): "))

    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    pq = [(0, K)]  # (time, node)
    dist = {i: float('inf') for i in range(1, N + 1)}

    dist[K] = 0

    while pq:
        curr_time, node = heapq.heappop(pq)
        if curr_time > dist[node]:
            continue

        for neighbor, time in graph[node]:
            new_time = curr_time + time
            if new_time < dist[neighbor]:
                dist[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))

    max_time = max(dist.values())
    if max_time == float('inf'):
        print(-1)
    else:
        print(max_time)

networkDelayTime()
