marks_1 = int(input("Enter the marks of subject 1: "))
marks_2 = int(input("Enter the marks of subject 2: "))
marks_3 = int(input("Enter the marks of subject 3: "))

minimum = min(marks_1,marks_2,marks_3)

sum_of_2 = marks_1 + marks_2 + marks_3 - minimum
avg = sum_of_2//2

print("The average of best two subject marks are: ",avg)