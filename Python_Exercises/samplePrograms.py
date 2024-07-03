import argparse


def get_number():
    myList = [1,3,5,8,4,2,3,6,9,0]
    num = 2
    for i in myList:
        num+=1
    print("The number is "+str(num))

def func(x,y):
    x+y
    return x

def print_fish(*fish):
    for f in fish:
        print("Fish: "+str(f))

def parsing_concept():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    args = parser.parse_args()
    print("Hello", args.name)

def variable_declaratioon():
    x=13
    print(x==13)
    print(x!="13")
    print(x=="13")





get_number()
print_fish("Pike", "Clown", "Puffer")
func(3,6)
parsing_concept()
variable_declaratioon()