# number guessing
 
import random

while True:
    system_num=random.randint(0,100)
    print("Correct Number is:",system_num,"Your number is ",input_num)
    input_num=int(input("Enter Your Number:"))
    if input_num<system_num:
        print("Your number is too less")
    elif input_num>system_num:
        print("Your number is too high")
    else:
        print(f"Congratulations! You guessed the correct number {system_num}")

