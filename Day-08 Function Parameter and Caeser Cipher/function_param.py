def greet(name):
    print(f"Hello {name}")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet("Jack")
greet("Bob")

def greet_with_name(first_name,last_name):
    print(f"Hello {first_name} {last_name}")

greet_with_name("Iron","man")  #postitional arguments
greet_with_name(last_name="Iron",first_name="man") #keyword arguments