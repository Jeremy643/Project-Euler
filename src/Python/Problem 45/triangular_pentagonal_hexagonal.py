import time


def main():
    tn = 286
    triangle = []
    pentagonal = []
    hexagonal = []
    for i in range(1, tn+1):
        triangle.append(i * (i + 1) / 2)
        pentagonal.append(i * (3 * i - 1) / 2)
        hexagonal.append(i * (2 * i - 1))
    start = time.time()
    while True:
        if triangle[-1] in pentagonal and triangle[-1] in hexagonal:
            print('Answer: {}'.format(int(triangle[-1])))
            break
        else:
            tn += 1
            triangle.append(tn * (tn + 1) / 2)
            pentagonal.append(tn * (3 * tn - 1) / 2)
            hexagonal.append(tn * (2 * tn - 1))
    print('Time taken = {}s'.format(time.time()-start))


if __name__ == '__main__':
    main()
