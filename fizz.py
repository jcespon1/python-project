##The Fizz Buzz problem is a simple programming exercise where you 
# print numbers from 1 to 100, but replace multiples of 3 with "Fizz" and 
# multiples of 5 with "Buzz"

for x in range(1,101):
    if (x % 3 == 0) and (x % 5 == 0):
        print("FizzBuzz")
    elif (x % 3 == 0):
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)
