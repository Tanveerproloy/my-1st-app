#c style printing

rollno=10
name=("rifaat")
avg=86.3445

print("student name is %s,his rollno. is %d and his marks average are %f"%(name,rollno,avg))
print("student name is %10s,his rollno. is %-5d and his marks average are %2.1f."%(name,rollno,avg))

#formatted printing

a=22
b=7
c=a/b

print("division of {0} and {1} is {2}".format(a,b,c))

print("division of {0:10} and {1:^4} is {2:1.3}".format(a,b,c))

print(f"division of {a:10} and {b:^4} is {c:1.3}")
