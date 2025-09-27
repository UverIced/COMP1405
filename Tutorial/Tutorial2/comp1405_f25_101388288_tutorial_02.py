"""
Name: John Ketiku
Student ID: 101388288
"""

# start program
def main():
    # get students marks
    tut_mark = float(input("\nInput your grade average for tutorials: "))
    mid1_mark = float(input("Input your grade for Midterm1: "))
    mid2_mark = float(input("Input your grade for Midterm2: "))
    assign_mark = float(input("Input assignment grade average: "))
    exam_mark = float(input("Input your grade for the final exam: "))

    # weight from our course outline
    tut_weight = 0.10 #10%
    assign_weight = 0.40 #40%
    mid1_weight = 0.15 #15%
    mid2_weight = 0.15 #15%
    exam_weight = 0.20 #20%

    # total mark
    total_mark  = (tut_mark*tut_weight)+(assign_mark*assign_weight)+(mid1_mark*mid1_weight)+(mid2_mark*mid2_weight)+(exam_mark*exam_weight)

    # figure out student grade
    if total_mark >= 90:
       grade = "A+"
    elif total_mark >= 85:
       grade = "A"
    elif total_mark >= 80:
       grade = "A-"
    elif total_mark >= 77:
       grade = "B+"
    elif total_mark >= 73:
       grade = "B"
    elif total_mark >= 70:
       grade = "B-"
    elif total_mark >= 67:
       grade = "C+"
    elif total_mark >= 63:
       grade = "C"
    elif total_mark >= 60:
       grade = "C-"
    elif total_mark >= 57:
       grade = "D+"
    elif total_mark >= 53:
       grade = "D"
    elif total_mark >= 50:
       grade = "D-"
    else:
       grade = "F"

    # print results
    print(f"\nYour final mark is: {total_mark: .2f}")
    print(f"Your Grading is: {grade}")

main()
