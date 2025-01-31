def main():
    students = [
        {"name": "Ali", "grade": 2.5},
        {"name": "Usman", "grade": 3.4},
        {"name": "Cheema", "grade": 3.0},
        {"name": "Malik", "grade": 2.7}
    ]

    for student in students:
        print("Name: ", student["name"], "Grade: ", student["grade"])

if __name__ == "__main__":
    main()