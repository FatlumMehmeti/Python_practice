#Write a function that takes a list of numbers and returns the second largest number.
def take(a:object):
    #a=sorted(a)
    #return a[-2]        
    max,max2=0,0
    for i in a:
        if max<i:
            max2=max
            max=i 
        if max>i>max2:
            max2=i       
    return max2        
#print(take([1,2,3,4,5,687,5,68,78,45,6]))        
#Write a function that returns the Fibonacci sequence up to n terms.
def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    s = [0, 1]
    for i in range(2, n+1):
        next_num = s[-1] + s[-2]
        s.append(next_num)
    return s
    #if n<=0:
    #    return[]
    #elif n==1:
    #    return [0]
    #elif n==2:
    #    return [0,1]
    #s=fib(n-1)
    #s.append(s[-1]+s[-2])
    #return s
#print(fib(15))
#Write a function that checks if two strings are anagrams of each other.
def anagram(s,t):
    if len(s) != len(t):
        return False

    s_count = {}
    t_count = {}

    for ch in s:
        s_count[ch] = s_count.get(ch, 0) + 1
    for ch in t:
        t_count[ch] = t_count.get(ch, 0) + 1

    return s_count == t_count            
#print(anagram('spar','rasp'))             
#Write a program that simulates rolling two dice until their sum equals 7, then prints how many rolls it took.
import random as r
def roll():
    a,b,c=0,0,0
    while True:
        a,b=int(r.randint(1,6)),int(r.randint(1,6))
        c+=1
        if a+b==7:
            print(c)
            break
#roll()     
#Write a function that checks if a given year is a leap year.
def leap(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return True
    else:
        return False
#print(leap(2004))
#Write a program that finds all prime numbers between 1 and 100.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def primes_between_1_and_100():
    primes = [n for n in range(1, 101) if is_prime(n)]
    print("Prime numbers between 1 and 100:")
    print(primes)
primes_between_1_and_100()
