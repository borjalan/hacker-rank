if __name__ == '__main__':
    N = int(input())
    hr_list = []

    functions = {
        'insert': lambda args: hr_list.insert(int(args[0]), int(args[1])) if len(args) >= 2 else None,
        'print': lambda _: print(hr_list),
        'remove': lambda args: hr_list.remove(int(args[0])) if len(args) >= 1 else None,
        'append': lambda args: hr_list.append(int(args[0])) if len(args) >= 1 else None,
        'sort': lambda _: hr_list.sort(),
        'pop': lambda args: hr_list.pop(int(args[0])) if len(args) >= 1 else hr_list.pop(),
        'reverse': lambda _: hr_list.reverse()
    }
    
    for _ in range(N):
        instruction = input().split()

        if len(instruction) >= 1:
            command = instruction[0]
            args = instruction[1:]
        else:
            command = None
            args = []
        
        if command and command in functions:
            functions[command](args)