def solution(ineq, eq, n, m):
    if n == m:
        return int(eq == "=")
    return int(n > m if ineq == ">" else n < m)