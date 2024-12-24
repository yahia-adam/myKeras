def myMatrix_multiply(a, b):
    """Multiply two matrices."""
    
    m = len(a)
    n = len(a[0])
    n2 = len(b)
    p = len(b[0])

    if n != n2:
        print(f"n={n}n2={n2}")
        # raise ValueError("Matrices are not compatible.")
        return
    result = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]

    return result
