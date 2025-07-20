from itertools import permutations

def generate_permutations(elements: list[str], r: int):
    result = list(permutations(elements, r))
    result.sort()
    for perm in result:
        print(''.join(perm))

if __name__ == '__main__':
    input_data = input().split()
    elements = list(input_data[0])
    r = int(input_data[1])
    generate_permutations(elements, r)
    