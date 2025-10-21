#Create a class Car with attributes brand, model, year, and a method start().
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def start(self):
        return f"{self.brand} {self.model} ({self.year}) starting..."

#Create a class Rectangle that has methods area() and perimeter().
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

#Create a class BankAccount with methods deposit(), withdraw(), and check_balance(). Ensure you can’t withdraw more than the balance.
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    def withdraw(self, amount):
        if amount <= 0:
            return False
        if amount > self._balance:
            return False
        self._balance -= amount
        return True
    def check_balance(self):
        return self._balance

#Create a subclass SavingsAccount that inherits from BankAccount and adds an interest_rate attribute.
class SavingsAccount(BankAccount):
    def __init__(self, owner, initial_balance=0, interest_rate=0.01):
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest

#Create a class Student with attributes name, id, and grade. Add a method to check if the student has passed (≥ 50).
class Student:
    def __init__(self, name, sid, grade):
        self.name = name
        self.id = sid
        self.grade = grade
    def has_passed(self):
        return self.grade >= 50

#Create a class Book with attributes title, author, and price, and a method to display book details.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def details(self):
        return f"'{self.title}' by {self.author} — ${self.price}"

#Create a class Inventory that allows adding, removing, and viewing items in stock.
class Inventory:
    def __init__(self):
        self._stock = {}
    def add(self, item, qty=1):
        if qty <= 0: return
        self._stock[item] = self._stock.get(item, 0) + qty
    def remove(self, item, qty=1):
        if item not in self._stock: return False
        if qty <= 0: return False
        if qty >= self._stock[item]:
            del self._stock[item]
        else:
            self._stock[item] -= qty
        return True
    def view(self):
        return dict(self._stock)

#Create a class Employee with attributes name, id, and salary, and a method to give a raise.
class Employee:
    def __init__(self, name, eid, salary):
        self.name = name
        self.id = eid
        self.salary = salary
    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            return True
        return False

#Create a class Library that manages a collection of Book objects with methods to add, remove, and search books.
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
    def remove_book(self, title):
        for i, b in enumerate(self.books):
            if b.title == title:
                return self.books.pop(i)
        return None
    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]
    def search_by_author(self, author):
        return [b for b in self.books if author.lower() in b.author.lower()]

#Create a class Matrix that supports addition and subtraction of matrices.
class Matrix:
    def __init__(self, rows):
        # rows is list of lists
        self.rows = [list(r) for r in rows]
        self.r = len(self.rows)
        self.c = len(self.rows[0]) if self.r>0 else 0
    def __add__(self, other):
        if self.r != other.r or self.c != other.c:
            raise ValueError("Matrix size mismatch")
        out = []
        for i in range(self.r):
            row=[]
            for j in range(self.c):
                row.append(self.rows[i][j] + other.rows[i][j])
            out.append(row)
        return Matrix(out)
    def __sub__(self, other):
        if self.r != other.r or self.c != other.c:
            raise ValueError("Matrix size mismatch")
        out = []
        for i in range(self.r):
            row=[]
            for j in range(self.c):
                row.append(self.rows[i][j] - other.rows[i][j])
            out.append(row)
        return Matrix(out)
    def __repr__(self):
        return f"Matrix({self.rows})"

#Create a class Logger that writes messages to a file with timestamps.
import datetime
class Logger:
    def __init__(self, filename):
        self.filename = filename
    def log(self, message):
        ts = datetime.datetime.now().isoformat()
        with open(self.filename, 'a') as f:
            f.write(f"{ts} - {message}\n")
    def read(self):
        with open(self.filename) as f:
            return f.read()
#c=Logger('diqka.txt')
#c.log('testim')
#print(c.read())        
#Write a function that generates the first n Fibonacci numbers.
def fib(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

#Write a program that finds all prime numbers between 1 and 100.
def primes_1_100():
    primes = []
    for num in range(2, 101):
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            primes.append(num)
    return primes

#Write a recursive function to calculate the factorial of a number.
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

#Write a recursive function to find the sum of all elements in a list.
def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

#Write a function that returns all permutations of a given list.
import itertools
def all_permutations(lst):
    return [list(p) for p in itertools.permutations(lst)]
def permutations(lst):
    if len(lst) == 0:
        return [[]]
    result = []
    for i in range(len(lst)):
        remaining = lst[:i] + lst[i+1:]
        print(remaining)
        for p in permutations(remaining):
            result.append([lst[i]] + p)
    return result

# Example:
print(permutations([1, 2, 3]))


#Write a function that returns a list of all palindromic numbers between 1 and 1000.
def palindromic_numbers():
    pals = []
    for n in range(1, 1001):
        s = str(n)
        if s == s[::-1]:
            pals.append(n)
    return pals
#Write a function that reads a list of numbers from a file and returns their sum.
def sum_numbers_in_file(filename):
    total = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                num = float(line)
            except:
                continue
            total += num
    return total

#Write a function that generates 10 random numbers between 1 and 100 and writes them to a file.
import random
def write_random_numbers(filename, count=10):
    with open(filename, 'w') as f:
        for _ in range(count):
            f.write(str(random.randint(1,100)) + "\n")

#Write a function that reads those numbers back and prints their average.
def read_and_average(filename):
    nums=[]
    with open(filename) as f:
        for line in f:
            line=line.strip()
            if line:
                try:
                    nums.append(float(line))
                except:
                    pass
    return sum(nums)/len(nums) if nums else 0

#Write a program that reads a CSV file and prints the average of a numeric column.
import csv
def average_csv_column(filename, column_index=0):
    vals=[]
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) <= column_index:
                continue
            try:
                vals.append(float(row[column_index]))
            except:
                pass
    return sum(vals)/len(vals) if vals else 0

#Write a program that saves a Python dictionary as a JSON file and reads it back.
import json
def save_dict_to_json(d, filename):
    with open(filename, 'w') as f:
        json.dump(d, f)
def read_json_to_dict(filename):
    with open(filename) as f:
        return json.load(f)

#Create a module math_utils.py with functions for addition, subtraction, multiplication, and division. Import it into another script.
# We'll create the module file (so it can be imported when running locally).
#math_utils_code = """
#def add(a,b): return a+b
#def sub(a,b): return a-b
#def mul(a,b): return a*b
#def div(a,b): 
#    if b==0: raise ZeroDivisionError('division by zero')
#    return a/b
#"""
#with open('math_utils.py','w') as _f:
#    _f.write(math_utils_code)
### Now import it
#import importlib
#math_utils = importlib.import_module('math_utils')

#Write a program that simulates a simple login system where the username and password are verified from a file.
def create_credentials_file(filename, creds):
    # creds: dict username -> password
    with open(filename, 'w') as f:
        for u,p in creds.items():
            f.write(f"{u},{p}\n")
def verify_login(filename, username, password):
    with open(filename) as f:
        for line in f:
            line=line.strip()
            if not line: continue
            u,p = line.split(',',1)
            if u==username and p==password:
                return True
    return False

#Write a function that counts how many words in a sentence start with a vowel.
def words_starting_with_vowel(sentence):
    vowels=set('aeiouAEIOU')
    count=0
    for word in sentence.split():
        if word and word[0] in vowels:
            count += 1
    return count

#Write a function that takes a sentence and returns the longest word.
def longest_word(sentence):
    best = ""
    for w in sentence.split():
        if len(w) > len(best):
            best = w
    return best

#Write a function that returns the number of unique words in a given text.
def unique_word_count(text):
    seen=set()
    for w in text.split():
        seen.add(w)
    return len(seen)

#Write a function that reads student names and scores from a file and prints the top 3 students.
def top_three_students(filename):
    students=[]
    with open(filename) as f:
        for line in f:
            parts=line.strip().split(',')
            if len(parts) < 2: continue
            name = parts[0].strip()
            try:
                score = float(parts[1])
            except:
                continue
            students.append((name, score))
    students.sort(key=lambda x: x[1], reverse=True)
    return students[:3]
#Write a function that simulates tossing two dice until their sum equals 7 and prints how many rolls it took.
def toss_until_7():
    count = 0
    while True:
        a = random.randint(1,6)
        b = random.randint(1,6)
        count += 1
        if a + b == 7:
            return count

#Write a function that takes a list of tuples (name, grade) and returns the name of the student with the highest grade.
def top_student(pairs):
    if not pairs:
        return None
    best = pairs[0]
    for p in pairs:
        if p[1] > best[1]:
            best = p
    return best[0]

#Create a class Temperature that can convert between Celsius and Fahrenheit.
class Temperature:
    def __init__(self, celsius=0.0):
        self.c = celsius
    def to_fahrenheit(self):
        return (self.c * 9/5) + 32
    @staticmethod
    def from_fahrenheit(f):
        return Temperature((f - 32) * 5/9)

#Write a function that simulates a rock-paper-scissors game between the computer and the user.
def rps_play(user_choice):
    choices = ['rock','paper','scissors']
    comp = random.choice(choices)
    user = user_choice.lower()
    if user not in choices:
        return "Invalid choice"
    if user == comp:
        return f"Draw (both {user})"
    wins = {'rock':'scissors','scissors':'paper','paper':'rock'}
    if wins[user] == comp:
        return f"User wins ({user} beats {comp})"
    else:
        return f"Computer wins ({comp} beats {user})"

#Write a function that returns a list of all palindromic numbers between 1 and 1000.
# (Implemented above as palindromic_numbers)

#Write a function that uses a lambda to sort a list of dictionaries by a specific key.
def sort_dicts_by_key(list_of_dicts, key):
    return sorted(list_of_dicts, key=lambda d: d.get(key))

#Write a program that uses a decorator to log when a function starts and ends.
def log_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"START {fn.__name__}")
        res = fn(*args, **kwargs)
        print(f"END {fn.__name__}")
        return res
    return wrapper

#Write a function that uses map() and filter() to square only the even numbers in a list.
def square_even(nums):
    evens = list(filter(lambda x: x%2==0, nums))
    squares = list(map(lambda x: x*x, evens))
    return squares

#Write a function that compresses a string using the counts of repeated characters (e.g., "aaabb" → "a3b2").
def compress_string(s):
    if not s: return ""
    res = []
    cur = s[0]
    count = 1
    for ch in s[1:]:
        if ch == cur:
            count += 1
        else:
            res.append(cur + str(count))
            cur = ch
            count = 1
    res.append(cur + str(count))
    return ''.join(res)

#Write a program that simulates a simple ATM system (balance, deposit, withdraw, exit).
def atm_sim(initial_balance=0):
    bal = initial_balance
    while True:
        cmd = input("Enter command (balance/deposit/withdraw/exit): ").strip().lower()
        if cmd == "balance":
            print("Balance:", bal)
        elif cmd == "deposit":
            amt = float(input("Amount to deposit: "))
            if amt>0:
                bal += amt
        elif cmd == "withdraw":
            amt = float(input("Amount to withdraw: "))
            if amt>0 and amt <= bal:
                bal -= amt
            else:
                print("Insufficient funds or invalid amount")
        elif cmd == "exit":
            break
        else:
            print("Unknown command")

#Write a function that uses recursion to count how many times a given character appears in a string.
def count_char_recursive(s, ch):
    if s == "":
        return 0
    return (1 if s[0]==ch else 0) + count_char_recursive(s[1:], ch)

#Write a function that merges multiple dictionaries into one.
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

#Write a function that takes a list of integers and returns the sum of all numbers that appear more than once.
def sum_duplicates(nums):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n,0) + 1
    total = 0
    for k,v in freq.items():
        if v > 1:
            total += k * v
    return total

#Write a function that returns the number of unique words in a given text.
# (Implemented above as unique_word_count)

#Write a function that returns the longest word from a sentence.
# (Implemented above as longest_word)

#Write a function that returns a random password with at least one uppercase, one lowercase, one number, and one symbol.
import string
def random_password(length=12):
    if length < 4:
        raise ValueError("length must be >= 4")
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    symbol = random.choice("!@#$%^&*()-_=+[]{};:,.<>?")
    others = [random.choice(string.ascii_letters + string.digits + "!@#$%^&*()") for _ in range(length-4)]
    pwd_list = [upper, lower, digit, symbol] + others
    random.shuffle(pwd_list)
    return ''.join(pwd_list)

#Write a program that copies the contents of one text file to another.
def copy_file(src, dst):
    with open(src) as fsrc:
        content = fsrc.read()
    with open(dst, 'w') as fdst:
        fdst.write(content)
