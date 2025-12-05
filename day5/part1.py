import sys

def solve():
    ans = 0
    section = True
    ranges = []
    for line in sys.stdin:
        if not line.strip():
            section = False
            break
        if section:
            ranges.append(tuple([int(x) for x in line.strip().split('-')]))
    
    for line in sys.stdin:
        id = int(line.strip())
        for start, end in ranges:
            if start <= id <= end:
                ans += 1
                break
    
    print(ans)
    


def main():
    solve()


if __name__ == "__main__":
    main()