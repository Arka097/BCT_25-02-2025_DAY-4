# user driven program to find fibonacci, prime or factorial using function overloading

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

def is_prime(n):
    if n < 2:
        print("Not Prime")
        return
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            return
    print("Prime")

choice = int(input("Enter 1 for Fibonacci, 2 for Factorial, 3 for Prime: "))
num = int(input("Enter a number: "))

if choice == 1:
    fibonacci(num)
elif choice == 2:
    factorial(num)
elif choice == 3:
    is_prime(num)
