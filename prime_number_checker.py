number = int(input("Enter a number: "))

# Check the prime number if the input > 1
def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number")
            break

    print("It's a prime number")

if number >= 0:
    if number <= 2:
        print("It's not a prime number")
    else:
        prime_checker(number)
else:
    print("Enter valid Integer")
