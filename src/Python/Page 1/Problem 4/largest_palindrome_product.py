def main():
    palin_nums = []
    for i in reversed(range(1000)):
        inner_loop = i
        for j in reversed(range(0, inner_loop+1)):
            product = i * j
            rev_product = str(product)[::-1]
            if product == int(rev_product):
                palin_nums.append(product)
    print('The largest palindrome number that is the product of two 3-digit numbers is: {}'.format(max(palin_nums)))


if __name__ == '__main__':
    main()
