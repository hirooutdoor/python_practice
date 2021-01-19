# %%
year = int(input("Which year do you want to check?"))
msg_f = "This is not Leap Year!"
msg_t = "This is Leap Year!"


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:    
            print(msg_t)
        else:
            print(msg_f)
    else:
        print(msg_t)
else:
    print(msg_f)

# %%
