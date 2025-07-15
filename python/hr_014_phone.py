import re

regex = r"^[789]\d{9}$"

if __name__ == '__main__':
    n = input()
    for _ in range(int(n)):
        number = input()
        match = re.fullmatch(regex,number)
        print('YES') if match else print('NO')
