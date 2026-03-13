#encapsulation
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

emp1 = Employee("Alice", 50000)
print(emp1.get_name())  # Output: Alice

print(emp1.get_salary())  # Output: 50000

#inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def intro(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old and my student ID is {self.student_id}."
    
student1 = Student("Bob", 20, "S12345")
print(student1.introduce())  # Output: Hello, my name is Bob, I am 20 years old.
print(student1.intro())  # Output: Hello, my name is Bob, I am 20 years old and my student ID is S12345.


#polymorphism
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
print(circle.area())  # Output: 78.5
print(rectangle.area())  # Output: 24


class EmailNotification:

    def send(self, message):
        print("Sending Email:", message)


class SMSNotification:

    def send(self, message):
        print("Sending SMS:", message)


def notify(notification, message):
    notification.send(message)


email_notification = EmailNotification()
sms_notification = SMSNotification()

notify(email_notification, "Hello via Email!")
notify(sms_notification, "Hello via SMS!")

#abstract class

from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def connect(self):
        pass


class MySQLDatabase(Database):

    def connect(self):
        print("Connecting to MySQL")


class PostgresDatabase(Database):

    def connect(self):
        print("Connecting to PostgreSQL")

mysql_db = MySQLDatabase()
postgres_db = PostgresDatabase()
mysql_db.connect()  # Output: Connecting to MySQL
postgres_db.connect()  # Output: Connecting to PostgreSQL
