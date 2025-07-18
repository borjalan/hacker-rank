def print_formatted(number):
    w = len('{0:{base}}'.format(number, base='b'))
    for n in range(1,number+1):
        for base in 'doXb':
            print('{0:{width}{base}}'.format(n, base=base, width=w), end=' ')
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)