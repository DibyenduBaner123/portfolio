import sys

# Function to print optimal parenthesization
def print_optimal_parens(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")


def matrix_chain_order(p):
    n = len(p) - 1

    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for L in range(2, n + 1):  # chain length
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = sys.maxsize

            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]

                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s


# Example dimensions
p = [30, 35, 15, 5, 10, 20, 25]

m, s = matrix_chain_order(p)

n = len(p) - 1

print("Minimum number of multiplications:", m[1][n])

print("Optimal Parenthesization:", end=" ")
print_optimal_parens(s, 1, n)