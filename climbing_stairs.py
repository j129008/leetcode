
record = {
    1: 1,
    2: 2
}

def climbStairs(n):
    if n in record: return record[n]
    record[n] = climbStairs(n-1) + climbStairs(n-2)

    return record[n]

print(climbStairs(35))
