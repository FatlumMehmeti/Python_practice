# Write a program that takes a user’s name and age, then prints a message saying how old they will be in 10 years.
def years(name,age):
    future_age = age + 10
    print(f"Hello {name}, in 10 years you will be {future_age} years old.")
# Write a program that converts a temperature from Celsius to Fahrenheit.
def celsious_to_fahrenheit(c):
    return (c*9/5)+32
def fahrenheit_to_celsius(f):
    return (f-32)*5/9    
# Write a function that checks if a number entered by the user is positive, negative, or zero.
def check():
    a=''
    try:
        s=int(input("Enter a number: "))
        if s<0:
            a+= "negative"
        else:
            a+= "positive"    
        return a    
    except Exception as e:
        print(f"You made a mistake try again......")
        return check()
    except:
        print("no idea")   
       
# Write a program that counts how many vowels are in a given string.
def count_vowels(s):
    s = s.lower()
    count =0
    for i in range(len(s)):
        if s[i] in ['a','e','i','o','u']:
            count += 1    
    return count
#print(count_vowels("AJONI"))        
# Write a program that prints all numbers from 1 to 50, but for multiples of 3 print "Fizz", for multiples of 5 print "Buzz", and for multiples of both print "FizzBuzz".
def print_numbers():
    s=''
    for i in range(1,51):
        if i%3==0 and i%5==0:
            s+='FizzBuzz'
        elif i%3==0:
            s+='Fizz'
        elif i%5==0:
            s+='Buzz'
        else:
            s+=str(i)   
    return s         
#print(print_numbers())