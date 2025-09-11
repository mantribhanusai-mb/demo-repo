#working with variables

#assigning data

student_name = "Bhanusai"
student_age = 24
student_grade = 10 

#retrieve data
print(student_name)
print(student_age)
print(student_grade)

#getting identity / memory
print(id(student_name))
print(id(student_age))

#getting type of data
print(type(student_name))
print(type(student_age))

# in python variable can change during execution

x = 10
print("Initially:", x)

x = x+5 # changes value
print("after addition:", x )

x = "salaar"  #type can also change
print("after reassignment:", x)