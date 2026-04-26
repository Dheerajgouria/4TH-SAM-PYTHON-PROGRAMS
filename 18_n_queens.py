def n_queens(n):
    def solve(board, row):
        if row == n: print(board); return
        for col in range(n):
            if col not in cols and (row-col) not in d1 and (row+col) not in d2:
                cols.add(col); d1.add(row-col); d2.add(row+col)
                solve(board+[col], row+1)
                cols.discard(col); d1.discard(row-col); d2.discard(row+col)
    cols, d1, d2 = set(), set(), set()
    solve([], 0)

n_queens(4)
