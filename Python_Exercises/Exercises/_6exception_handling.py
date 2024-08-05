"""
Exception handling
"""
class DividendsSmallError(Exception):
    pass

class HandlingException(object):

    def __init__(self,num1,num2):
        print('Initialize Parent Class member variables')
        self.num1=num1
        self.num2=num2

    def divide_two_numbers(self):
        print('Parent method')
        try:
            if self.num1<self.num2:
                raise DividendsSmallError
            num3=self.num1/self.num2
        except ZeroDivisionError:
            print('Divide by Zero Exception')
        except DividendsSmallError:
            print('Dividend is smaller than Divisor')
        except Exception as e:
            print('Exception Occured:\n'+str(e))
        else:
            print('Result: {}'.format(num3))
        finally:
            print('This is finally block')

class MathematicalOperations(HandlingException):

    def __init__(self, number1, number2):
        HandlingException.__init__(self,number1,number2)
        # print('Initialize child Class member variables')

    def divide_two_numbers(self):
        super(MathematicalOperations, self).divide_two_numbers()
        print('Child Class method')
        try:
            if self.num1<self.num2:
                raise DividendsSmallError
            num3=self.num1/self.num2
        except ZeroDivisionError:
            print('Divide by Zero Exception')
        except DividendsSmallError:
            print('Dividend is smaller than Divisor')
        except Exception as e:
            print('Exception Occured:\n'+str(e))
        else:
            print('Result: {}'.format(num3))
        finally:
            print('This is finally block')

class Exception_Handling_Excersie(object):
    def __init__(self):
        self.car={'make':'Honda','model':'i10','year':'2020'}

    def get_car_value(self,key):
        try:
            print(test.car[key])
        except:
            print('The given key {} is not defined'.format(key))
        finally:
            print('Car data: {}'.format(self.car))


# divide=HandlingException(6,7)
# divide.divide_two_numbers()
# maths=MathematicalOperations(8,7)
# maths.divide_two_numbers()
test=Exception_Handling_Excersie()
test.get_car_value('color')

