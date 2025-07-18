import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []
    
    for i in range(size):
        s = '-'.join(alphabet[i:size])
        line = (s[::-1] + s[1:]).center(4 * size - 3, '-')
        lines.append(line)
    print('\n'.join(lines[::-1]+lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)