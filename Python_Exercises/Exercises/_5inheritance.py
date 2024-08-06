class Fruits(object):
    def __init__(self, name, vitamin):
        self.name = name
        self.vitamin = vitamin
        print('Initialize the parent class 1 variables')

    def nutrition(self):
        print('Vitamin: {}'.format(self.vitamin))
        print('Nutrition method from the parent class')

class Fruit_Shape(object):
    def __init__(self,shape):
        print('Initialize the parent class 1 variables')
        self.shape=shape

    def fruit_shape(self):
        print('Fruit Shape: {}'.format(self.shape))

class Fruit_Details(Fruits,Fruit_Shape):
    def __init__(self, name, vitamin, shape, color):
        Fruits.__init__(self, name, vitamin)
        Fruit_Shape.__init__(self,shape)
        print('Initialize the child class variables')
        self.color = color

    def nutrition(self):
        super(Fruit_Details, self).nutrition()
        # print('Nutrition method from the child class')

    def fruit_color(self):
        print('Fruit Color: {}'.format(self.color))

class Fruits_Orgin(Fruit_Details):
    def __init__(self, name, vitamin, shape, color,origin):
        Fruit_Details.__init__(self, name, vitamin, shape, color)
        self.origin=origin

    def origin_of_fruit(self):
        print('Origin of the {} is: {}'.format(self.name,self.origin))




# fruit=Fruit_Details('Apple','B12','Oval','Red')
# print('Fruit Name: {}'.format(fruit.name))
# fruit.nutrition()
# fruit.fruit_color()
# fruit.fruit_shape()

fruit=Fruits_Orgin('Apple','B12','Oval','Red','America')
print('Fruit Name: {}'.format(fruit.name))
fruit.nutrition()
fruit.fruit_color()
fruit.fruit_shape()
fruit.origin_of_fruit()

