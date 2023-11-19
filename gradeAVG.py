
stu = int(input("Number of student:"))
def grade_avg(stu):
    sum2 = 0
    for i in range(1,stu+1):
        grade =float(input("Enter student grade:"))
        sum2 +=grade
    avg = sum2/stu
    return avg

result = grade_avg(stu)
print (result)