if __name__ == '__main__':
    records = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records[name] = score
    scores = set(records.values())
    lowest_grade = min(scores)
    scores.remove(lowest_grade)
    second_low_grade = min(scores)
    tstudents = list()
    for name in records.keys():
        if records[name] == second_low_grade:
            tstudents.append(name)
    tstudents.sort()
    for name in tstudents:
        print(name)
