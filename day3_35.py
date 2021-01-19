# %%
"Hirofumi".lower()
# %%
"Hirofumi".count("h")
# %%
lower_case_name = "Hirofumi".lower()
lower_case_name.count("h")
# %%
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_str = name1 + name2

lower_case_name = combined_str.lower()

t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

true = t + r + u + e

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

love = l + o + v + e

str_love_score = str(true) + str(love)
love_score = int(str_love_score)

print(love_score)

if (love_score) < 10 or (love_score) > 90:
    print(f"Your love score is {love_score}, you go together like Coke and Mentos.")
elif (love_score) <= 50 and (love_score) >= 40:
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}. Hummmm, not really but.")
# %%
