

def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        print(f"number: {number} values,i:{i} number mod i: {number % i}")
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")




n = int(input("Check this number: "))
prime_checker(number=n)