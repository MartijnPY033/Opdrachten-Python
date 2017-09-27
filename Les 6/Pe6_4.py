studentcijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemmidelde_per_student(studentcijfers):
    student = 0
    lst_average = []
    vg = []
    for cijfers in studentcijfers:
        average = int(sum(cijfers) /3)
        student += 1
        result = 'student %d: gemiddelde %d' % (student, average)
        lst_average.append(result)
        vg.append(average)

        print(vg)
    return lst_average


def gemmidelde_van_alle_studenten(studentcijfers):
    allegemmidelde = 0

    for student in studentcijfers:
        gemmiddelde = int(sum(student) / len(student))
        allegemmidelde = allegemmidelde + gemmiddelde

    #print(str(allegemmidelde / len(studentcijfers)))
    return allegemmidelde / len(studentcijfers)


resultaat1 = gemmidelde_per_student(studentcijfers)
print(resultaat1)
resultaat2 = gemmidelde_van_alle_studenten(studentcijfers)
print(resultaat2)
