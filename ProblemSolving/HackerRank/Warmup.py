import unittest
import numpy as np
from datetime import datetime

class TestWarmupFunctions(unittest.TestCase):

    # refer to the below page for the problem desciptions
    # https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=warmup
    def test_AddTwoNumbers(self):
        a=5
        b=6
        print(f"Sum of {a} and {b} is: {a+b}")

    def test_simple_array_sum(self):
        # ar = np.array([1,2,3])
        # arrSum = np.sum(ar)
        # print(f"Sum of array is {arrSum}")
        ar = [1, 2, 3]
        print(f"Sum of array is {sum(ar)}")

    def test_compare_triplets(self):
        arr1 = [17,28,30]
        arr2 = [99,16,8]
        x=0
        y=0
        for i,j in zip(arr1, arr2):
            if i>j:
                x=x+1
            elif j>i:
                y=y+1
        print(f"Compare triplets value is {x,y}")

    def test_diagonal_difference(self):
        arr = [[ 11,2,4 ], [ 4, 5, 6 ], [ 10, 8, -12 ]]
        leftDiagonal = 0
        rightDiagonal = 0
        size = len(arr)
        i=0
        while(i<size):
            leftDiagonal = leftDiagonal + arr[i][i]
            rightDiagonal = rightDiagonal + arr[i][size-1-i]
            i=i+1
        print(abs(leftDiagonal-rightDiagonal))

    def test_plus_minus_ration(self):
        arr = [-4, 3, -9, 0, 4, 1]
        positiveNumCount = 0
        negativeNumCount = 0
        zeroCount = 0

        for i in arr:
            if i>0:
                positiveNumCount = positiveNumCount+1
            elif i<0:
                negativeNumCount = negativeNumCount+1
            elif i==0:
                zeroCount = zeroCount+1
        posRatio = "{:.5f}".format(positiveNumCount/len(arr))
        negRatio = "{:.5f}".format(negativeNumCount/len(arr))
        zerRatio = "{:.5f}".format(zeroCount/len(arr))
        print(f"Positive number count {positiveNumCount} and the ratio is {posRatio}")
        print(f"Negative number count {negativeNumCount} and the ratio is {negRatio}")
        print(f"Zero count {zeroCount} and the ratio is {zerRatio}")

    def test_staircase(self):
        n=4
        for i in range(0,n):
            print(" ")
            for j in range(0,n):
                if j>=n-1-i:
                    print("#", end ="")
                else:
                    print(" ", end ="")

    def test_staircases(self,num_stairs=4):
        for stairs in range(1, num_stairs + 1):
            print(' ' * (num_stairs - stairs) + '#' * stairs)

    def test_minmaxsum(self):
        arr=[1,3,5,7,9]
        minArr = arr.copy()
        maxArr = arr.copy()
        minimum = min(arr)
        maximum = max(arr)
        maxArr.remove(minimum)
        minArr.remove(maximum)
        print(sum(minArr), sum(maxArr))

    def test_birthday_cake_candles(self):
        candles = [4,4,1,3]
        maximum = max(candles)
        maxOccurance = len([i for i in candles if i==maximum])
        print(maxOccurance)

    def test_timeConversion(self):
        s = '07:05:45PM'
        t = datetime.strptime(s,'%I:%M:%S%p')
        print(t.strftime('%H:%M:%S'))
