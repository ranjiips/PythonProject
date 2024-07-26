import argparse

class sample():
    count = 0
    def __init__(self):
        sample.count +=1

    def get_number(self):
        myList = [1,3,5,8,4,2,3,6,9,0]
        num = 2
        for i in myList:
            num+=1
        print("The number is "+str(num))

    def func(self,x,y):
        x+y
        return x

    def print_fish(self,*fish):
        for f in fish:
            print("Fish: "+str(f))

    def parsing_concept(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--name')
        args = parser.parse_args()
        print("Hello", args.name)

    def variable_declaratioon(self):
        x=13
        print(x==13)
        print(x!="13")
        print(x=="13")

    def merge_two_list(self):
        country = ["India", "is"]
        statement = ["my", "country"]
        print(country[-1])
        print(country[::-1])
        print(country, statement)
        listval = country + statement
        print(listval)
        print(' '.join(listval))

    def merge_two_list_into_dictionary(self):
        list1 = ['a', 'b', 'c']
        list2 = [1, 2, 3]
        x = zip(list1, list2)
        print(list(x))
        dict1 = dict(zip(list1, list2))
        print(dict1)
        dict2 = {list1[i]: list2[i] for i in range(len(list1))}
        print(dict2)

    def get_duplicate_unique_char_from_list(self):
        country = ['India', 'is', 'my', 'country']
        str = ''.join(country)
        print(str)
        duplicates = []
        unique = []
        for char in str:
            if str.count(char)>1 and char not in duplicates:
                duplicates.append(char)
            if str.count(char)==1 and char not in unique:
                unique.append(char)
        print(duplicates)
        print(*unique)

    def get_words_starts_with_given_character(self):
        country = ['India', 'Is', 'My', 'Country']
        words = [word for word in country if word.startswith('I')]
        print(words)



obj1 = sample()
obj2 = sample()
obj3 = sample()
obj4 = sample()
obj1.get_number()
obj2.print_fish("Pike", "Clown", "Puffer")
obj3.func(3,6)
obj4.parsing_concept()
obj1.variable_declaratioon()
print(f"Object count: {sample.count}")
obj1.merge_two_list()
obj2.merge_two_list_into_dictionary()
obj3.get_duplicate_unique_char_from_list()
obj4.get_words_starts_with_given_character()