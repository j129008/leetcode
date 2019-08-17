def generate(n):
    pascals = [
        [1],
        [1, 1]
    ]
    for i in range(2, n):
        new_line = [1]
        for j in range(len(pascals[i-1])-1):
            new_line.append(pascals[i-1][j] + pascals[i-1][j+1])
        pascals.append(new_line+[1])

    return pascals[:n]

print(generate(5))
