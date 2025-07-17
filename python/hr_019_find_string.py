def count_substring(string, sub_string):
    count = 0
    i = 0
    while i <= len(string) - len(sub_string):
        if(string[i:i+len(sub_string)] == sub_string):
            count += 1
        i += 1
    return count

def count_substring2(string, sub_string):
    return sum(1 for i in range(len(string) - len(sub_string) + 1) 
               if string[i:i+len(sub_string)] == sub_string)

def count_substring3(string, sub_string):
    return sum(string[i:].startswith(sub_string) 
               for i in range(len(string) - len(sub_string) + 1))

def count_substring_optimal(string, sub_string):
    count = 0
    start = 0
    while True:
        pos = string.find(sub_string, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring_optimal(string, sub_string)
    print(count)