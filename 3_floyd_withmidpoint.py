N = int(input("Enter number of offices: "))

cost_matrix = []
INF = float('inf')

print("Enter cost matrix (inf for infinity): ")
for i in range(N):
    row = input().split()
    cost_row = []
    for j in range(N):
        if row[j].lower() == 'inf':
            cost_row.append(INF)
        else:
            cost_row.append(int(row[j]))

    cost_matrix.append(cost_row)

for k in range(N):
    print(f"{k} as midpoint: ")
    for i in range(N):
        for j in range(N):
            if cost_matrix[i][k] + cost_matrix[k][j] < cost_matrix[i][j]:
                cost_matrix[i][j] = cost_matrix[i][k] + cost_matrix[k][j]

    for row in cost_matrix:
        print(*row)

print("Final minimum cost matrix:")
for row in cost_matrix:
    print(*row)
