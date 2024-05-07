import random


# number = int(input("Enter a number to guess"))

rand_number = random.randint(1,10)
def guess():
    for i in range(5):
        number = int(input("Enter a number to guess: "))
        if number < rand_number:
            print(number, "entered number is less, guess greater number")
        elif number > rand_number:
            print(number,"number is greater, guess smaller number")
        else:
            print(number, "You have guessed number correctly")
            

        if i == 5:
            print('you exceed you limit try again')
            
            try_again = input("enter 'y' for try again and 'n' for end")
        
            if try_again == 'y':
                guess()
            else:
                print("thank you")
guess()
# for i in range(5):
#     number = int(input("Enter a number to guess: "))
#     if number < rand_number:
#         print(f"entered number {number} is less, guess greater number ")
#     elif number > rand_number:
#         print(f"entered number {number} is greater, guess smaller number")
#     else:
#         print(f"You have guessed number correctly {rand_number}")
#         break

# else:
#     print("Try again")
            




    
        
       
    

