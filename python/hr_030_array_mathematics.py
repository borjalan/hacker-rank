import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    a_list = []
    for _ in range(n):
        a_list.extend(list(map(int, input().split())))
    a = numpy.array(a_list).reshape(n, m)
    
    b_list = []
    for _ in range(n):
        b_list.extend(list(map(int, input().split())))
    b = numpy.array(b_list).reshape(n, m)
    
    print(numpy.add(a, b))
    print(numpy.subtract(a, b))
    print(numpy.multiply(a, b))
    print(numpy.floor_divide(a, b))
    print(numpy.mod(a, b))
    print(numpy.power(a, b))
