first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
operational_sign = input("Sign: ")

if operational_sign=="+":
    print("The answer is : "+str(first_number+second_number))

if operational_sign=="-":
    print("The answer is : "+str(first_number-second_number))

if operational_sign=="x":
    print("The answer is : "+str(first_number*second_number))

if operational_sign=="/":
    print("The answer is : "+str(first_number/second_number))