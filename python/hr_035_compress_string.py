from itertools import groupby

def compress_string(s: str):
    result = []
    for key, group in groupby(s):
        count = len(list(group))
        result.append(f"({count}, {key})")
    print(" ".join(result))

if __name__ == '__main__':
    a = input()
    compress_string(a)
