def calculate_average(A, B, C):
    average = (A + B+ C) / 3
    return average


students = int(input("How many students? "))

for i in range(students):
    print("\nStudent", i + 1)

    name = input("Enter name: ")
    A = float(input("A: "))
    B = float(input("B: "))
    C = float(input("C: "))

    average = calculate_average(A, B, C)

    print("\n____Student Result____")
    print("Name:", name)
    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("Average:", average)

    if average >= 90:
        print("Excellent")
    elif average >= 80:
        print("Very Good")
    elif average >= 75:
        print("Passed")
    else: 
        print("Failed")
    