import math


class ArrayPrograms(object):
    # Python Program to find sum of array
    def SumOfArray(self,arr):
        print(f"Sum of Array {sum(arr)}")

    # Python Program to find largest element in an array
    def LargestElementInArray(self, arr):
        print(f"Largest number in array are {max(arr)}")

    # Python Program for array rotation
    def RotateArray(self, arr, d):
        # Python Program for Reversal algorithm for array rotation
        # Example:
        # Input:  arr[] = [1, 2, 3, 4, 5, 6, 7]
        #          d = 2
        # Output: arr[] = [3, 4, 5, 6, 7, 1, 2]
        print(f"Array before rotation {arr}")
        print(f"Array after rotation {arr[d:]+arr[:d]}")

    # Python Program to Split the array and add the first part to the end
    def SplitArray(self,  arr, d):
        # Input : arr[] = {12, 10, 5, 6, 52, 36}
        #             k = 2
        # Output : arr[] = {5, 6, 52, 36, 12, 10}
        # Explanation : Split from index 2 and first
        # part {12, 10} add to the end .
        print(f"Array before spllit {arr}")
        print(f"Array after split {arr[d:] + arr[:d]}")

    # Python Program for Find reminder of array multiplication divided by n
    def FindRemainder(self, arr, n):
        #print the remainder after multiplying all the numbers divided by n.
        # Input: arr[] = {100, 10, 5, 25, 35, 14},
        # n = 11
        # Output: 9
        # Explanation: 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9
        val = math.prod(arr)
        print(f"Array multiplication is {val} and the remainder after divide with {n} is {val%n}")

    # Python Program to check if given array is Monotonic

obj=ArrayPrograms()
obj.SumOfArray([1,2,3,4,5])
obj.LargestElementInArray([1,8,3,4,5])
obj.RotateArray([1, 2, 3, 4, 5, 6, 7], 3)
obj.RotateArray([12, 10, 5, 6, 52, 36], 2)
obj.FindRemainder([100, 10, 5, 25, 35, 14], 11)



