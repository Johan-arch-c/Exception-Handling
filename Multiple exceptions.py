try:
    num1,num2=eval(input("enter to numbers, seperated by a coma"))
    result=num1/num2
    print("result is", result)
except ZeroDivisionError:
    print("division by zero is error !!")
except SyntaxError:
    print("coma is missing. enter numbers seperated with coma like this 1,2")
except:
    print("wrong input")
else:
    print("no exeptions")
finally:
    print("this will execute no matter what")