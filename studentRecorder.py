
import os
import sys


## 1 Create a file with name, grade, school name
## 2 Ask the user about this info and write it into the file
## 3 Read the file and display all the students information
## 4 get student info
## 5 Delete student info
## 6 Update student info
##  Name,grade,school name
## follows csv format (comma separating values)

def getStudent():
    ## Search the file and display the information
    file = open('studentInfo.txt', mode='r')
    userSearch = input ("Enter name to search database: ")

    for lines in file: 
        lineData = lines.split (',')
        if userSearch == lineData [0]:  
            print ("Found")
            print (lines)
            break               
    else: 
        print ("Invalid Search")

def deleteStudent():
    ## Find and remove the student record from the file    
    with open('studentInfo.txt', mode='r+') as file:
        userSearch = input ("Enter name to be deleted: ")
        for lines in file: 
            lineData = lines.split (',')
            if userSearch == lineData [0]:  
                print ("Found")
                print (type (lineData))
                del lineData [0:3]
                
                print (lineData)
                break
        else: 
            print ("Invalid Search")        

def updateStudent():
    ## Find the student and change their grade and schools
    file = open('studentInfo.txt', mode='r')
    userSearch = input ("Enter name to update database: ")

    for lines in file: 
        lineData = lines.split (',')
        if userSearch == lineData [0]:  
            print ("Found")
            print (lines)
            break               
    else: 
        print ("Invalid Search")    
    file = open('studentInfo.txt', mode='w+')
    newGrade = input ("Enter new Grade: ")
    newSchool = input ("Enter new School: ")
    grade = str.replace (grade, newGrade)
    sn = str.replace (sn, newSchool)
    
    pass

def addStudent(name, grade, schoolName):
    file = open('studentInfo.txt', mode='a')
    file.write(name)
    file.write(',')
    file.write(grade)
    file.write(',')
    file.write(schoolName)
    file.write('\n')

def readStudents():
    print ('====Student Record System==')
    print ('Name          Grade  School')
    print ('---------------------------------')
    
    file = open('studentInfo.txt', mode='r')
    for line in file:
        rec = line.split(',')
        print (rec[0].ljust(14), end='')
        print (rec[1].ljust(8), end='')
        print (rec[2], end='')        

    print ('---------------------------------')
    print ('')
 
 
## main  
print ('Welcome to the student Recorder System')

print ('----------------------')
print ('A:     Add a Student')
print ('D:     Delete a Student')
print ('RR:    Read the records')
print ('R:     Read specific Record')
print ('U:     Update a Student Record')
print ('Q:     End System')

func = input ('Enter your choice: ')

if func == 'A':
    while True:
        name = input('Enter Student Name (Q to Quit): ')
        if name == 'Q':
            print ('Thanks for using student recoder system, come again')       
            break
        
        grade = input('Enter Student Grade: ')
        sn = input('Enter School Name: ')

        addStudent(name, grade, sn)
elif func == 'RR':
    readStudents()
elif func == 'U':    
    updateStudent ()
elif func == 'D':   
    deleteStudent ()
elif func == 'R':
    ## Ask the use about the name
    ## Search in the file and display the info
    getStudent ()
else:
    print ('Invalid Choice, better luck next time')
