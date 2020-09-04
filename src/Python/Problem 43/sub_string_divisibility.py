from itertools import permutations


def main():
    digits = list(map(lambda x: str(x), [i for i in range(10)]))
    perm = list(map(lambda x: ''.join(x), permutations(digits)))
    sum_p = 0
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for p in perm:
        valid = True
        for i in range(1, 8):
            value = int(p[i:i+3])
            if value % divisors[i-1] == 0:
                continue
            else:
                valid = False
                break
        if valid:
            sum_p += int(p)
    print('Answer: {}'.format(sum_p))


if __name__ == '__main__':
    main()
