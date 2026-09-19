# while loop
'''count=0
while(count<=3):
    count=count+1
    print("Hello Greek")

# while loop with siongle statement
count=0
while(count==0):print("Alishba")'''

#-----for loop----
#---iterating over  list
list=[1,2,3,4,5]
for i in list:
    print(i)

#for tuple
tuple=('a','b','c','d')
for j in tuple:
    print(j)

# iterating over string
s="Alishba"
for i in s:
    print(i)

# ----iterating by index of sequences----
name=["mango","Bnanana","Apple"]
for index in range(len(name)):
    print (name[index])

# ----control statements------
a="Alishba"
for i in a:
    if i=='i' or i=='h':
        continue
    print ("Current letter:",i)
    b="Nasir"
for i in b:
    if i=='i' or i=='h':
        break
    print ("remaining letter:",i)


#-----functions------
def my_function():
    print("Artificial intelligence")
my_function()
def func(name):
    print(name +'\t'+ "Qaiser")
func("Hadiya")

def para(country="Pakistan"):
    print("I am from"+ ' '+country)
para("India")
para("Sweden")

#----passing a list as a Parameter-----

def list(food):
    for i in food:
        print(i)
fruits=['apple','bnana',4,'a']
list(fruits)
#------Return value-----
def mobile(x):
    return 5*x
print(mobile(6))
#-----classes/objects----
class Myclass:
    x=5
c1=Myclass()
print(c1.x)

#----init function----
class Person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
p1=Person("Alishba",21)
print(p1.name)
print(p1.age)

#-----object methods-----
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print("my dog's name is"+ ' '+ self.name)
d=dog("Jerry",2) 
d.bark()



arr=[5,4,3,2,1]
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j=j-1
        arr[j+1]=key
        print("sorted array:",arr)
