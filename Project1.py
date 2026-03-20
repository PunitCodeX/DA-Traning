#simple calculator

num1 = int(input("enter a number :"))
num2 = int(input("enter a number :"))
op = input(" choose the operation[+,-,*,/] :")
if op =='+':
     print("result :", num1 + num2)
elif op == '-':
      print("result :", num1 - num2)
elif op == '*':
      print("result :", num1 * num2)
elif op == '/':
    if num2 != 0:
        
      print("result :", num1 /num2)
    else :
        print("error : division by zero!")
else:
    print("invalid operation")
