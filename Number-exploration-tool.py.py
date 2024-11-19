user = input("enter your name;")
num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))
print(f"Hello, {user}, Let's explore your favorite numbers:")
if num1 % 2 == 0:
  print(f"{num1} is even.")
else:
  print(f"{num1} is odd.")

if num2 % 2 == 0:
  print(f"{num2} is even.")
else:
    print(f"{num2} is odd.")
if num3 % 2 == 0:
  print(f"{num3} is even.")
else:
  print(f"{num3} is odd.")
sum = num1 + num2 + num3
print("the sum of the numbers are:",sum)
if sum % 2 == 0:
  print(f"wow,{sum} is even number.")
else:
  print(f"wow,{sum} is prime number.")
