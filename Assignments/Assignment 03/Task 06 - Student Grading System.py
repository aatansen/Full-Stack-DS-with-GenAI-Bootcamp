"""
### Task 06 - Student Grading System

> 💼 **Real-world use:** School result automation.

- Write a function `calculate_grade(score)` that:
  - returns `"A+"`, `"A"`, `"A-"`, `"F"` based on numeric marks
- Write another function `grade_students(student_dict)` that:
  - takes a dictionary of `student: score`
  - returns a dictionary of `student: grade`

- **Example**
  - **Input (Scores Dictionary):** `{"Alice": 85, "Bob": 78, "Charlie": 32, "David": 69}`
  - **Output (Grades Dictionary):** `{"Alice": "A+", "Bob": "A", "Charlie": "F", "David": "A-"}`
"""

import ast

def calculate_grade(score):
    if score>=80 and score<=100:
        return "A+"
    elif score>=75 and score<=79:
        return "A"
    elif score>=69 and score<=74:
        return "A-"
    elif score>=65 and score<=68:
        return "B+"
    elif score>=60 and score<=64:
        return "B"
    elif score>=55 and score<=59:
        return "B-"
    elif score>=50 and score<=54:
        return "C+"
    elif score>=45 and score<=49:
        return "C"
    elif score>=33 and score<=44:
        return "D"
    else:
        return "F"

def grade_students(student_dict):
    grade_dict=student_dict
    for name,score in grade_dict.items():
        grade_dict[name]=calculate_grade(score)
    return grade_dict

scores=input("Enter Scores Dictionary: ")
scores_dict=ast.literal_eval(scores)
result=grade_students(scores_dict)
print(result)
