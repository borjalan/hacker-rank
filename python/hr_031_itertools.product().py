from itertools import product

def cartesian_product(a: list[int], b: list[int]) :
    print(*list(product(a, b)))


if __name__ == '__main__':
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    cartesian_product(a, b)