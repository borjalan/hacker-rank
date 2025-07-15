if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    m = max(s)
    s.remove(m)
    print(max(s))
