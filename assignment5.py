# q.1 verify Leap year

y=int(input("Enter a year"))
if(y%4==0):
    if(y%100==0):
        if(y%400==0):
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")


# q.2 check whether the given dimension are of square or rectangle

l=int(input("Enter length"))
b=int(input("Enter breadth"))
if(l==b):
    print("this is square")
else:
    print("this is rectangle")



# q.3 determine oldest and the youngest age

l1=[]
n=int(input("Enter no. of elements in a list"))
for i in range(n):
    l1.append(int(input("Enter a Age")))
print("Oldest age:- ",max(l1))
print("Youngest Age:- ",min(l1))

# q.4 analyse the given data

age=int(input("Enter age"))
sex=input("Enter sex")
m=input("Enter marital status")
if(sex=='F'):
    print("she work in Urban Areas")
else:
    if(age>=20 and age<=40):
        print("he Can work anywhere")
    elif(age>=40 and age<=60):
        print(" he will work in urban areas")
    else:
        print("Error")


# q.5 cost problem

q=int(input("Enter quantity"))
c=100*q
if(c>1000):
    c=c-(c*0.1)
    print("Total cost is =",c)
else:
    print("Total cost is =",c)



#LOOPS

# q.6 print user defined integers
l2=[]
for i in range(10):
    a=int(input("Enter integer"))
    l2.append(a)
print(l2)

# q.7 write an infinite loop

while True:
    print("10")

    
# q.8 make a list which will store square of elements of other list
    
l3=[]
l4=[]
num=int(input("enter number of elements"))
for i in range(num):
    c=int(input("enter the number"))
    l3.append(c)
for j in l3:
    b=j*j
    l4.append(b)
print(l4)

# q.9 group the all data types in a list

l5=[]
l6=[]
l7=[]
l8=[]
a=int(input("Enter total number of inputs"))
for i in range(a):
    b=input("Enter the element")
    l5.append(b)
for i in l5:
    if(i.isdigit()):
        l6.append(i)
    elif(i.isalpha()):
        l7.append(i)
    else:
        l8.append(i)
print(l6)
print(l7)
print(l8)

# q.10 make a list containing prime numbers

a=[]
for i in range(1,101):
    if(i>1):
        flag=False
        for j in range(2,i):
            if(i%j==0):
                flag=True
        if not flag:
            a.append(i)
print(a)

# q.11 pattern

for i in range(5):
    for j in range(i):
        print("*",end='')
    print()


# q.12 search and delete an element from  a user defined list


l9=[]
n=int(input("Enter no. of elements in a list"))
for i in range(n):
    a=int(input("Enter element"))
    l9.append(a)
num=int(input("Enter the no. you want to delete"))
x=l9.count(num)
for i in range(x):
    y=l9.index(num)
    del(l9[y])
print(l9)
