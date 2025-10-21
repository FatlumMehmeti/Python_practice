#Write a function that creates a text file called data.txt and writes the line "Hello World" into it.
def wr():
    with open('Projects\\data.txt','wt') as file:
        file.write('Hello World')
        file.close()
#wr()        
#Write a function that reads all lines from a text file and prints them on the screen.
def rt():
    with open('Projects\\data.txt','rt') as file:
        content=''
        for i in file.readlines():
            print(i,end='')   
        file.close()
#rt()
#Write a program that handles a ZeroDivisionError when dividing two numbers entered by the user.
def zero(a:int,b:int):
    try:
        return a/b
    except ZeroDivisionError:
        print("try again cause the numbers were incorrect")
    except:
        print('no idea what error this is')        
#print(zero(1,0))
#Write a function that counts how many lines, words, and characters are in a given text file.
def count():
    l,w,c=0,0,0
    with open('Projects\\data.txt','rt') as f:
        for line in f:
            l+=1
            w+=len(line.split())
            c+=len(line)
    return l,w,c   
#print(count()) 
#Write a program that appends user input to a file until the user types "stop".
def write_smt():
    with open('Projects\\data.txt','a') as f:
        while True:
            i=input(">")
            if i.lower() =='stop':
                break
            f.write(i +'\n')
#write_smt()            
#Write a program that asks for a filename and checks whether the file exists.
import os
def check_file_existence():
    filename = input("Please enter the name or path of the file to check: ").strip()
  
    if not filename:
        print("Error: No filename was entered.")
        return
    if os.path.exists(filename):
        print(f"\nSuccess! The file or directory '{filename}' exists.")
