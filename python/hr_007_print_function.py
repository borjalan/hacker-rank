if __name__ == '__main__':
    n = int(input())
    res=0
    i=0
    while i<n:
        if i < 9:
            res = res*10 + (i+1)
        elif i < 99:
            res = res*100 + (i+1)
        else:
            res = res*1000 + (i+1)
        i = i + 1
    print(res)
