from itertools import combinations

def combination_generator(elements: list[str], r: int):
    elements.sort()
    for subr in range(1, r + 1):
        result = list(combinations(elements, subr))
        for comb in result:
            print(''.join(comb))

if __name__ == '__main__':
    input_data = input().split()
    elements = list(input_data[0])
    r = int(input_data[1])
    combination_generator(elements, r)
