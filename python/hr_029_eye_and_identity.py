import numpy

def identity_eye_matrix(n:int, m:int):
    numpy.set_printoptions(legacy='1.13')
    print(numpy.eye(n, m, k=0))

if __name__ == '__main__':
    n, m = map(int,input().split())
    identity_eye_matrix(n,m)