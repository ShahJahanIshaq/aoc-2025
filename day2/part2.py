import sys

def solve():
    ans = 0
    line = sys.stdin.readline().strip()
    rstr = line.split(',')
    ranges = []
    for rng in rstr:
        ranges.append(tuple([int(x) for x in rng.split('-')]))


    MAX_LENGTH = 12
    done = set()
    # for each repeat size
    for repeat_size in range(1, 7):
        # generate all possible permutations of size repeat_size
        perm_set = set()
        curr = ""
        permute(perm_set, repeat_size, curr)
        # for each permutation
        for perm in perm_set:
            # generate its copy-repeated variants uptil MAX_LENGTH
            max_copies = MAX_LENGTH // repeat_size
            for num_copies in range(2, max_copies + 1):
                copy_variant = perm * num_copies
                # check if copy_variant belongs to any interval
                if belongs(ranges, int(copy_variant)) and int(copy_variant) not in done:
                    ans += int(copy_variant)
                    done.add(int(copy_variant))

    print(ans)

# dfs - O(10^size)
def permute(perm_set, size, curr):
    if len(curr) >= size:
        perm_set.add(curr)
        return
    for digit in range(0, 10):
        if digit == 0 and curr == "":
            continue
        curr += str(digit)
        permute(perm_set, size, curr)
        curr = curr[:-1]

# O(|ranges|), can be optimized to O(log_2 |ranges|) using binary search
def belongs(ranges, num):
    for start, end in ranges:
        if start <= num <= end:
            return True
    return False

def main():
    solve()


if __name__ == "__main__":
    main()