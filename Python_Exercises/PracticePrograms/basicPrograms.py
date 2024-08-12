import math


class BasicPrograms(object):
    # Python program to add two numbers
    def AddTwoNumbers(self, n1, n2):
        print(f"Addition of {n1}+{n2} is {n1+n2}")

    # Maximum of two numbers in Python
    def MaxOfTwoNumbers(self, n1, n2):
        print(f"Maximum of {n1} and {n2} is {max(n1,n2)}")

    # Python Program for factorial of a number
    def FactorialOfNumber(self, num):
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        print(f"Factorial of {num} is {fact}")

    # Python Program for simple interest
    def SimpleInterestCalculation(self, p, t, r):
        #Simple interest formula is given by: Simple Interest = (P x T x R)/100 Where,
        #P is the principal amount T is the time and R is the rate
        print("Simple Interest Calculation:")
        print(f"Principal = {p}")
        print(f"Tenure/Period = {t} months")
        print(f"Rate of Interest = {r}%")
        print(f"Total Interest amount is {(p*t*r)/100}")

    # Python Program for compound interest
    def CompundInterest(self, p, r,t):
        # The formula to calculate compound interest annually is given by:
        # A = P(1 + R/100)^t
        # Compound Interest = A – P
        # Where, A is amount, P is the principal amount, R is the rate and T is the time span
        amount = p*pow((1+r/100), t)
        ci = amount - p
        print(f"Compund Interest:")
        print(f"Principal = {p}")
        print(f"Tenure/Period = {t} months")
        print(f"Rate of Interest = {r}%")
        print(f"Total Interest amount is {ci}")

    # Python Program to check Armstrong Number
    def ArmstrongNumber(self, num):
        sum=0
        for i in str(num):
            sum=sum+int(i)**3
        if sum==num:
            print(f"Given number {num} is a Armstrong Number")
        else:
            print(f"Given number {num} is NOT a Armstrong Number")

    # Python Program for Program to find area of a circle
    def AreaOfCircle(self, r):
        # Area = pi * r2
        # where r is radius of circle
        PI = 3.142
        print(f"Area of circle is {PI*(r**2)}")

    # Python program to print all Prime numbers in an Interval
    def PrimeNumbersInInterval(self, startRange, endRange):
        for i in range(startRange, endRange+1):
            self.IsPrime(i)

    # Python program to check whether a number is Prime or not
    def IsPrime(self, num):
        midVal = num // 2
        flag = 0
        for i in range(2, midVal + 1):
            if num % i == 0:
                flag = 1
                break
            else:
                flag = 0
        if flag == 0:
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a Prime number")

    # Python Program for n-th Fibonacci number
    def FibonacciOfGivenPosition(self,n):
        if n <= 0:
            print("Incorrect input")
        # First Fibonacci number is 0
        elif n == 1:
            return 0
        # Second Fibonacci number is 1
        elif n == 2:
            return 1
        else:
            return self.FibonacciOfGivenPosition(n - 1) + self.FibonacciOfGivenPosition(n - 2)

    # Python Program for How to check if a given number is Fibonacci number?
    def IsFibonacciNumber(self,num):
        n1= (5*(num**2))+4
        n2= (5*(num**2))-4
        sq1 = self.IsPerfectSquare(n1)
        sq2 = self.IsPerfectSquare(n2)

        if sq1==True or sq2==True:
            print(f"{num} is a Fibonacci Number")
        else:
            print(f"{num} is NOT a Fibonacci Number")

    def IsPerfectSquare(self, num):
        val = math.sqrt(num)
        if(val.is_integer()):
            return True
        else:
            return False

    # Python Program for n\’th multiple of a number in Fibonacci Series
    # Program to print ASCII Value of a character
    def GetASCIIOfCharacter(self, char):
        print(f"The ASCII value of {char} is {ord(char)}")

    # Python Program for Sum of squares of first n natural numbers
    def SumOfSquares(self, num):
        sum=0
        for i in range(1,num+1):
            sum = sum + i**2
        print(f"Sum of squares of first {num} natural numbers is {sum}")

    # Python Program for cube sum of first n natural numbers
    def SumOfCubes(self, num):
        sum=0
        for i in range(1,num+1):
            sum = sum + i**3
        print(f"Sum of cubes of first {num} natural numbers is {sum}")

obj=BasicPrograms()
obj.AddTwoNumbers(15,32)
obj.MaxOfTwoNumbers(15,32)
obj.FactorialOfNumber(5)
obj.SimpleInterestCalculation(10000,5,5)
obj.CompundInterest(10000,10.25,5)
obj.ArmstrongNumber(152)
obj.AreaOfCircle(5)
obj.PrimeNumbersInInterval(2,20)
obj.IsPrime(4)
obj.IsFibonacciNumber(5)
print(f"Fibonacci number in {10} position is {obj.FibonacciOfGivenPosition(10)}")
obj.GetASCIIOfCharacter('a')
obj.SumOfSquares(5)
obj.SumOfCubes(5)