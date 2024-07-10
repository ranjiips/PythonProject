import unittest
import numpy as np

class TestWarmupFunctions(unittest.TestCase):

    def test_AddTwoNumbers(self):
        a=5
        b=6
        print(f"Sum of {a} and {b} is: {a+b}")

    def test_simple_array_sum(self):
        # ar = np.array([1,2,3])
        # arrSum = np.sum(ar)
        # print(f"Sum of array is {arrSum}")
        ar = [1, 2, 3]
        temp = 0
        for i in ar:
            temp = temp+i
        print(f"Sum of array is {temp}")

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

    # def test_plus_minus_ratio: