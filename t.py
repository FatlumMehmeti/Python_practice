
#### from typing import Final
#### PI:Final=30.00
#### for i in range(11, 10):
####     print(i)
####     if i % 2 == 0:
####         print(i)
#### PI=322.00

#### print(PI)
#### from platform import processor

#### print(processor())

#### a=1e-2
#### b=2.5e1
#### print(a,"  ",b)
#### print(a*b)

#### def fun():
####     a=int(input("Enter a number: "))
####     if a%2==0:
####         print("Even")
####     else:
####         print("Odd")
    
#### fun()


#### from os import strerror
#### srcname = input("Enter the source file name: ")
#### try:
####     src = open(srcname, 'r')
####     content = src.read()
####     print(content)
####     src.close()  
#### except IOError as e:
####     print("I/O error occurred:", strerror(e.errno))

###def read_file():
###        with open("diqka.txt", 'wt') as file:
###            content = file.write("Hello World")
###            print(content)
###            file.close()
###read_file()           
##import datetime
##class Logger:
##    def __init__(self, filename):
##        self.filename = filename
##    def log(self, message):
##        ts = datetime.datetime.now().isoformat()
##        with open(self.filename, 'a') as f:
##            f.write(f"{ts} - {message}\n")
##    def read(self):
##        with open(self.filename) as f:
##            return f.read()
##c=Logger('diqka.txt')
##c.log('testim')
##print(c.read())  

#def permutations(lst):
#    if len(lst) == 0:
#        return [[]]
#    result = []
#    for i in range(len(lst)):
#        remaining = lst[:i] + lst[i+1:]
#        print(f'{lst[:i]} + {lst[i+1:]}   ',i)
#        print(remaining)
#        for p in permutations(remaining):
#            result.append([lst[i]] + p)
#    return result

## Example:
#print(permutations([1, 2, 3]))
##import itertools
##def all_permutations(lst):
##    return [list(p) for p in itertools.permutations(lst)]
##print(all_permutations([1, 2, 3]))
#s='121'
#print(s[::-1])

def palindromic_numbers():
    pals = []
    for n in range(1, 1001):
        s = str(n)
        if s == s[::-1]:
            pals.append(n)
    return pals
print(palindromic_numbers())