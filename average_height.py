students_height = input("Input a list of student height").split()

for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
    
print(students_height);
print( "{:.2f}".format(sum(students_height)))
print(round(sum(students_height)/len(students_height),2))

#I/P - 154 163 173 183 172 146 153

"""
Input a list of student height154 163 173 183 172 146 153
[154, 163, 173, 183, 172, 146, 153]
1144.00
163.43
"""


