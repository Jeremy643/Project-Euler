import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


def main():
    dim = 20
    routes = ncr(dim*2, dim)
    print('The number of routes in a {}x{} grid is: {}'.format(dim, dim, routes))


if __name__ == '__main__':
    main()
