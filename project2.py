def calculate (fnum,snum,operation = '+') :
    if operation == '+' or operation.lower() == 'add' or operation.lower() == 'a' :
        return fnum + snum 
    elif operation == '-' or operation.lower() == 's' or operation.lower() == 'subtract' :
        return fnum - snum
    elif operation == '*' or operation.lower() == 'm' or operation.lower() == 'multiply' :
        return fnum * snum
    elif operation == '**' or operation.lower() == 'p' or operation.lower() == 'power' :
        return fnum **snum
    elif operation == '/' or operation.lower() == 'd' or operation.lower() == 'devide' :
        return fnum / snum
    elif operation == '%' or operation.lower() == 'mod' or operation.lower() == 'modlus' :
        return fnum / snum
    else :
        print("Invalid Operation !! ")
        


print("Welcome To My simple Calculator ....")

num1 = int(input("Enter First Number").strip())
num2 = int(input("Enter Seconed Number").strip())

op = input("Enter Operation You Want..").strip()

print(f"The Result of Operation {num1} {op} {num2} = {calculate(num1,num2,op)}")