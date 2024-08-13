import math
import string
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

    def test_sockMerchant(self):
        ar = [ 10, 20, 20, 10, 10, 30, 50, 10, 20 ]
        distinctItems = set(ar)
        pairs = 0
        for i in distinctItems:
            occurance = ar.count(i)
            if occurance // 2 > 0:
                pairs=pairs+ (occurance // 2)
                print(f"Total number of Socks {i} is {occurance} and the pair is {occurance//2}")
        return pairs

    def test_drawingBooks(self):
        pages = 19
        n = pages
        p = 12
        totalFlips = int(n / 2)
        flip = 0
        if p > totalFlips:
            for i in range (totalFlips):
                if n == p:
                    flip = i
                    break
                elif n % 2 == 0:
                    if (n == p) or (n + 1) == p:
                        flip = i
                        break
                    else:
                        n -= 2
                else:
                    if (n == p) or (n - 1) == p:
                        flip = i
                        break
                    else:
                        n -= 2
        else:
            for i in range (totalFlips):
                if i == 0 and (i + 1) == p:
                    flip = i
                    break
                elif flip > 0 and (flip == p or (flip + 1) == p):
                    flip = i
                    break
                else:
                    flip += 2
        print(f"Total number of pages: {pages}, Page to navigate: {p}, Number of flips: {flip}")

    def test_counting_valleys(self):
        steps= 8
        path = "UDDDUDUU"
        currStep=0
        prevStep=0
        valley=0

        for i in range(steps):
            prevStep=currStep
            if path[i]=='D':
                currStep=currStep-1
            else:
                currStep=currStep+1
            if(currStep==0 and prevStep==-1):
                valley=valley+1
            #print(f"Path:{path[i]}, Current level: {currStep}, Previous level: {prevStep}, Valley:{valley}")

        print(f"Total number of valleys travelled: {valley}")

    def test_electroniShops(self):
        budget=60
        keyboardPrice = [40,50,60]
        usbDrivePrice = [25,28,12]
        expensivePrice=0

        for k in keyboardPrice:
            for u in usbDrivePrice:
                price = k+u
                if price>expensivePrice and price<= budget:
                    expensivePrice = price
        if expensivePrice==0:
            expensivePrice = -1
        print(f"The expensive purchase is {expensivePrice}")

    def test_CatAndMouse(self):
        x=2
        y=5
        z=3

        if abs(x-z) < abs(y-z):
            print("Cat A catches the mouse")
        elif abs(x-z) > abs(y-z):
            print("Cat B catches the mouse")
        else:
            print("Mouse C escapes, since both the cat are busy in fighting")

    def test_pickingNumbers(self):
        a=[1, 1, 2,3, 2, 4, 4, 5, 5,2, 5,6,7,6,6,8,9,8,9,0]
        a.sort()
        temparr = []
        maxArrr=0
        min=a[0]
        for i in a:
            if (i-min) <=1:
                temparr.append(i)
            else:
                if len(temparr)>= maxArrr:
                    maxArrr = len(temparr)
                min=i
                temparr.clear()
                temparr.append(i)
        if len(temparr) >= maxArrr:
            maxArrr = len(temparr)

        print(f"The length of maximum sub list is {maxArrr}")

    def test_hurdleRace(self):
        height = [1,2,3,3,2]
        k=1
        maxHeight = max(height)
        if maxHeight>k:
            print(f"Dose required: {maxHeight-k}")
        else:
            print(f"Dose required: 0")

    def test_designer_pdf_viewer(self):
        h=[1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
        word = 'zaba'
        size=len(word)
        tallestLetter = 1
        for i in word:
            charIndex=string.ascii_lowercase.index(i)
            if(h[charIndex]>tallestLetter):
                tallestLetter=h[charIndex]
        print(f'Size of the highlighted area is {size*tallestLetter}')

    def test_utopianTree(self):
        n=5
        val=1
        for i in range(0,n+1):
            if i==0:
                val = val+i
            elif i%2==0:
                val = val+1
            else:
                val = val+val
        print(f"The height of the tree after the given number of cycles {n} is {val}")

    def test_angryProfessor(self):
        a=[26, 94, -95, 34, 67, -97, 17, 52, 1, 86]
        k=7
        count = len([x for x in a if x<=0])
        if count>=k:
            print(f"Number of student present are {count}, expectd is {k}, Class will continue - NO")
        else:
            print(f"Number of student present are {count}, expectd is {k}, Class will not continue - YES")
