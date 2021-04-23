import random

# Guess the price

# Give a radom price between 0 and 100
price = int(random.random() * 100);

user_price = int(input())
while user_price != price:
    if user_price > price:
        print("lower")
    else:
        print("upper")

    user_price = int(input())


print("Congratulation")

