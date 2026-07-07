# Mini Project 1 - Student Marks Management System

# Objective
# Manage student names and their marks.

# List for Data Storing
students = []


# 1 Add student name and marks
def std_details():
    name = input("Enter Student Name:")
    marks = float(input("Enter Student Marks:"))

    students.append((name, marks))
std_details()
std_details()
std_details()

# 2 Display Details
def display_details():
    print()
    for n in students:
        print("|", "Student Name:-", n[0], "|", "Student Marks:-" ,n[1], "|")
display_details()

# 3 Search for students
def search_students():
    name = input("Enter Student Name: ")

    for a in students:
        if a[0] == name:
            print("Found")
            print("Student Name:",a[0])
            print("Student Marks:",a[1])
            break

    else:
        print("Student Not Found")
search_students()