# Author: Yanling Wang yuw17@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 12

def getLetterGrade(grade):
    if grade >= 93.0:
        #print("Your letter grade for CMPSC 131 is A.")
        return "A"
    elif grade >= 90.0:
        return "A-"
    elif grade >= 87.0:
        return "B+"
    elif grade >= 83.0:
        return "B"
    elif grade >= 80.0:
        return "B-"
    elif grade >= 77.0:
        return "C+"
    elif grade >= 70.0:
        return "C"
    elif grade >= 60.0:
        return "D"
    else:
        return "F"

def run():
    print("Enter your CMPSC 131 grade: ",end= '')
    grade = input()
    print(f"Your letter grade for CMPSC 131 is {getLetterGrade(float(grade))}.")
    
if __name__ == "__main__":
    run()
