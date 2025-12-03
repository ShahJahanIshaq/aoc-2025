import sys

def solve():
    ans = 0
    for line in sys.stdin:
        nums = [int(x) for x in list(line.strip())]
        digit1 = digit2 = None
        idx1 = idx2 = None
        for i in range(len(nums) - 1):
            if not digit1 or nums[i] > digit1:
                digit1 = nums[i]
                idx1 = i
        for i in range(idx1 + 1, len(nums)):
            if not digit2 or nums[i] > digit2:
                digit2 = nums[i]
                idx2 = i
        ans += digit1 * 10 + digit2
    print(ans)

def main():
    solve()


if __name__ == "__main__":
    main()