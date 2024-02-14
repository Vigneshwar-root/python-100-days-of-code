student_scores = input("Input a list of students scores").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
maxi = student_scores[0]
for n in range(0, len(student_scores)):
      if(n != len(student_scores)-1):
        print(student_scores[n])
        print(student_scores[n+1])
        if(maxi < student_scores[n+1]):
            maxi = student_scores[n]
            
print(student_scores)
print(max(student_scores))
print(f"the highest score in the class is {maxi}")

#Input - 88 67 34 45 99 92 34 74 78 67 34 90