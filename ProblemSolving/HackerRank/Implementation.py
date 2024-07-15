import math
import unittest
import numpy as np
from datetime import datetime
class TestImplementationFunctions(unittest.TestCase):

    # refer to the below page for the problem desciptions
    # https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=implementation
    def test_gradingStudents(self):
        print("Logic to implement the grading students")

    def test_apple_orange(self):
        print("Logic to implement the apple and orange")

    def test_number_line_jumps(self):
        print("Logic to implement the number line jumps")

    def test_between_two_sets(self):
        print("Logic to implement the between two sets")

    def test_breaking_the_records(self):
        print("Logic to implement the breaking the records")

    def test_subArrayDivision(self):
        print("Logic to implement the Subarray Division")
        arr = [ 2,2,1,3,2 ]
        d=4
        m= 2
        counter=0
        for i in range(0, len(arr)):
            subList = arr[i:m]
            if(sum(subList)==d):
                counter = counter+1
            m=m+1
        print(counter)

    def test_divisible_sum_pairs(self):
        print("Logic to implement the Divisible Sum Pairs")
        arr=[1,3,2,6,1,2]
        k=3
        counter = 0
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if (arr[i]+arr[j])%k==0:
                    print(arr[i], arr[j])
                    counter = counter+1
        print(counter)

    def test_migratory_birds(self):
        print("Logic to implement the Migratory Birds")
        arr = [ 1, 4, 4, 4, 5, 3, 5, 5 ]
        dummyArray = [0]*len(arr)
        for i in arr:
            dummyArray[i] = dummyArray[i]+1
        print(dummyArray.index(max(dummyArray)))

    def test_day_of_the_programmer(self):
        print("Day of the Programmer")
        year = 2024
        if year==1918:
            print("26.09.2018")
        elif (year <1917 and year%4==0) or (year>1918 and (year %400==0 or (year%4==0 and year%100!=0))):
            print(f"12.09.{year}")
        else:
            print(f"13.09.{year}")

    def test_billDivision(self):
        print("Bill Division")
        bill=[72,53, 60, 66, 90, 62, 12, 31, 36, 94]
        k=6
        b=288

        bill.pop(k)
        sharewithdeduction = sum(bill) / 2
        if sharewithdeduction == b:
            print("Bon Appetit")
        else:
            print(math.trunc(b - sharewithdeduction))

