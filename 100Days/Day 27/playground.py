

# Los datos de args son guardados en tuplas
def args_(*args):
    squares = []
    for i in args:
        squares.append(i)
    squares = sum(squares)
    print(squares)

# args_(1,2,3,4,5,4)


def kwargs_(n,**kwargs):
    print(kwargs)
    # for key, values in kwargs.items():
    #     print(key, values)
    n *= kwargs['number1']
    print(n)

# kwargs_(3,number1=4, number2=5)

# Para los **kwargs, podemos almacenar varias funciones en una clase y solo llamar las que querramos
class Car:
    def __init__(self, **kwargs):
        self.brand = kwargs.get('brand')
        self.colour = kwargs.get('colour')
        self.model = kwargs.get('model')
        self.seats = kwargs.get('seats')



my_car = Car(model='Tahoe', seats=7)
print(my_car.seats)