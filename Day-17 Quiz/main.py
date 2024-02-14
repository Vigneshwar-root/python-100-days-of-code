# class Cars:
#     def __init__(self, seats, brand): #Every time I create a new object this init function will be called
#         self.seats = seats
#         self.brand = brand
    

# car_1 = Cars(5,"Kia")
# print(car_1.brand)

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1 

user_1 = User("001","Angela Yu")
user_2 = User("002", "Alan")
user_3 = User("003","Bruce Wills")

user_1.follow(user_2)
user_1.follow(user_3)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
print(user_3.followers)
print(user_3.following)




