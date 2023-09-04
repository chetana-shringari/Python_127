''' (a) Develop a python program to read student details Name, USN and Marks in the three subjects.
Display the student details , total marks and percentage with suitable messages '''

name = input('Enter the student name: ')
usn = input('Enter the student USN: ')
phy = int(input('Enter the marks obtained in Physics: '))
che = int(input('Enter the marks obtained in Chemistry: '))
mat = int(input('Enter the marks obtained in Mathematics: '))
max_marks = 300
print(30 * '*')
print('Name of the Student:', name)
print('Student USN:', usn)
print(30 * '*')
total = phy + che + mat
print('The total marks scored by the student in Physics', phy, 'Chemistry', che, 'Mathematics', mat, 'is', total)
print(30 * '*')
percent = (total/max_marks) * 100
print('Percentage of the Student:', round(percent))

''' (b) Python program to calculate distance between two points '''
import math
x1 = float(input('Enter the x1 value: '))
x2 = float(input('Enter the x2 value: '))
y1 = float(input('Enter the y1 value: '))
y2 = float(input('Enter the y2 value: '))
print('Co-ordinates of first point are (',x1, ',', y1,')')
print('Co-ordinates of second point are (',x2, ',', y2,')')
r = math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2))
print('Distance between two points is ', r)
