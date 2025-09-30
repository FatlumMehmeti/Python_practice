# secret_number = 777  # the magician’s secret number

# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """
# )

# guess = int(input("Enter your guess: "))

# while guess != secret_number:
#     print("Ha ha! You're stuck in my loop!")
#     guess = int(input("Enter your guess: "))

# print(secret_number)
# print("Well done, muggle! You are free now.")
for i in range(1,1):
    print("The value of i is currently", i)
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.
for i in range(5):
    print(str(i+1)+" Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")


# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")


largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

while True:
    word=input("Enter a word diffrent from chupacabra:  ")
    if(word=="chupacabra"):
        print("You've successfully left the loop.")
        break
    print(word)
    

    # Prompt the user to enter a word
# and assign it to the user_word variable.
user_word=input("Enter a Word").upper()

for letter in user_word:
    # Complete the body of the for loop.
    if (letter == "A") or (letter == "E") or (letter == "I") or (letter == "O") or (letter == "U"):
        continue
    print(letter)

blocks = int(input("Enter the number of blocks: "))

height = 0
layer = 1

while blocks >= layer:
    blocks -= layer
    height += 1
    layer += 1

print("The height of the pyramid:", height)

c0=int(input())
steps=0
while c0!=1:
    if c0%2==0:
        c0//=2
    else:
        c0=3*c0+1
    print(c0)
    steps+=1
    
print("Steps: ",steps)    