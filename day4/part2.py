import sys

def solve():
    ans = 0
    grid = []
    for line in sys.stdin:
        grid.append(list(line.strip()))

    m = len(grid)
    n = len(grid[0])
    dirs = [(1,0), (1, -1), (1, 1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
    updated = True
    while updated:
        updated = False
        to_update = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '@': continue
                cnt = 0
                for dx, dy in dirs:
                    nx = i + dx
                    ny = j + dy
                    if not valid(nx, ny, m, n):
                        continue
                    if grid[nx][ny] == '@':
                        cnt += 1
                if cnt < 4:
                    to_update.add((i, j))
                    updated = True
                    ans += 1
        update(grid, to_update)
    print(ans)

def update(grid, to_update):
    for i, j in to_update:
        grid[i][j] = '.'

def valid(i, j, m, n):
    if i < 0 or j < 0 or i >= m or j >= n:
        return False
    return True

def main():
    solve()


if __name__ == "__main__":
    main()