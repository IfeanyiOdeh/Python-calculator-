def calculator():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))


    print(" Available operations" )
    print( "a is addition          s is subtraction")
    print(" m is multiplication    d is division")
    print(" e is Modulus           f is End")
    while True:
        operation = input('what operation do you want to perform: ')
        if operation == "a":
            print(a + b)
        if operation == "s":
            print(a - b)
        if operation == "m":
            print(a * b)
        if operation == "d":
            print(a / b)
        if operation == "e":
            print(a % b)
        if operation == "f":
            break





(calculator())
