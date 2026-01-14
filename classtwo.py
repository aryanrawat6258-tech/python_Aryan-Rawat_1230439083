x = 10
print(x)

#2
num = 10     
num += 5      
print(num)    

#3
num = 10      
num /= 2      
print(num)    

#4
num = 10      
num //= 3     
print(num)

#5
num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("The number is positive and even")
elif num > 0 and num % 2 != 0:
    print("The number is positive and odd")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

#6
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")
#7
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#8
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("The greater number is:", num1)
elif num2 > num1:
    print("The greater number is:", num2)
else:
    print("Both numbers are equal")
#9
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")

#10
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")

#11

year = int(input("Enter a year: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#12

num = int(input("Enter a number: "))


if -9 <= num <= 9:
    print(f"{num} is a single-digit number.")
elif -99 <= num <= 99:
    print(f"{num} is a double-digit number.")
else:
    print(f"{num} has more than two digits.")

#13

day_number = int(input("Enter a day number (1-7): "))


if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid input! Please enter a number between 1 and 7.")

#14

correct_password = "mypassword123"
password = input("Enter your password: ")
if password == correct_password:
    print("Access Granted")
else:
    print("Access Denied")

#15

num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("The number is positive and even.")
elif num > 0 and num % 2 != 0:
    print("The number is positive and odd.")
else:
    print("The number is either zero or negative.")

#17
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")

#18
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))

if sub1 > 35 and sub2 > 35 and sub3 > 35:
    print("Student Passed")
else:
    print("Student Failed")

#18
ch = input("Enter a character: ")
if len(ch) != 1:
    print("Please enter only one character.")
else:
    
    ch = ch.lower()
    if ch.isalpha():
        if ch in "aeiou":
            print("The character is a vowel.")
        else:
            print("The character is a consonant.")
    else:
        print("The character is not an alphabet.")
