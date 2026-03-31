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

