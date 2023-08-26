def get_max():
    grades = [9.6, 9.2, 9.7]
    return max(grades)


max_grade = get_max()
print(max_grade)


def get_max_grades():
    grades = [9.6, 9.2, 9.7]
    max_grading = max(grades)
    min_grading = min(grades)

    return f"Max:{max_grading},Min:{min_grading}"

max_min_grades = get_max_grades()
print(max_min_grades)
