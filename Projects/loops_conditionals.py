#Write a function that takes a list of integers and returns a new list with only the even numbers.
def even(a):
    t=[]
    for i in a:
        if i%2==0:
            t.append(i)
    return t
#print(even([1,2,3,4,5,6,7,8,9,0]))

#Write a function that calculates the factorial of a number using a for loop.
def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
def factorial_1(n):
    res=1
    for i in range(n+1):
        if i==0:
            continue
        res=res*i
    return res
#print(factorial_1(5))    
#Write a program that prints the multiplication table (1–10) for a number entered by the user.
def multi(n):
    for i in range(1,11):
        print(f"{n} * {i} = {i*n} ")
#multi(4)        
#Write a program that reverses a string without using Python’s built-in reverse functions.
def revers(t:str):
    rev=''
    u=(len(t)-1)
    for  i in range(len(t)):
        rev+=t[u-i]
    return rev
#print(revers("nuk e di"))
#s="nuk e di"
#print(s[::-1])
#Write a program that asks the user to enter 5 numbers and prints the largest and smallest ones.
def enter():
    print("Enter 5 numbers")
    max,min=None,None
    for i in range(5):
        en=int(input(f" Number {i+1} : "))
        if i==0:
            max,min=en,en
        if(max<en):
            max=en
        if(min>en):
            min=en     
    print(f"The largest number you gave is {max} and the smallest number is {min}")        
#enter()