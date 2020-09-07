def find_gcd(n, d):
    for divider in reversed(range(1, n+1)):
        if n % divider == 0 and d % divider == 0:
            return divider


def main():
    lower = 10
    upper = 99
    curious_fractions = []
    for n in range(lower, upper+1):
        d = n + 1
        while d <= upper:
            if n % 10 == 0 or d % 10 == 0:
                d += 1
            else:
                for digit in str(n):
                    if digit in str(d):
                        dec_before = n / d
                        dec_after = int(str(n).replace(digit, '', 1)) / int(str(d).replace(digit, '', 1))
                        if dec_before == dec_after:
                            curious_fractions.append((n, d))
                            break
                d += 1

    numerator = 1
    denominator = 1
    for fraction in curious_fractions:
        numerator *= fraction[0]
        denominator *= fraction[1]
    gcd = find_gcd(numerator, denominator)
    lowest_denominator_form = int(denominator / gcd)
    print('The denominator in its lowest form is: {}'.format(lowest_denominator_form))


if __name__ == '__main__':
    main()
