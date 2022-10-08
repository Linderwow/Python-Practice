n = int(input("Check this number: "))


def prime_checker(number):
    is_Prime = True
    for i in range(2, number):
        if number % i == 0:
            is_Prime = False
    if is_Prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


prime_checker(number=n)
