'''
Samuel Calise and Sergio DeSousa-Rosa

Assignment1: matching.py 

link: https://static.us.edusercontent.com/files/9rCWSbfrHBfc2Uji1PjS1aIb
Pages: 1-3
'''
import sys

def fileHandling(filename):
    file = open(filename,"r")
    count = 0
    size = 0
    students = {}
    residents = {}
    data = file.readlines()
    for line in data:
        if count==0 :
            if(line.split()[0].isdigit()):
                size = int(line)
            else:
                exit(1)
        elif count<size:
            students[line.split()[0]] = line.split()[1::]
        else:
            residents[line.split()[0]] = line.split()[1::]
        count += 1

    if(count-1 != size*2):
        exit(1)
    
    return size,students,residents

def stableMatching(num_entries,students,hospitals):
    matches = {}
    freeStudents = []
    freeHospitals = []

    for student in students:
        freeStudents.append(student)
    
    for hospital in hospitals:
        freeHospitals.append(hospital)

    while student in freeStudents:
        currStudent = freeStudents.pop()
        currStudentChoice = students[currStudent][0]
        if currStudentChoice in freeHospitals:
            matches[currStudentChoice] = currStudent
        else:
            curr

def main():
    if( len(sys.argv)==1 ):
       exit(1)
    else:
       num_entries,students,hospital = fileHandling(sys.argv[1])

    matches = stableMatching(num_entries,students,hospital)
    

main()
