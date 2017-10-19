def FizzBuzz(a,b):
    """
    This function works like this:
    First, input the range.
    If the number is divisible by 3, it prints “Fizz”
    If the number is divisible by 5, it prints “Buzz”
    If the number is divisible by both 3 and 5, it prints “FizzBuzz”
    Otherwise, it prints the number.
    """

a = int(input("Low value: "))
b = int(input("High value: "))

for n in range(a,b+1,1):
    if (n % 3 == 0) and (n % 5 != 0):
        print("Fizz")
    elif (n % 3 !=0) and (n % 5 == 0):
        print("Buzz")
    elif (n % 3 == 0) and (n % 5 == 0):
            print("FizzBuzz")
    else:
            print(n)
FizzBuzz(a,b)
