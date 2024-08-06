

def print_headers(header):
    print(30*"*"+header+20*"*")
def list_accessing_elements():
    print_headers("list and accessing the elements")
    cars=['Tata','Maruti','Kia','Honda','Hyundai']
    print(cars)
    print(cars[2])
def list_actions():
    print_headers("List functions")
    list=[]
    list.append(1)
    list.append(2)
    list.append("text")
    print(list)
    list.insert(1,"venkat")
    print(list)

def number_lists():
    print_headers("Number list operations")
    num_list=[9,2,7,6,8,0,8,5,4,7,9,8]
    num_list.append(12)
    sum=num_list[2]+num_list[4]
    print(sum)
    print('Original list: '+str(num_list))
    num_list[5]=11
    print('List after change the value in 5th index: '+str(num_list))
    cc=num_list.count(8)
    print("Number of time value 8 occurs in list: "+str(cc))

    print("Length  of the list: "+str(len(num_list)))
    print("*"*20)

    #find the index of the object from the list
    print('Original list: '+str(num_list))
    x=num_list.index(8)
    print("Return index of 8(1st occurance): "+str(x))

    #remove the vaue from list
    x=num_list.pop()    #remove the last value
    print("Last Value removed: " + str(x))
    x=num_list.pop(4)    #remove the last value
    print("removed value from the index 4: " + str(x))

    print('New list: '+str(num_list))
    num_list.remove(11)     #removes given  value from list
    print("List after remove 11: "+str(num_list))
    num_list.sort()
    print("Ascending Order: "+str(num_list))
    num_list.sort(reverse=True)
    print("Descending Order: "+str(num_list))
    num_list.reverse()
    print("Print list in reverse Order: "+str(num_list))
    print("*"*20)

def slicing_the_list():
    print_headers("Slicing the List")
    cars=['Tata','Maruti','Kia','Honda','Hyundai']
    slicing=cars[:]
    print(slicing)
    slicing=cars[2:]
    print(slicing)
    slicing=cars[:3]
    print(slicing)
    slicing=cars[2:4]
    print(slicing)
    slicing=cars[::1]
    print(slicing)
    slicing=cars[::-1]
    print(slicing)
    slicing=cars[::2]
    print(slicing)
    slicing=cars[::-2]
    print(slicing)
    print("List: " + str(cars))

def dictionary_actions():
    print_headers("Dictionary:")
    name={'Name':'Ranjith','Age':35,'Gender':'Male'}
    print(name)
    print(name["Name"])
    print(name["Age"])
    print(name)
    aa=name
    aa['City']='Salem'
    aa['Country']='India'
    print(aa)
    age_after_five_years = aa['Age']+5
    print(age_after_five_years)

    aa['Age'] = aa['Age']+5
    print(aa['Age'])
    print(aa)
    print('Dictionary: ' + str(aa))
def nested_dictionary():
    print_headers("Nested Dictiionary and Dictionary methods")

    person_details={"Ranjith":{'Age':35,'Gender':'Male'},'Priya':{'Age':30,'Gender':'Female'}}
    print(person_details)
    print(person_details['Ranjith'])
    print(person_details['Priya']['Gender'])
    print((person_details["Ranjith"]["Gender"]))

    print("Dictionary Methods")
    print(person_details.keys())
    print(person_details.values())
    print(person_details["Ranjith"].keys())
    print(person_details["Ranjith"].values())
    print(person_details.items())
    persons=person_details.copy()
    print(persons)
    persons=persons.clear()
    print(persons)
    persons=person_details["Priya"].copy()
    print(persons)
    persons1=persons.pop("Age")
    print(persons1)
    print(persons)

def tuple_functions():
    cars = ['Tata', 'Maruti', 'Kia', 'Honda', 'Hyundai']
    print('Tuple')
    print("List: "+str(cars))
    my_tuple=(1,2,3,'Ranjith','35',2021,2,2)
    print("Tuple: "+str(my_tuple))
    print(my_tuple[1])
    print_headers("slicing the tuple")
    slicing=my_tuple[:]
    print(slicing)
    slicing=my_tuple[2:]
    print(slicing)
    slicing=my_tuple[:3]
    print(slicing)
    slicing=my_tuple[2:4]
    print(slicing)
    slicing=my_tuple[::1]
    print(slicing)
    slicing=my_tuple[::-1]
    print(slicing)
    slicing=my_tuple[::2]
    print(slicing)
    slicing=my_tuple[::-2]
    print(slicing)
    print(my_tuple)
    print(my_tuple.index('Ranjith'))
    print(my_tuple.count(2))
    print('Tuple: '+str(my_tuple))

list_accessing_elements()
list_actions()
number_lists()
slicing_the_list()
dictionary_actions()
nested_dictionary()
tuple_functions()