from itertools import combinations_with_replacement

def combination_with_replacement_generator(elements: list[str], r: int):
    elements.sort()
    result = list(combinations_with_replacement(elements, r))
    for comb in result:
        print(''.join(comb))

if __name__ == '__main__':
    input_data = input().split()
    elements = list(input_data[0])
    r = int(input_data[1])
    combination_with_replacement_generator(elements, r)
