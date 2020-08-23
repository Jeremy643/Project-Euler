import math


def find_divisors(n):
    divisors = [1]
    for i in range(2, int(math.floor(math.sqrt(n)))+1):
        if n % i == 0 and n/i != i:
            divisors.extend([i, int(n/i)])
        elif n % i == 0 and n/i == i:
            divisors.append(i)
    return divisors


def main():
    limit = 28123
    i = 3
    total_sum = 3
    divisor_sums = {}
    while i <= limit:
        abundant_sum = False
        for j in range(2, math.floor(i/2)+1):
            diff = i - j
            if j not in divisor_sums:
                divisor_sums[j] = sum(find_divisors(j))
            if diff not in divisor_sums:
                divisor_sums[diff] = sum(find_divisors(diff))
            if divisor_sums[j] > j and divisor_sums[diff] > diff:
                abundant_sum = True
                break
        if not abundant_sum:
            total_sum += i
        i += 1
    print('The total sum of all integers that cannot be formed through the sum of two abundant numbers is: {}'
          .format(total_sum))


if __name__ == '__main__':
    main()
