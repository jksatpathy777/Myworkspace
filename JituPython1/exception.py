import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Invalid Input, Hello or string Can not be converted to integer")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Can not divide by zero")
    sys.exit(1)

print(f"{x} / {y} = {result}")

#using result=x/y incase if anyone enter y=0 it throws ZeroDivisionError exception- Solve this by using try: & except
#this ZeroDivisionError can be handled by importing 'sys' & using 'try' and 'except'
# Similarly if any one type a string like 'Hello' in place of integer you will get 'ValueError' which can be handled in same way as shown