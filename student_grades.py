import csv
with open('student_grades.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile)

    header = next(reader)  
    print(header)  # Optional: Print headers and their indices
    print(list(range(len(header))))
    for rows in reader:

        first_name = rows[0]
        last_name = rows[1]
        student_id = rows[2]
        grades = [int(grade)for grade in rows[3:13]]
        mean_grade = sum(grades) / len(grades)
        
        #Output the results
        print(f"{first_name} {last_name} ID: {student_id} - Mean Grade: {mean_grade:.2f}")