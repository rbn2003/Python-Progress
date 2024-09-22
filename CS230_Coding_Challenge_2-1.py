# Assignment: Simple Grade Calculator with Loops (Using a Flag)
# Objective: Create a Python program that calculates the letter grade for multiple students' scores using a flag to control the loop.

'''
Example CONSOLE Output:

Enter scores for student 1 (0-100) or type 'q' to quit:
Enter score for student 1: 85
Student 1: B

Enter score for student 1 (0-100) or type 'q' to quit:
Enter score for student 1: 105
Invalid score. Please enter a score between 0 and 100.
Enter score for student 1: 72
Student 1: C

Enter scores for student 2 (0-100) or type 'q' to quit:
Enter score for student 2: 91
Student 2: A

Enter scores for student 3 (0-100) or type 'q' to quit:
Enter score for student 3: q

'''

# Instructions START FROM THE TOP AND READ CAREFULLY!:

# 1. Define a predefined number of students.
#    - Create a variable (e.g., `num_students`) to store the number of students you want to process. You'll need this to control the loop.

# 2. Create a `for` loop to iterate through each student.
#    2a. Inside the `for` loop, print a message asking the user to enter scores for the current student.
#        - Display a message like "Enter scores for student 1 (0-100) or type 'q' to quit:" to clearly instruct the user.
#    - Use the `range()` function to specify how many times the loop should iterate.
#        - The `range()` function is used to create a sequence of numbers that represent the students' identifiers. In this case, it ensures that the loop iterates the desired number of times.
#        - Remember that Python uses 0-based indexing, so you may need to adjust the range to start from 1 if you want the student numbers to start from 1.

# 3. Inside the `for` loop, create a flag variable (`student_done`) and set it to `True`.
#    - The flag (`student_done`) will be crucial in controlling the loop for each student. Think about how and where to use it effectively.
#    - The `student_done` flag can be used as a condition in the `while` loop to control whether the current student's scores are being entered.

# 4. Use a `while` loop to repeatedly take user input for numerical scores (0 to 100) as integers while the flag is `True`.
#    4a. Get the input score from the user or allow them to quit.
#        - Use the `input()` function to collect scores from the user. Make sure to handle the user's request to quit gracefully.
#        - To quit entering scores for the current student, you should check whether the user input matches the quit option (e.g., 'q' or 'quit').

# 5. Inside the `while` loop, check if the input score is within the valid range (0-100). If it's not, display an error message and ask the user to re-enter the score.
#    5a. Check if the input score is within the valid range (0-100).
#        - Utilize conditional statements (if, elif, else) to verify the score's validity. Consider how to handle invalid scores.
#        - Provide a clear error message to guide the user on what's expected in terms of valid scores.

# 6. Use control structures (if, elif, else) to calculate the letter grade based on the following grading scale:
#    - A: 90-100
#    - B: 80-89
#    - C: 70-79
#    - D: 60-69
#    - F: 0-59
#        - Think about how to structure your conditional statements to assign the appropriate letter grade based on the input score.
#        - You can use nested if-elif-else statements to make it clear and organized.

# 7. Display the calculated letter grade for each student.
#        - Utilize the `print()` function to display the grade to the user in a clear and informative way.
#        - Ensure that each student's grade is displayed separately and labeled for clarity.

# HINT! Implement a way for the user to decide when to stop entering scores (e.g., by typing 'q' or 'quit' when prompted).
#       If the user enters 'q' or 'quit,' set the flag (`student_done`) to `False` to exit the inner loop.
#        - Allow the user to exit the loop gracefully when they are finished entering scores for a student.
#        - Make sure the user understands how to exit and provide clear instructions when prompting for input.


#My code begins from here: 

num_students = 5 #it will work for 5 different students! 

for student_id in range(1, num_students + 1):  # Adjusting range to start from 1 and including all students
    print(f"Enter scores for student {student_id} (0-100) or type 'q' to quit:")
    
    student_done = False
    
    
    while not student_done: 
        score_input = input("Enter Score: ")
        
        if score_input.lower() == 'q' or score_input.lower() == 'quit':
            student_done = True
            continue 
        
        if not score_input.isnumeric():
            print("Invalid Input. Please enter a numeric score: ")
            continue 

        score = int(score_input)
            
        if score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
    

        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'


        print(f"Student {student_id} - Score: {score}, Grade: {grade}")  # in a line, it will be easier for user to work ! 
