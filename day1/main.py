import sys

def solve():
    curr = 50
    ans = 0
    for line in sys.stdin:
        dir = line[0]
        shift = int(line[1:])

        if dir == 'L':
            if curr == 0:
                ans += shift // 100
            else:
                ans += 0 if shift < curr else (shift - curr) // 100 + 1
            curr = (curr - shift) % 100
        else:
            ans += (curr + shift) // 100
            curr = (curr + shift) % 100
    print(ans)


def main():
    solve()


if __name__ == "__main__":
    main()