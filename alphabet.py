Given the names and grades for each student in a class of students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.



if __name__ == '__main__':
    students = []
  
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

   
    grades = sorted(list(set([x[1] for x in students])))
    second_lowest_grade = grades[1]


    low_scorers = [x[0] for x in students if x[1] == second_lowest_grade]

    
    low_scorers.sort()
    for name in low_scorers:
        print(name)

