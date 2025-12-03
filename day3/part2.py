import sys

def solve():
    ans = 0
    for line in sys.stdin:
        nums = [int(x) for x in list(line.strip())]
        n = len(nums)
        NEED = 12
        digits = []
        start = 0
        for leave_out in range(NEED - 1, -1, -1):
            mx, mxidx = find_max(nums, start, n - leave_out - 1)
            digits.append(mx)
            start = mxidx + 1
        joltage = 0
        for digit in digits:
            joltage = joltage * 10 + digit
        ans += joltage

    print(ans)

def find_max(nums, i, j):
    mx = -1
    mxidx = -1
    for idx in range(i, j + 1):
        if mx == -1 or nums[idx] > mx:
            mx = nums[idx]
            mxidx = idx
    return mx, mxidx

def main():
    solve()


if __name__ == "__main__":
    main()