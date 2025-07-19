def minion_game(string: str):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    kevin_score = 0
    stuart_score = 0
    max_len = len(string)
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += max_len - i
        else:
            stuart_score += max_len - i
    
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)