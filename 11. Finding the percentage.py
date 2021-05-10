    n = int(input())
    student_marks = {}
    for line in range(n):
        info = input().split(" ")
        grades = list(map(float, info[1:]))
        student_marks[info[0]] = sum(grades) / float(len(grades))
    
    print("%.2f" % round(student_marks[input()], 2))
