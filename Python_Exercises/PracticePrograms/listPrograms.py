import copy
import math


class ListPrograms(object):
    # Python program to interchange first and last elements in a list
    def SwapListElements(self, list):
        #Input : [12, 35, 9, 56, 24] Output : [24, 35, 9, 56, 12]
        print(f"Before interchange first and last elements in a list: {list} ")
        swapList = list[:-2:-1]+list[1:-1]+list[0:1]
        print(f"After interchange first and last elements in a list: {swapList} ")

    # Python program to swap two elements in a list
    def SwapPositions(self, list, pos1, pos2):
        #swap the two elements in the list.
        # Examples:
        # Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
        # Output : [19, 65, 23, 90]
        print(f"Before swap the two elements in the list: {list} ")
        pos1=pos1-1
        pos2=pos2-1
        list[pos1], list[pos2] = list[pos2], list[pos1]
        print(f"After swap the two elements from position{pos1} and {pos2} in the list: {list} ")


    # Python | Ways to find length of list
    def LengthOfList(self, list):
        print(f"Length of the list {list} is {len(list)}")

    # Python | Ways to check if element exists in list
    def IsElementExist(self, list, value):
        flag=False
        for i in list:
            if i==value:
                flag=True
                break
        return flag

    def IsElementExistinList(self, list, value):
        if value in list:
            return True
        else:
            return False

    # Different ways to clear a list in Python
    def ClearList(self,val):
        print(f"List before clear: {val}")
        val.clear()
        print(f"List after clear: {val}")


    # Python | Reversing a List
    def ReverseList(self, val):
        print(f"Original List: {val}")
        print(f"Reverse List: {val[::-1]}")

    # Python program to find sum of elements in list
    def SumOfElementsList(self, list):
        #Input: [12, 15, 3, 10]
        # Output: 40
        print(f"Sum of the list {list} is {sum(list)}")

    # Python | Multiply all numbers in the list
    def MultiplyList(self, list):
        print(f"Multiply list values {list} is {math.prod(list)}")

    # Python program to find smallest number in a list
    def SmallestNumberInList(self, list):
        print(f"Smallest number from the list {list} is {min(list)}")

    # Python program to find largest number in a list
    def LargestNumberInList(self, list):
        print(f"Largest number from the list {list} is {max(list)}")

    # Python program to find second largest number in a list
    def SecondLargestNumber(self, listvalues):
        listvalues=sorted(listvalues, reverse=True)
        print(f"Second largest number from the list {listvalues} is {listvalues[1]}")

    # Python program to find N largest elements from a list
    def FindNlargestElements(self,list, n):
        #Input : [81, 52, 45, 10, 3, 2, 96]
        # N = 3
        # Output : [81, 96, 52]
        sortedList = sorted(list, reverse=True)
        print(f"List {list}, {n} largest element from the list is {sortedList[:3]}")

    # Python program to print even numbers in a list
    def EvenNumbersInList(self, list):
        even = [x for x in list if x%2==0]
        print(f"List: {list}, Even numbers are {even}")

    # Python program to print odd numbers in a List
    def OddNumbersInList(self, list):
        odd = [x for x in list if x%2>0]
        print(f"List: {list}, odd numbers are {odd}")

    # Python program to print all even numbers in a range
    def EvenNumberInRange(self, start, end):
        even = [i for i in range(start, end+1) if i%2==0]
        print(f"Print the even numbers in the range {start}-{end}: {even}")

    # Python program to print all odd numbers in a range
    def OddNumberInRange(self, start, end):
        odd = [i for i in range(start, end+1) if i%2>0]
        print(f"Print the odd numbers in the range {start}-{end}: {odd}")

    # Python program to print positive numbers in a list
    def PositiveNumbers(self, list):
        positive = [i for i in list if i>0]
        print(f"Postive numbers in the list {list} are {positive}")

    # Python program to print negative numbers in a list
    def NegativeNumbers(self, list):
        negative = [i for i in list if i<0]
        print(f"Negative numbers in the list {list} are {negative}")

    # Python program to print all positive numbers in a range
    def AllPositiveNumbersInRange(self, start, end):
        positiveRange = [i for i in range(start, end+1) if i>=0]
        print(f"Positive numbers in the range of {start}-{end} are {positiveRange}")

    # Python program to print all negative numbers in a range
    def AllNegativeNumbersInRange(self, start, end):
        negativeRange = [i for i in range(start, end+1) if i<0]
        print(f"Negative numbers in the range of {start}-{end} are {negativeRange}")

    # Remove multiple elements from a list in Python
    def RemoveMultipleElement(self):
        #Removing all even elements in a list
        lst = [23, 65, 19, 3, 90, 12, 35, 9, 56, 24]
        print(f"List: {lst}")
        for i in lst:
            if i%2==0:
                lst.remove(i)
        print(f"After removing even numbers: {lst}")

        #Fetch odd  numbers
        lst = [23, 65, 19, 3, 90, 12, 35, 9, 56, 24]
        oddNumbers = [i for i in lst if i%2!=0]
        print(f"List: {lst}, fetch odd numbers: {oddNumbers}")

        #Remove adjacent elements using list slicing
        lst = [23, 65, 19, 3, 90, 12, 35, 9, 56, 24]
        print(f"Actual List: {lst}")
        del lst[2:5]
        print(f"After Remove the range [2:5]: {lst}")

        #Remove the  given elements
        lst = [23, 65, 19, 3, 90, 12, 35, 9, 56, 24]
        print(f"Actual List: {lst}")
        result = [i for i in lst if i not in [3,56]]
        print(f"List after removed 3and 56 is {result}")

    # Python – Remove empty List from List
    def  RemoveEmptyList(self):
        test_list = [5, 6, [], 3, [], [], 9]
        newList=[i for i in test_list if i!=[]]
        print(f"Original List: {test_list}, list after remove empty list {newList}")

    # Python | Cloning or Copying a list
    def CopyList(self, list):
        # Using the slicing technique
        listUsingSlicing=list[:]
        print(f"New list using Slicing: {listUsingSlicing}")

        # Using the extend() method
        listUsingExtend=[]
        listUsingExtend.extend(list)
        print(f"New list using Extend: {listUsingExtend}")

        # List copy using =(assignment operator)
        listUsingEqualTo = list
        print(f"New list using Equal Operator: {listUsingEqualTo}")

        # Using the method of Shallow Copy
        copyList = copy.copy(list)
        copyList[3] = 7
        print("Original List:", *list)
        print("Shallow Copy List:", *copyList)

        # Using list comprehension
        newList = [i for i in list]
        print("Newly copied list using list comprehension is ", *newList)

        # Using the append() method
        newList=[]
        for i in list:
            newList.append(i)
        print("Newly copied list using list comprehension and append is ", *newList)

        # Using the copy() method
        copyList = list.copy()
        print("Newly copied list using copy method is ", *copyList)

        # Using the method of Deep Copy
        copyList = copy.deepcopy(list)
        copyList[3] = 7
        print("Original List:", *list)
        print("Deep Copy List:", *copyList)


    # Python | Count occurrences of an element in a list
    
    # Python | Remove empty tuples from a list
    # Python | Program to print duplicates from a list of integers
    # Python program to find Cumulative sum of a list
    # Python | Sum of number digits in List
    # Break a list into chunks of size N in Python
    # Python | Sort the values of first list using second list

list = [0, 65, -19,3, 90, 12, -35, 9, -2, 56, 24]
list1 = [23, 65, 19,3, 90, 12, 35, 9, 56, 24]
obj=ListPrograms()
obj.SwapListElements(list)
obj.SwapPositions(list,1,3)
obj.LengthOfList(list)
print(f"Is 3 present in the list {list}: {obj.IsElementExist(list, 3)}")
print(f"Is 8 present in the list {list}: {obj.IsElementExistinList(list, 8)}")
obj.ClearList(list1)
obj.ReverseList(list)
obj.SumOfElementsList(list)
obj.MultiplyList(list)
obj.SmallestNumberInList(list)
obj.LargestNumberInList(list)
obj.SecondLargestNumber(list)
obj.FindNlargestElements(list, 3)
obj.EvenNumbersInList(list)
obj.OddNumbersInList(list)
obj.EvenNumberInRange(4,15)
obj.OddNumberInRange(4,15)
obj.PositiveNumbers(list)
obj.NegativeNumbers(list)
obj.AllPositiveNumbersInRange(-5,5)
obj.AllNegativeNumbersInRange(-5,5)
obj.RemoveMultipleElement()
obj.RemoveEmptyList()
obj.CopyList(list)

