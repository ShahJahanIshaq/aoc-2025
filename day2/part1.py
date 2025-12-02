import sys

def solve():
    ans = 0
    line = sys.stdin.readline().strip()
    rstr = line.split(',')
    ranges = []
    for rng in rstr:
        ranges.append(tuple([int(x) for x in rng.split('-')]))
    for start, end in ranges:
        for id in range(start, end + 1):
            idstr = str(id)
            length = len(idstr)
            for ln in range(1, length // 2 + 1):
                if idstr[:ln] == idstr[ln:]:
                    ans += int(idstr)
    
    print(ans)

def main():
    solve()


if __name__ == "__main__":
    main()