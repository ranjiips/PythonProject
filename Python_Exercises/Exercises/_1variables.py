name="Ranjith"
gender="Male"
fname="Ranjith"
a="nyc"
a=123
xxx=''

def print_values():
    print("===================== Print Statements =====================")
    print(name)
    xxx="ccc"
    print(xxx)

def arthimetic_operations():
    print("===================== Addition =====================")
    b=a
    c=20
    add=b+c
    print(f"{b} + {c} = {add}")
    print("===================== Subtraction =====================")
    sub=c-b
    print(f"{c} - {b} = {sub}")
    print("===================== Multiplication =====================")
    mul=a*b
    print(f"{a} * {b} = {mul}")
    print("===================== Division =====================")
    div=c/b
    print(f"{c} / {b} = {div}")
    print("===================== Quotient =====================")
    quotient=c//b
    print(f"{c} // {b} = {quotient}")
    print("===================== Remainder =====================")
    remainder=b%c
    print(f"{b} % {c} = {remainder}")
    print("===================== Exponents =====================")
    exponents = 2**3
    print(f"{2} ** {3} = {exponents}")
    print("===================== Order_of_precedence =====================")
    order_of_precedence = (2+6)*(6*4)/4
    print(f"order_of_precedence for (2+6)*(6*4)/4 is {order_of_precedence}")

def boolean_operations():
    print("===================== Boolean_operations =====================")
    print(bool(0))
    print(bool(1))
    print(bool(0.5))
    a=True
    print(bool(a))

def using_format():
    print("===================== Print using formats =====================")
    a,b,c=5,4,6
    d=e=f=10
    print('a={} b={} c={}'.format(a,b,c))
    print('d={} e={} f={}'.format(d,e,f))

def get_index_of_sum():
    numbers=[6, 8, 11, 6, 7, 18]
    value=17
    print(f"Number list: {numbers}")
    for i in range(0, len(numbers)-1):
            if(numbers[i]+numbers[i+1]==value):
                print(f"Index1 = {i}, Index2 = {i+1}")


print_values()
a=True
a=(5)
print(f"Type of variable a-{a} is {type(a)}")
arthimetic_operations()
boolean_operations()
using_format()

# num = [6,8,11,6,7,18]
get_index_of_sum()