def cal(op):
    if(op =='+'):
        print("The Addition of two Number are ",x+y)
    elif(op == '-'):
        print("The Subtraction of Two Number are ",x-y)
    elif(op == '*'):
        print("The Multiplication of Two Number Are ",x*y)
    elif(op == '/'):
        print("The Division of two Number are ",x/y)
    elif(op == '%'):
        print("The Modulation Of Two Number are ",x%y)        
x = int(input("Enter The Number x\n"))
y = int(input("Enter The Number y\n"))
dict1 = {
    "Addition" : "+",
    "Subtraction" : "-",
    "Division" : "/",
    "Multiplication":"*",
    "Modulo":"%"
}
print(dict1)
op1 = input("Enter The Operation you Want To perform\n")
cal(op1)
