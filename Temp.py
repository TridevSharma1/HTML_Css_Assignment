print("Test")
print("hello")
print("welcome to python programming")
# opprator
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
# oops 
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print(f"Car make: {self.make}")
        print(f"Car model: {self.model}")
        print(f"Car year: {self.year}")
my_car=Car("Toyota","Camry",2020)
my_car.display_info()

# fabonacci series
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
n = 10
print(f"Fibonacci sequence up to {n} terms: {fibonacci(n)}")
 
# palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]  # Check if the string is equal to its reverse
word = "madam"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

print("End of the program")

# This code demonstrates basic Python programming concepts, including printing output, performing arithmetic operations, defining a class and its method, generating a Fibonacci sequence, and checking for palindromes. Each section of the code serves a specific purpose, showcasing different aspects of Python programming.

print("This is the end of the code snippet.")
# class Person:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
person1 = Person("Alice", 30)
person1.display_info()
