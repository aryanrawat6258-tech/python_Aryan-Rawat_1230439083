#1

salary = float(input("Enter salary: "))

if salary < 30000:
    salary += salary * 0.20
elif salary <= 60000:
    salary += salary * 0.10

print("New Salary:", salary)

#2

n = int(input("Enter number: "))

if n % 3 == 0 and n % 4 == 0:
    print("Divisible by both 3 and 4")
elif n % 3 == 0 or n % 4 == 0:
    print("Divisible by only one")
else:
    print("Divisible by none")

#3

bill = float(input("Enter bill amount: "))
mode = input("Payment mode: ")
premium = input("Premium member (yes/no): ")

if bill > 5000 and mode == "card":
    bill *= 0.85
elif bill > 5000 or premium == "yes":
    bill *= 0.90

print("Final Bill:", bill)

#4

n = int(input("Enter number: "))

if n % 2 == 0 and 50 <= n <= 100:
    print("Even and between 50–100")
elif n % 2 != 0 and n > 100:
    print("Odd and greater than 100")
else:
    print("Invalid Category")

#5

x = int(input("Enter x: "))

x += 10
x *= 2
x -= 5

print("Final Value:", x)

#6

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a < b < c:
    print("Increasing Order")
else:
    print("Not Increasing")

#7

username = input("Username: ")
password = input("Password: ")
attempts = int(input("Attempts: "))

if username == "admin" and len(password) >= 6 and attempts < 3:
    print("Login Allowed")
else:
    print("Login Denied")

#8

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print((a + b) ** 2 > a**2 + b**2 + c)

#9

n = int(input("Enter number: "))

if n % 2 == 0 and n % 5 == 0:
    print("Divisible by 2 and 5")
elif n % 2 == 0:
    print("Divisible by only 2")
elif n % 5 == 0:
    print("Divisible by only 5")
else:
    print("Not divisible by 2 or 5")

#10

income = float(input("Enter income: "))

tax = 0
if income > 1000000:
    tax = income * 0.20
elif income > 500000:
    tax = income * 0.10
elif income > 250000:
    tax = income * 0.05

print("Tax:", tax)
print("Net Income:", income - tax)

#11

marks = int(input("Enter marks: "))

if marks >= 90:
    print("A - Excellent")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")

#12

units = int(input("Units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print("Bill Amount:", bill)

#13

balance = float(input("Balance: "))
amount = float(input("Withdraw amount: "))

if amount % 100 == 0 and balance - amount >= 500:
    print("Withdrawal Successful")
else:
    print("Withdrawal Denied")

#14

day = int(input("Enter day number: "))

match day:
    case 6 | 7:
        print("Weekend")
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case _:
        print("Invalid Day")

#15

a = int(input("Enter a: "))
b = int(input("Enter b: "))
choice = int(input("Enter choice: "))

match choice:
    case 1:
        print(a + b)
    case 2:
        print(a - b)
    case 3:
        print(a * b)
    case 4:
        print(a / b)
    case _:
        print("Invalid Choice")

#16

age = int(input("Enter age: "))
salary = int(input("Enter salary: "))
medical = input("Medical history: ")

if age >= 25 and salary >= 40000 and medical == "clear":
    print("Eligible")
else:
    print("Not Eligible")

#17

color = input("Signal color: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid")

#18

a = int(input("Side a: "))
b = int(input("Side b: "))
c = int(input("Side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a valid triangle")

#19

result = input("Result (pass/fail): ")
attempts = int(input("Attempts: "))

if result == "fail" and attempts <= 3:
    print("Re-attempt allowed")
else:
    print("No more attempts")

#20

password = input("Enter password: ")

has_digit = any(ch.isdigit() for ch in password)
has_upper = any(ch.isupper() for ch in password)

if len(password) >= 8 and has_digit and has_upper:
    print("Strong")
else:
    print("Weak")

