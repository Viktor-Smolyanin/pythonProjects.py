grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
average_rate = {students_sorted[0]: sum(grades[0]) / 5, students_sorted[1]: sum(grades[1]) / 4, students_sorted[2]: sum(grades[2]) / 4, students_sorted[3]: sum(grades[3]) / 3, students_sorted[4]: sum(grades[4]) / 5}
print(average_rate)
