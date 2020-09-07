def main():
    limit = 1000
    fib_seq = [1, 1]
    while True:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        if len(str(fib_seq[-1])) == limit:
            break
    print('The index of the first {} digit number in the Fibonacci Sequence is: {}'.format(limit, len(fib_seq)))


if __name__ == '__main__':
    main()
