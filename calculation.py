print('''
+ For Addition
- For Subtraction
* For Multiplication
/ For Divide
''')
a=eval(input("Enter The First Number:-"))
b=eval(input("Enter The Second Number:-"))
operation=input("What operation you want to perform:-")
if operation=="+":
    print(a+b)
elif operation=="-":
    print(a-b)
elif operation=="*":
    print(a*b)
elif operation=="/":
    print(a/b)
else:
    print("Invalid Operation......")
