if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if b == 0:
        print(f"0\n0")
    else:
        intDiv = a // b
        floDiv = a / b
        print(f"{intDiv}\n{floDiv}")
