universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def tuitions(ll):
    tuitions = []
    for i in range(len(ll)):
        tuitions.append(ll[i][2])
    return tuitions

def students(ll):
    students = []
    for i in range(len(ll)):
        students.append(ll[i][1])
    return students

def enrolment_stats(ll):
    print("Total students:", sum(students(ll)))
    print("Total tuition: $", sum(tuitions(ll)), '\n')

def s_mean(list):
    print("Student mean:", round(sum(list)/len(list), 2))
def s_median(list):
    list = sorted(list)
    l = len(list)
    if l%2==1:
        print("Student median:", list[(l)//2], '\n')
    else:
        print("Student median:", (list[l//2-1]+list[l//2])//2, '\n')

def t_mean(list):
    print("Tuition mean:", round(sum(list)/len(list), 2))
def t_median(list):
    list = sorted(list)
    l = len(list)
    if l%2==1:
        print("Tuition median:", list[(l)//2])
    else:
        print("Tuition median:", (list[l//2-1]+list[l//2])//2)
enrolment_stats(universities)
s_mean(students(universities))
s_median(students(universities))
t_mean(tuitions(universities))
t_median(tuitions(universities))



