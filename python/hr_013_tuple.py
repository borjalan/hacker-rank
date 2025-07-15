if __name__ == '__main__':
    n = int(input())
    hr_tuple = tuple(map(int, input().split()))

    print(hash(hr_tuple))
    