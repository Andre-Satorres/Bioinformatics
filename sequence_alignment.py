GAP = -5
MATCH = 2
MISMATCH = -2

def sigma(x, y):
    if x == y:
        return MATCH
    return MISMATCH

# Using dumb brute force, finds the cost of optinal alignment
def align(a: list, b: list) -> int:
    if a == []:
        return GAP * len(b)
    
    if b == []:
        return GAP * len(a)
    
    x1 = align(a[:-1], b[:-1]) + sigma(a[-1], b[-1])
    x2 = align(a[:-1], b) + GAP
    x3 = align(a, b[:-1]) + GAP
    return max(x1, x2, x3)

a = ['T', 'C', 'G', 'A', 'A', 'A', 'G', 'C']
b = ['T', 'A', 'C', 'G', 'C']

# now, using Dynamic Programming
def align2(a, b):
    M = [[float('-inf') for _ in range(len(b))] for _ in range(len(a))]
    
    for i in range(len(a)):
        M[i][0] = 0
    
    for j in range(len(b)):
        M[0][j] = 0

    for i in range(len(a)):
        for j in range(len(b)):
            x1 = M[i][j-1] + GAP
            x2 = M[i-1][j-1] + sigma(a[i], b[j])
            x3 = M[i-1][j] + GAP
            M[i][j] = max(x1, x2, x3)
    
    return M


# given above matrix, generate the alignment
def align22(a, b):
    M = align2(a, b)
    last = M[len(a)-1][len(b)-1]
    
    x1 = M[len(a)-2][len(b)-1]
    x2 = M[len(a)-1][len(b)-2]
    x3 = M[len(a)-2][len(b)-2]

    if 