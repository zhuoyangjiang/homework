# Author: Yanling Wang yuw17@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 12
def getLetterGrade(grade):
    print(f"Enter your CMPSC 131 grade:{grade}")
    if grade >= 93.0:
        print("Your letter grade for CMPSC 131 is A.")
    elif grade >= 90.0:
        print("Your letter grade for CMPSC 131 is A-.")
    elif grade >= 87.0:
        print("Your letter grade for CMPSC 131 is B+.")
    elif grade >= 83.0:
        print("Your letter grade for CMPSC 131 is B.")
    elif grade >= 80.0:
        print("Your letter grade for CMPSC 131 is B-.")
    elif grade >= 77.0:
        print("Your letter grade for CMPSC 131 is C+.")
    elif grade >= 70.0:
        print("Your letter grade for CMPSC 131 is C.")
    elif grade >= 60.0:
        print("Your letter grade for CMPSC 131 is D.")
    else:
        print("Your letter grade for CMPSC 131 is F.")


if __name__ == "__main__":
    grade = input()
    getLetterGrade(float(grade))