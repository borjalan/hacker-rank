def merge_the_tools(string, k):
    substrings = [string[i:i+k] for i in range(0, len(string), k)]
    for subs in substrings:
        proc_subs = []
        for char in subs:
            if char not in proc_subs:
                proc_subs += char
        print(''.join(proc_subs))

# This one is faster because of dict instead of list to verify duplicates
def merge_the_tools2(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        unique_chars = ''.join(dict.fromkeys(substring))
        print(unique_chars)

def merge_the_tools3(string, k):
    for i in range(0, len(string), k):
        seen = set()
        result = []
        for char in string[i:i+k]:
            if char not in seen:
                seen.add(char)
                result.append(char)
        print(''.join(result))

def merge_the_tools4(string, k):
    [print(''.join(dict.fromkeys(string[i:i+k]))) for i in range(0, len(string), k)]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)