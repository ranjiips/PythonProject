# Python program to add two numbers
def addtwonumbers(num1,num2):
    sum=num1+num2
    print(f"Sum of {num1}+{num2}={sum}")

# Maximum of two numbers in Python
def maximum_of_two_numbers(num1,num2):
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1==num2:
        print(f"{num1} equal to {num2}")
    else:
        print(f"{num2} is greater than {num1} ")

# Python Program for factorial of a number
def factorial_of_number(num1):
    fact=1
    for i in range(1,num1+1):
        fact=fact*i
    print(f"Factorial of {num1} is {fact}")

# Python Program for simple interest
# Python Program for compound interest
# Python Program to check Armstrong Number
def armstrong_number(num):
    result = 0
    for i in str(num):
        result = result + (int(i)**3)
    if result==num:
        print(f"The number {num} is an Armstrong number")
    else:
        print(f"The number {num} is NOT an Armstrong number")
# Python Program for Program to find area of a circle
# Python program to print all Prime numbers in an Interval
# Python program to check whether a number is Prime or not
# Python Program for n-th Fibonacci number
# Python Program for How to check if a given number is Fibonacci number?
# Python Program for n\’th multiple of a number in Fibonacci Series
# Program to print ASCII Value of a character
# Python Program for Sum of squares of first n natural numbers
# Python Program for cube sum of first n natural numbers

addtwonumbers(10,20)
maximum_of_two_numbers(50,40)
factorial_of_number(4)
armstrong_number(154)