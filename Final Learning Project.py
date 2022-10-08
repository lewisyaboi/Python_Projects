from statistics import mean as m

admins = {'Python':'Pass123@','user2':'pass2'}

studentDict = {'Jeff':[78,88,93],
               'Alex':[92,76,88],
               'Sam':[89,92,93]}

def enterGrades():
    nameToEnter = input('\nStudent Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('\nAdding Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist.')

    print(studentDict)

def removeStudent():
    nameToRemove = input('\nStudent Name: ')
    if nameToRemove in studentDict:
        print('\nRemoving student...')
        del studentDict[nameToRemove]
    else:
        print('Student does not exist.')

    print(studentDict)

def studentAVG():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)
        
        print(eachStudent,'has an average grade of:',avgGrade)
        

def main():
    print("""
    Welcome to Grade System

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Averages
    [4] - Exit
    """)

    action = input('What would you like to do today? (Please enter a number) ')

    if action == '1':
        enterGrades()

    elif action == '2':
        removeStudent()

    elif action == '3':
        studentAVG()

    elif action == '4':
        exit()

    else:
        print('No valid choice was given, please try again')



login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('\nWelcome,', login)
        while True:
            main() 
    else:
        print('Invalid password')
else:
    print('Invalid username')
