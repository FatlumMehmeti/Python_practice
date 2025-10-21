#Write a function that flattens a nested list (e.g., [1, [2, 3], [4, [5]]] → [1, 2, 3, 4, 5]).
def flatten(n:list):
    """Write a function that flattens a nested list (e.g., [1, [2, 3], [4, [5]]] → [1, 2, 3, 4, 5])."""
    flat=[]
    for i in n:
        if isinstance(i,list):
            flat.extend(flatten(i))
        else:
            flat.append(i)            
    return flat
#print(flatten([1, [2, 3], [4, [5]]]))      

#Write a function that counts vowels and consonants in a given string.
def count_v_c(a:str):
    v,c=0,0
    a=a.replace(" ",'').lower()
    vowels=['a','e','i','o','u']
    for i in a:
        found=False
        for j in vowels:
            if i==j:
                v+=1
                found=True
                break
        if not found:
            c+=1    
    return v,c 
#print(count_v_c("Who are you "))       

#Write a function that returns the average of numbers in a list.
def avg(a:list):
    s=0
    count=0
    for i in a:
        s+=i
        count+=1
    return s/count if count!=0 else 0
#print(avg([1,2,3,4,5]))

#Write a program that asks the user to enter 5 numbers and prints the smallest and largest.
def min_max_5():
    nums=[]
    for _ in range(5):
        nums.append(int(input("Enter number: ")))
    smallest=nums[0]
    largest=nums[0]
    for n in nums:
        if n<smallest:
            smallest=n
        if n>largest:
            largest=n
    print("Smallest:",smallest,"Largest:",largest)
#min_max_5()

#Write a function that removes duplicates from a list.
def remove_dup(a:list):
    new=[]
    for i in a:
        exists=False
        for j in new:
            if i==j:
                exists=True
                break
        if not exists:
            new.append(i)
    return new
#print(remove_dup([1,2,2,3,4,4,5]))

#Write a function that takes a dictionary and prints all its keys and values.
def print_dict(d:dict):
    for k in d:
        print(f"{k}: {d[k]}")
#print_dict({'a':1,'b':2})

#Write a function that merges two lists into a dictionary (first → keys, second → values).
def merge_lists(keys:list,values:list):
    d={}
    i=0
    while i<len(keys) and i<len(values):
        d[keys[i]]=values[i]
        i+=1
    return d
#print(merge_lists(['a','b','c'],[1,2,3]))

#Write a program that reads numbers until the user enters 0, then prints the total sum.
def sum_until_zero():
    s=0
    while True:
        n=int(input("Enter number (0 to stop): "))
        if n==0:
            break
        s+=n
    print("Sum:",s)
#sum_until_zero()

#Write a function that counts how many lines, words, and characters are in a text file.
def file_stats(filename:str):
    f=open(filename)
    text=f.read()
    f.close()
    line_count=1 if text else 0
    word_count=0
    char_count=0
    for ch in text:
        char_count+=1
        if ch=='\n':
            line_count+=1
    in_word=False
    for ch in text:
        if ch.isspace():
            in_word=False
        else:
            if not in_word:
                word_count+=1
                in_word=True
    return line_count,word_count,char_count
#print(file_stats("sample.txt"))

#Write a program that handles a ZeroDivisionError and prints a custom message.
def safe_divide():
    try:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Result:",a/b)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
#safe_divide()

#Write a program that reads a file and prints only lines that contain the word "Python".
def print_python_lines(filename:str):
    f=open(filename)
    for line in f:
        if "Python" in line:
            print(line,end='')
    f.close()
#print_python_lines("sample.txt")

#Write a program that asks for a filename and checks whether the file exists.
import os
def check_file():
    fname=input("Enter filename: ")
    if os.path.exists(fname):
        print("File exists.")
    else:
        print("File not found.")
#check_file()

#Write a function that takes a list of integers and returns only the even numbers.
def even_only(a:list):
    ev=[]
    for x in a:
        if x%2==0:
            ev.append(x)
    return ev
#print(even_only([1,2,3,4,5,6]))

#Write a function that checks whether a given year is a leap year.
def leap_year(y:int):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#print(leap_year(2024))

#Write a function that returns a list of squares for numbers 1–10.
def squares():
    result=[]
    i=1
    while i<=10:
        result.append(i*i)
        i+=1
    return result
#print(squares())

#Write a function that simulates rolling a dice 10 times and prints each result.
import random
def roll_dice():
    i=0
    while i<10:
        print(random.randint(1,6))
        i+=1
#roll_dice()

#Write a function that finds the second largest number in a list.
def second_largest(a:list):
    if len(a)<2:
        return None
    largest=a[0]
    second=None
    for n in a:
        if n>largest:
            second=largest
            largest=n
        elif second is None or (n>second and n<largest):
            second=n
    return second
#print(second_largest([1,3,5,4,5,2]))

#Write a function that checks if two strings are anagrams.
def anagram(a:str,b:str):
    a=a.replace(" ","").lower()
    b=b.replace(" ","").lower()
    if len(a)!=len(b):
        return False
    for ch in a:
        found=False
        for i in range(len(b)):
            if ch==b[i]:
                b=b[:i]+b[i+1:]
                found=True
                break
        if not found:
            return False
    return len(b)==0
#print(anagram("listen","silent"))

#Write a function that takes a string and returns a dictionary counting each character.
def char_count(s:str):
    d={}
    for c in s:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    return d
#print(char_count("hello"))

#Write a function that writes a list of strings to a file, one per line.
def write_lines(filename:str,lines:list):
    f=open(filename,'w')
    for line in lines:
        f.write(line+'\n')
    f.close()
#write_lines("out.txt",["Hello","World"])

#Write a function that reads a text file and returns the number of lines it contains.
def count_lines(filename:str):
    f=open(filename)
    count=0
    for _ in f:
        count+=1
    f.close()
    return count
#print(count_lines("out.txt"))

#Write a program that reads integers from the user until they type "done", then prints the average.
def avg_until_done():
    s=0
    c=0
    while True:
        s_in=input("Enter number (or 'done'): ")
        if s_in.lower()=="done":
            break
        s+=int(s_in)
        c+=1
    print("Average:",s/c if c>0 else 0)
#avg_until_done()

#Write a function that checks if a number is prime.
def is_prime(n:int):
    if n<=1:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
#print(is_prime(7))

#Write a program that takes a list of numbers and prints a list of their squares using list comprehension.
def list_squares(nums:list):
    res=[]
    for x in nums:
        res.append(x*x)
    print(res)
#list_squares([1,2,3,4])

#Write a function that finds the median of a list of numbers.
def median(a:list):
    n=len(a)
    for i in range(n):
        for j in range(i+1,n):
            if a[j]<a[i]:
                a[i],a[j]=a[j],a[i]
    if n==0:
        return None
    if n%2==0:
        return (a[n//2-1]+a[n//2])/2
    else:
        return a[n//2]
#print(median([1,2,3,4,5]))

#Write a program that removes all punctuation from a given string.
def remove_punc(s:str):
    punc="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    new=""
    for ch in s:
        found=False
        for p in punc:
            if ch==p:
                found=True
                break
        if not found:
            new+=ch
    return new
#print(remove_punc("Hello, world! It's great."))

#Write a function that takes a dictionary and returns another dictionary with keys and values swapped.
def swap_dict(d:dict):
    new={}
    for k in d:
        new[d[k]]=k
    return new
#print(swap_dict({'a':1,'b':2}))

#Write a program that counts how many unique words are in a text file.
def unique_words(filename:str):
    f=open(filename)
    text=f.read()
    f.close()
    words=text.split()
    unique=[]
    for w in words:
        found=False
        for u in unique:
            if w==u:
                found=True
                break
        if not found:
            unique.append(w)
    count=0
    for _ in unique:
        count+=1
    return count
#print(unique_words("sample.txt"))

#Write a function that returns the factorial of a number using recursion.
def fact(n:int):
    if n<=1:
        return 1
    return n*fact(n-1)
#print(fact(5))

#Write a function that checks if all elements in a list are unique.
def all_unique(a:list):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                return False
    return True
#print(all_unique([1,2,3,3]))

#Write a function that takes a sentence and returns a list of all words that are longer than 5 letters.
def long_words(s:str):
    words=[]
    w=""
    for ch in s:
        if ch==" ":
            if w!="":
                words.append(w)
                w=""
        else:
            w+=ch
    if w!="":
        words.append(w)
    long=[]
    for word in words:
        count=0
        for _ in word:
            count+=1
        if count>5:
            long.append(word)
    return long
#print(long_words("This sentence contains several longwords indeed"))

#Write a program that finds all numbers between 1 and 1000 that are divisible by both 3 and 5.
def div_3_5():
    nums=[]
    x=1
    while x<=1000:
        if x%3==0 and x%5==0:
            nums.append(x)
        x+=1
    print(nums)
#div_3_5()

#Write a program that sorts a list of tuples by the second value in each tuple.
def sort_by_second(tuples:list):
    n=len(tuples)
    for i in range(n):
        for j in range(i+1,n):
            if tuples[j][1]<tuples[i][1]:
                tuples[i],tuples[j]=tuples[j],tuples[i]
    return tuples
#print(sort_by_second([(1,3),(2,2),(3,1)]))

#Write a program that generates a random number between 1 and 100 and asks the user to guess it until they are correct.
def guess_number():
    num=random.randint(1,100)
    while True:
        guess=int(input("Guess number: "))
        if guess==num:
            print("Correct!")
            break
        elif guess<num:
            print("Too low!")
        else:
            print("Too high!")
#guess_number()

#Write a program that copies the contents of one text file to another.
def copy_file(src:str,dst:str):
    f1=open(src)
    content=f1.read()
    f1.close()
    f2=open(dst,'w')
    f2.write(content)
    f2.close()
#copy_file("source.txt","destination.txt")
#write a function that counts the prints the first 3 charachte
# rs and the last 3 charachters in a string
def print_first_last_three(text):
    if len(text) < 3:
        print("String is too short!")
    else:
        first_three = text[:3]
        last_three = text[-3:]
        print("First three characters:", first_three)
        print("Last three characters:", last_three)
