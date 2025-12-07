import sys

def solve():
    ans = 0
    grid = []
    for line in sys.stdin:
        grid.append(line.split())
    # m rows x n cols
    m = len(grid)
    n = len(grid[0])
    ops = grid[-1]
    for col, op in enumerate(ops):
        if op == '+':
            sub_ans = 0
            for i in range(m - 1):
                sub_ans += int(grid[i][col])
        else:
            sub_ans = 1
            for i in range(m - 1):
                sub_ans *= int(grid[i][col])
        ans += sub_ans
    print(ans)


def main():
    solve()


if __name__ == "__main__":
    main()