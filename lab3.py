# q no 1
for number in range(1500, 2701):
    if number % 7 == 0 and number % 5 == 0:
     print (number)

# qno 2
c = float(input("Enter temperature in Celsius: "))
f = (c * 9 / 5) + 32
print(c, "C is", round(f), "in Fahrenheit")
f = float(input("Enter temperature in Fahrenheit: "))
c = (f - 32) * 5 / 9
print(f, "F is", round(c), "in Celsius")

# q no 3
import random
number = random.randint(1, 9)
while True:
 guess = int(input("Guess a number between 1 and 9: "))
 if guess == number:
  print("Well guessed!")
  break
else:
 print("Wrong guess. Try again.")

# q no 4
for i in range(1,6):
 for j in range(i):
    print("*",end=" ")
 print()
for i in range(4,0,-1):
 for j in range(i):
    print("*",end=" ")
 print()


 # q no 5
word = input("Enter a word: ")
print("Reversed word:", word[::-1])

 # q no 6
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for number in numbers:
 if number % 2 == 0:
  even += 1
 else:
  odd += 1
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)

# q no 7

datalist = [1452, 11.23, 1+2j, True, 'w3resource',
             (0, -1), [5, 12], {"class": "V", "section": "A"}]
for item in datalist:
    print(item, "->", type(item))

# q no 8

for number in range(7):
    if number == 3 or number == 6:
        continue
    print(number)

# q no 9

a = 0
b = 1
while b <= 50:
    print(b, end=" ")
    print()
    a, b = b, a + b




# q no 10
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
array = []  
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(i * j)
    array.append(row)
print(array)

# q no 11

print("Enter lines (blank line to terminate):")
while True:
    line = input()
    if line == "":
        break
    print(line.lower())

# q no 12

data = input("Enter 4-digit binary numbers separated by commas: ")
numbers = data.split(",")
result = []
for binary in numbers:
    if int(binary, 2) % 5 == 0:
        result.append(binary)
print(",".join(result))

# q no 13

text = input("Enter a string: ")
letters = 0
digits = 0
for character in text:
    if character.isalpha():
        letters += 1
    elif character.isdigit():
        digits += 1
print("Letters", letters)
print("Digits", digits)

# q no 14

password = input("Enter password: ")
has_lower = any(c.islower() for c in password)
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "$#@" for c in password)
if (6 <= len(password) <= 16 and
        has_lower and has_upper and has_digit and has_special):
    print("Valid password")
else:
    print("Invalid password")

    
