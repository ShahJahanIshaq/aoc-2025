import sys

def solve():
    ans = 0
    grid = []
    for line in sys.stdin:
        grid.append(list(line.rstrip('\n')))
    m = len(grid)
    line_length = len(grid[0])
    separator_cols = []
    for j in range(line_length):
        is_separator = True
        for i in range(m):
            if grid[i][j] != ' ':
                is_separator = False
                break
        if is_separator:
            separator_cols.append(j)
    separator_cols.append(line_length)
    
    start = 0
    k = 0
    while start < line_length:
        end = separator_cols[k] - 1
        operator = grid[m - 1][start]
        sub_ans = 1 if operator == '*' else 0
        for col in range(start, end + 1):
            operand = 0
            for row in range(m - 1):
                if grid[row][col] == ' ':
                    continue
                operand = operand * 10 + int(grid[row][col])
            sub_ans = operate(sub_ans, operand, operator)
        ans += sub_ans
        start = separator_cols[k] + 1
        k += 1
    print(ans)

def operate(opA, opB, op):
    if op == '+':
        return opA + opB
    elif op == '*':
        return opA * opB

def main():
    solve()


if __name__ == "__main__":
    main()