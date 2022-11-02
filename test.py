m = [[1,2],[2,3],[3,4]]
for i in range(len(m[0])):
    m[0][i] = m[1][i]
print(m)