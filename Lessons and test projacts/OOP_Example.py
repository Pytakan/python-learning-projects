import math
#encapsulation example in Python
class Email:
    def __init__(self,sender, recipient, subject, body):
        self.__sender = sender
        self.__recipient = recipient
        self.__subject = subject
        self.__body = body

    def send_email(self):
       pass # code to send email

    def display_email(self):
        pass # code to display email details
    # при помощи меодов изменяет значения приватных атрибутов но не даем прямой доступ к ним это и есть ИНКАПСУЛЯЦИЯ

#inheritance example in Python
class Vahicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        pass # code to start engine

    def stop_engine(self):
        pass # code to stop engine

class Car(Vahicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def open_trunk(self):
        pass # code to open trunk

    def close_trunk(self):
        pass # code to close trunk

class Motorcycle(Vahicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def pop_wheelie(self):
        pass # code to pop a wheelie
    
# При помощи наследования дочерние классы Car и Motorcycle получают все атрибуты и методы родительского класса Vehicle, 
# что позволяет переиспользовать код и создавать специализированные классы с дополнительными функциями.

#polymorphism example in Python
class Shape:
    def area(self):
        pass # Abstract method

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self): # тут мы переопределяем метод area из родительского класса Shape 
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self): # тут мы переопределяем метод area из родительского класса Shape 
        return math.pi* pow(self.radius,2)
# Полиморфизм позволяет использовать один и тот же интерфейс (метод area) для разных типов объектов (Rectangle и Circle),
# что упрощает работу с ними и делает код более гибким и расширяемым.


#abstraction example in Python
from abc import ABC, abstractmethod 
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass # Abstract method
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        pass # code to process credit card payment

class PayPalPayment(Payment):
    def process_payment(self, amount):
        pass # code to process PayPal payment
# Абстракция позволяет скрыть сложные детали реализации (как именно обрабатывается платеж)
# и предоставлять простой интерфейс (метод process_payment) для взаимодействия с различными
# с помощью декоратора @abstractmethod мы определяем абстрактный метод process_payment,
# который должен быть реализован в любых подклассах класса Payment.
 