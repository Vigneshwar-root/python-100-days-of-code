enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemeies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope, global scope and Namespace

#no block scope

# game_level = 3
# enemies = ["Skeleton","Zombie","Alien"]
# if game_level > 5:
#     new_enemy = enemies[0]
# print(new_enemy)



#modifying a global variable

enemies = 1

def increase_enemies():
    global enemies
    enemies += 2
    print(f"enemeies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# general rule avoid modifying global scope in python
print("using return statement to avoid global scoping issue")

def increase_enemies(): 
    print(f"enemeies inside function: {enemies}")
    return enemies + 2
    
enemies = 1



enemies = increase_enemies()
print(f"enemies outside function: {enemies}")