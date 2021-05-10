STUDENTS = []
SECOND_LOWEST_GRADES = []
GRADES = set()

for _ in range(int(input())):
    name = input()
    score = float(input())
    STUDENTS.append([name, score])
    GRADES.add(score)

SECOND_LOWEST = sorted(GRADES)[1]

for name, score in STUDENTS:
    if score == SECOND_LOWEST:
        SECOND_LOWEST_GRADES.append(name)

for name in sorted(SECOND_LOWEST_GRADES):
    print(name, end='\n')
