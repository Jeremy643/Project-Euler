def main():
    pw = 0
    limit = 1000000
    value = []
    d = []
    i = 1
    while len(value) <= limit:
        value.extend(list(map(lambda x: int(x), [*str(i)])))
        if len(value) >= 10 ** pw:
            d.append(value[(10**pw)-1])
            pw += 1
        i += 1
    d_product = 1
    for value in d:
        d_product *= value
    print('Answer: {}'.format(d_product))


if __name__ == '__main__':
    main()
