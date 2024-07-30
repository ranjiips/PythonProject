class arithmetic_operation():
    def add(self,num1,num2):
        print("===================Addition======================")
        print(num1,'+',num2,'=',num1 + num2)

    def sub(self,num1,num2):
        print("===================Subration======================")
        print(num1-num1,'-',num2,'=',num1-num2)

    def mul(self,num1,num2):
        print("===================Multipilicatio======================")
        print(num1,'*',num2,'=',num1*num2)

    def div(self,num1,num2):
        print("===================Division================")
        print("Division:",num1,'/',num2,'=',num1/num2)

obj=arithmetic_operation()
obj.add(10,20)
obj.sub(40,30)
obj.mul(2,4)
obj.div(45,10)