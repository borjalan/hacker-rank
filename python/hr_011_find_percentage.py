if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_grades = student_marks.get(query_name)
    print(f"{sum(query_grades)/len(query_grades):.2f}")
