try:
    print("outer try block")
    n = int(input("enter a number"))
    print(10/n)
    try:
        print("inner try")
        print("sarb"+"jeet")
    except TypeError as e:
        print("Hello")
    else:
     print("inner no exception")
except ArithmeticError as e:
     print(10/5)
else:
     print("outer no excepiton")
finally:
    print("finally block")
