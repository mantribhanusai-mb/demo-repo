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

#python memory model
a = 10
print(id(a))
b = 20
print(id(b))
c = 10
print(id(c))

# a,b,c int which is simple data type (one only value)

#python has complex data types (more than one value)

list_num_a = [10,20,30,40,50]  #list is created using [value1,value2,....value-n]
print(type(list_num_a))
print(id(list_num_a))

list_num_b = [10,20,30,40,50]  
print(type(list_num_b))
print(id(list_num_b))

#to access data inside list we use index -> index starts from o 1 2....

print(list_num_a[0])
print(list_num_b[2])
 
