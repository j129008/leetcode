
record = dict()
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n-1 not in record:
        record[n-1] = climbStairs(n-1)
    if n-2 not in record:
        record[n-2] = climbStairs(n-2)

    return record[n-1] + record[n-2]

print(climbStairs(35))
