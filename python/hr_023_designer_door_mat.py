def designer_door_mat(n, m, mat_name, pattern):
    mat = []
    for i in range(n):
        if i < n // 2:
            row = pattern * (i * 2 + 1)
        elif i == n // 2:
            row = mat_name.center(m, '-')
        else:
            row = pattern * ((n - i - 1) * 2 + 1)
        mat.append(row.center(m, '-'))
    return '\n'.join(mat)

if __name__ == '__main__':
    mat_name = 'WELCOME'
    pattern = '.|.'
    n, m  = map(int,input().split())
    mat = designer_door_mat(n, m, mat_name, pattern)
    print(mat)