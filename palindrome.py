## to check if the input string is a palindrome or not 
def palindrome():
    user = input("Please enter a string").lower()
    reversed_string = user[::-1]
    print("reversed_string", reversed_string)

    if user == reversed_string:
        print("the input string is a palindrome")

    else:
        print("The input string is not a palindrome")

palindrome()


