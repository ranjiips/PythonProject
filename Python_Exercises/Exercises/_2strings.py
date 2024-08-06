#strings in python
def string_concepts():
    a="Ranjith"
    b='Kumar'
    print(a)
    print(b)
    c="string with 'single quotes'"
    d='string with "double quotes"'
    print(c)
    print(d)
    e="string with \"double quotes\""
    f='string with \'single quotes\''
    print(f)
    g="string with single quote's"
    print(g)
    h="string written in multiple lines\
    but displaying in single line\
    continuing the line"
    print(h)
    print(50*"*")
    name="Ranjith"
    print(f"string manipulation for the value '{name}'")
    n=name[3]
    print("print 3rd index character: "+n)
    lname="Kumar"
    length=len(name)
    print("Name length: "+str(length))
    print("2nd character from reverse: "+name[length-2])
    print("Name in upper case: "+name.upper())
    print("Last name in lower case: "+lname.lower())
    print("Concatenation: "+name+" "+lname)

def replace_string():
    text="xdfghbgfhxdftfght"
    print("Replace string: "+text.replace("xdf","AAAA"))
    print("Replace string given instance: "+text.replace("xdf","AAAA",1))

def substring_slicing():
    text="xdfghbgfhxdftfght"
    print(f"Substring and slicing for the string '{text}'")
    sub=text[2]
    print(sub)
    sub=text[2:8]
    print(sub)  #fghbgfh   fbh
    sub=text[2:9:3]     #last number is skip the alternate value
    print(sub)

def slicing_and_Indexing():
    name="Ranjith"
    print(f"Slicing and Indexing for the string '{name}'")
    print(name[:])      #Ranjith
    print(name[2:])     #njith
    print(name[:3])     #Ran
    print(name[2:5])    #nji
    print(name[3])      #j
    print(name[-3])     #i
    print(name[:-2])    #Ranji
    print(name[::])     #Ranjith
    print(name[::2])    #Rnih

def reverse_the_string():
    name="Ranjith"
    print(f"Reverse the string '{name}'")
    print(name[::-1])   #htijnaR
    print(name[::-2])   #hinR
    print(name[::-3])   #hjR

def string_formatting():
    print(20*"*"+"String_Formatting"+20*"*")
    country="India"
    content="Enjoy well"
    a=10
    b=True
    string1="Welcome to Incredible "+country+"! "+content
    string2="Welcome to Incredible %s! %s %r %r"%(country,content,bool(a),b)
    print(string1)
    print(string2)
    print("I am from %s"%(country))
    print("I am from %s"%country)
    print(bool(a))

string_concepts()
replace_string()
substring_slicing()
slicing_and_Indexing()
reverse_the_string()
string_formatting()