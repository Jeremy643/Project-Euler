def is_pentagon(t, pentagon_numbers):
    if (t[0] + t[1]) in pentagon_numbers and (abs(t[0] - t[1])) in pentagon_numbers:
        return True
    else:
        return False


def main():
    limit = 3000
    pentagon_numbers = []
    for i in range(1, limit):
        p = int(i * (3 * i - 1) / 2)
        pentagon_numbers.append(p)

    interest_numbers = []
    for p in pentagon_numbers[:-1]:
        p_index = pentagon_numbers.index(p)
        for prev_p in pentagon_numbers[:p_index]:
            if prev_p >= (pentagon_numbers[p_index] - p) and (p + prev_p) in pentagon_numbers and (abs(p - prev_p)) \
                    in pentagon_numbers:
                interest_numbers.append((p, prev_p))
    k, j = interest_numbers[0]
    diff = abs(k - j)
    print('Answer: {}'.format(diff))


if __name__ == '__main__':
    main()
