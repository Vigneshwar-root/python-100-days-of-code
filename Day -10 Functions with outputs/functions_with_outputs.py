def my_function():
    return 3 * 2

def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "you did not provide valid inputs."
    # f_name[0] = f_name[0].upper()
    # return f"{f_name.capitalize()} {l_name.capitalize()}"
    return f"{f_name.title()} {l_name.title()}"

print(my_function())
print(format_name(input("What is your first name?"),input("What is your last name ")))


