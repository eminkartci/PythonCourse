

## PYTHON


# Print Welcome Title
print("\n\n--- A-MEAN Grade Calculator ---\n\n")

# Get Student Name from User
studentName = input("Name: ")

# Try - Get Exam Grades
try:

    mid1 = int(input("Midterm 1: "))
    mid2 = int(input("Midterm 2: "))
    final = int(input("Final   : "))

except: # If it is not an integer warn the user
    print("Please type an integer !!")

# Calculate the average
average = mid1 * 0.3 + mid2 * 0.3 + final * 0.4

## Decide the letter grade
letterGrade = ""

if(average > 90):
    letterGrade = "A"
elif(average > 80):
    letterGrade = "B"
elif(average > 70):
    letterGrade = "C"
elif(average > 60):
    letterGrade = "D"
else:
    letterGrade = "F"


print("------------------------")
print("Student  : " , studentName)
print("Midterm 1: " , mid1)
print("Midterm 2: " , mid2)
print("Final    : " , final)
print("------------------------")
print("Aveage       : " , average)
print("Letter Grade : " , letterGrade)


