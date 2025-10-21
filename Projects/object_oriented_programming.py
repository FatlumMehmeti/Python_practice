#Create a class called Car with attributes brand, model, and year. Add a method start() that prints a message like "The car has started".
class Car:
    def __init__(self,brand,model,year):
        self.__brand=brand
        self.__model=model
        self.__year=year
    def start(self):
        print(f"The car has started of \n Brand: {self.__brand},\n Model: {self.__model},Year: {self.__year}")    
#obj=Car('www','ggg','2025')
#obj.start()

#Create a class Rectangle that has methods to calculate its area and perimeter.
class Rectangle:
    def __init__(self,l,w):
        self.__l=l
        self.__w=w
    def area(self):
        return self.__l *self.__w
    def perimeter(self):
        return 2*(self.__l+self.__w) 
#ob=Rectangle(1,3)
#print(f'The area is: {ob.area()} \nThe perimeter is: {ob.perimeter()}')           
#Create a class BankAccount with methods to deposit, withdraw, and check balance. Prevent withdrawing more than the current balance.
class BankAccount:
    def __init__(self,amount):
        self.__amount=amount
    def deposit(self,n):
        self.__amount+=n
        return self.__amount


    def withdraw(self,n): 
        if self.__amount==0:
            return 'you dont have any credits'
        elif self.__amount-n<0:
            return 'not enogh amount to do the transaction'
        self.__amount-=n 
        return f'Transaction success'

    def balance(self):
        return self.__amount      
#ob=BankAccount(1000)
#print(ob.deposit(20))
#print(ob._BankAccount__amount)    
#print(ob.withdraw(1000))  
#print(ob.withdraw(20))  
#print(ob.withdraw(20))  
#print(ob.balance())
#Create a class Person with attributes name and age. Then create a subclass Student that also has an attribute student_id.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'Name: {self.name}, Age: {self.age}')    
class  Student(Person):
        def __init__(self, name, age,student_id):
             super().__init__(name, age)  
             self.student_id=student_id
        def display(self):
            print(f'Name: {self.name}, Age: {self.age},StudentID:{self.student_id}')                
p = Person("Alice", 30)
print("--- Person Info ---")
p.display()
s = Student("Bob", 22, "S1001")
print("\n--- Student Info ---")
s.display()

#Write a class Temperature with a method to convert Celsius to Fahrenheit and vice versa.
class Temperature:
    def __init__(self,v,scale='C'):
        self.v = v
        self.scale = scale.upper()
    def celsius_to_fahrenheit(self):
        if self.scale == 'C':
            return (self.v * 9/5) + 32
        elif self.scale == 'F':
            return self.v
        else:
            raise ValueError("Invalid scale. Use 'C' or 'F'.")
    def fahrenheit_to_celsius(self):
        if self.scale == 'F':
            return (self.v - 32) * 5/9
        elif self.scale == 'C':
            return self.v
        else:
            raise ValueError("Invalid scale. Use 'C' or 'F'.")

