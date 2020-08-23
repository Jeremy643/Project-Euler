from itertools import permutations


def main():
    numbers = [i for i in range(10)]
    perm = list(permutations(numbers))
    specific_perm = ''.join(map(lambda x: str(x), perm[999999]))
    print('The one millionth permutation is: {}'.format(specific_perm))


if __name__ == '__main__':
    main()
