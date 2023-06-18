def grading(grades):
    for grade in grades:
        if grade < 38:
            continue
        
        # find the next multiple of 5
        next_multiple = 0

        for count in range(1, 6):
            if (grade + count) % 5 == 0:
                next_multiple = grade + count

        if(next_multiple - grade < 3):
            grades[grades.index(grade)] = next_multiple

    return grades

print(grading([73, 67, 38, 33]))