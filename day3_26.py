# %%
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill += 7
        print("Child tickets are $7.")
    elif age <= 18:
        bill += 10
        print("Youth tickets are $10.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    answer = input("Do you want a photo taken? $3 Y or N.")
    if answer == "Y":
        bill += 3
        
    print(f"So your totall bill is ${bill}. ")
else:
    print("Sorry, you have to grow taller before you can ride.")
# %%
