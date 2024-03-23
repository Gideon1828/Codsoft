def calculator():
    n1=float(input("Enter a First Number:"))
    n2=float(input("Enter a SecondNumber:"))
    op=input("Enter Operation(+ , - , * , / , %)")
    if op=='+':
        result=n1+n2
    elif op=='-':
        result=n1-n2
    elif op=='*':
        result=n1*n2
    elif op=='%':
        result=n1%n2
    elif op=='/':
        if n2!=0:
            result=n1/n2
        else:
            print("Error:Division by Zero")
            return
    else:
        print("Invalid Operation")
        return
    print("Result:",result)
calculator()                            