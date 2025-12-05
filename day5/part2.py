import sys

def solve():
    ans = 0
    ranges = []
    for line in sys.stdin:
        if not line.strip():
            break
        ranges.append(tuple([int(x) for x in line.strip().split('-')]))
    
    ranges = sorted(ranges)
    merged = [list(ranges[0]), ]
    
    for i in range(1, len(ranges)):
        this_range = ranges[i]
        if this_range[0] > merged[-1][1]:
            merged.append(list(this_range))
        else:
            merged[-1][1] = max(this_range[1], merged[-1][1])
    
    for start, end in merged:
        ans += end - start + 1
    
    print(ans)
    


def main():
    solve()


if __name__ == "__main__":
    main()