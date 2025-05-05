## Create a program that takes a password from the user and checks how strong it is based on certain rules.
def check_password_strength():
    password = input("please enter a password")
    strength = 0 # to track the score
    if len(password) >= 7:
        if any(char.isupper() for char in password):
            strength += 1
            
        if any(char.islower() for char in password):
            strength += 1
        
        if any(char.isnumeric() for char in password):
            strength += 1

        if any(not char.isalnum() for char in password):
            strength += 1

    else:
        print("password too short")
    if strength == 4:
        print("very strong password")
    elif 2< strength <= 4:
        print("Moderately strong password")
    else:
        print("password not strong enough")

check_password_strength()



    

        


