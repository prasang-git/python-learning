# ===== Grade Checker V1.0 =====

Marks = int(input("Enter your marks (0-100): "))

if Marks > 100 or Marks < 0:
    print("Invalid marks!" \
    "Marks should be between 0 and 100.")
elif Marks == 100:
    print("Grade: A+")  
elif Marks >= 90:
    print("Grade: A") 
elif Marks >= 80:
    print("Grade: B+")
elif Marks >= 70:
    print("Grade: B")
elif Marks >= 60:
    print("Grade: C")
elif Marks >= 50:
    print("Grade: D")
elif Marks >= 0:
    print("Grade: F")
else:
    print("Invalid marks!"\
    "Marks should be between 0 and 100.")