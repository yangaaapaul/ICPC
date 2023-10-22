import math

def possible(students, tutors, max_dist):
    students.sort(key=lambda x: x[1])
    tutors.sort(key=lambda x: x[1])
    s, t = 0, 0
    while s < len(students) and t < len(tutors):
        x1, y1 = students[s]
        x2, y2 = tutors[t]
        dist = abs(x1 - x2) + abs(y1 - y2)
        if dist > max_dist:
            t += 1
        else:
            s += 1
            t += 1
    return s == len(students)

def min_dist(students, tutors):
    l, r = 0, max(abs(students[0][1] - tutors[-1][1]), abs(students[-1][1] - tutors[0][1]))
    while l < r:
        mid = (l + r) // 2
        if possible(students, tutors, mid):
            r = mid
        else:
            l = mid + 1
    return l

n = int(input())
students, tutors = [],[]
for i in range(n):
    x,y = map(int, input().split())
    students.append((x,y))
for i in range(n):
    x,y = map(int, input().split())
    tutors.append((x,y))
result = min_dist(students, tutors)
print(result)