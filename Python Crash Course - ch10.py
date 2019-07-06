# ch 10

# 10.1　从文件中读取数据
# file_reader.py
file_path = r'C:\Users\Aaron\Syncthing\Jupyter\Python-Crash-Course-Bootcamp\chapter_10\pi_digits.txt'
# Read a file and print its content.
with open(file_path) as file_object:
    contents = file_object.read()
    print((contents))

# Read a file line by line.
with open(file_path) as file_object:
    for line in file_object: # same: for line in file_object.readlines()
        print(line)
# Read a file line by line and store lines in a list for later use.
with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

# pi_string.py
filename = 'chapter_10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:52] + "...")
print(len(pi_string))

# Is my birthday included in 1000000 long pi number? 
filename = 'chapter_10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# Exercise 10-1
filename = 'chapter_10/learning_python.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(f"Exercise 10-1: method 1")
    print(contents)

with open(filename) as file_object:
    print(f"Exercise 10-1: method 2")
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    print(f"Exercise 10-1: method 3")
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# Exercise 10-2
# Questons: Can I write it as functions?
def read_file(filename):
    """Read a file and return its contents line by line in a list."""
    with open(filename, 'r') as file_object:
        print(f"DEBUG: Is file object closed? {file_object.closed}")
        lines = file_object.readlines()
    print(f"DEBUG: Is file object closed? {file_object.closed}")
    return lines

def replace_lines(lines: list, old, new, count=-1):
    """Replaces strings in lines in a list given.
    As a wrapper of str.replace()."""
    # Should I return something back? See help(str.replace)...'Return a copy...'
    new_lines = []
    for line in lines:
        new_lines.append(line.replace(old, new))
    return new_lines

def print_lines(lines, line_start, line_end):
    """Given a list and print its content line by line."""
    for line in lines:
        print(f"{line_start}{line}{line_end}")

if __name__ == "__main__":
    print(f"\nExercise 10-2 rewrite as function call.")
    filename = 'chapter_10/learning_python.txt'
    lines = read_file(filename)
    new_lines = replace_lines(lines, 'Python', 'Javvva')
    print_lines(new_lines, '\t - ', '')

# Exercise 10-2
# Questons: Can I write it as classes?
class FileOperator():
    """Operator of files."""
    def __init__(self, filename):
        """Initial FileOperator with filename."""
        self.filename = filename

    def read_file(self):
        """Read a file and return its contents line by line in a list."""
        with open(self.filename, 'r') as file_object:
            # print(f"DEBUG: Is file object closed? {file_object.closed}")
            lines = file_object.readlines()
        # print(f"DEBUG: Is file object closed? {file_object.closed}")
        return lines

class ListOperator():
    """Operator of lists."""
    def __init__(self, list):
        """Give a list to be operated."""
        self.list = list

    def replace_lines(self, old, new, count=-1):
        """Replaces strings in lines in a list given.
        As a wrapper of str.replace()."""
        # Should I return something back? See help(str.replace)...'Return a copy...'
        new_lines = []
        for line in self.list:
            new_lines.append(line.replace(old, new))
        self.list = new_lines
        # return new_lines

    def print_lines(self, line_start, line_end):
        """Given a list and print its content line by line."""
        for line in self.list:
            print(f"{line_start}{line}{line_end}")

if __name__ == "__main__":
    print(f"\nExercise 10-2 rewrite as OOP.")
    filename = 'chapter_10/learning_python.txt'
    file_op1 = FileOperator(filename)
    lines = file_op1.read_file()
    list_op1 = ListOperator(lines)
    new_lines = list_op1.replace_lines('Python', 'Javvva')
    list_op1.print_lines('\t - ', '')


# 10.2　写入文件
# write_message.py
# Write to a file (overwrite).
filename = 'chapter_10/programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love programming.')

# Append to a file
filename = 'chapter_10/programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")


'''
10-3 访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件 guest.txt 中。

10-4 访客名单：编写一个while循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt 中。确保这个文件中的每条记录都独占一行。

10-5 关于编程的调查：编写一个while循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
'''
# Exercise 10-3
# I borrow the FileOperator defined in Exercise 10-2
# FileOperator - most updated
class FileOperator():
    """Operator of files."""
    def __init__(self, filename):
        """Initial FileOperator with filename."""
        self.filename = filename

    def read_file(self):
        """Read a file and return its contents line by line in a list."""
        try:
            with open(self.filename, 'r') as file_object:
                # print(f"DEBUG: Is file object closed? {file_object.closed}")
                lines = file_object.readlines()
            # print(f"DEBUG: Is file object closed? {file_object.closed}")
        except FileNotFoundError:
            msg = f"Sorry, the file {filename} does not exist."
            print(msg)
        except IOError:
            msg = f"File {self.filename} cannot be read."
            print(msg)
        else:
            return lines

    def write_file(self, content):
        """Write a file with the given content."""
        try:
            with open(self.filename, 'w') as file_object:
                file_object.write(content)
        except IOError:
            msg = f"Unable to write file on disk."
            print(msg)
        else:
            msg = f"File '{self.filename}' is written."
            print(msg)

    def append_file(self, content):
        """Append to a file with the given content."""
        try:
            with open(self.filename, 'a') as file_object:
                file_object.write(f"{content}\n")
        except IOError:
            msg = f"Unable to write file on disk."
            print(msg)
        else:
            msg = f"File '{self.filename}' is appened."
            print(msg)

def ask_input(msg):
    user_input = input(msg)
    return user_input

if __name__ == "__main__":
    print(f"\nExercise 10-3: Ask user input his name, then write his name to a file.")
    filename = 'chapter_10/guest.txt'
    msg = "What's your name?"
    
    file_op1 = FileOperator(filename)
    name = ask_input(msg)
    file_op1.write_file(name)

# Exercise  10-4
def greeting(name):
    return (f"Greeting! {name}.")

if __name__ == "__main__":
    print(f"\nExercise 10-4: Ask user input his name, then write his name to screen then to a file. Repeat.")
    filename = 'chapter_10/guest.txt'
    print("Enter 'q' to quit.")
    msg = "What's your name?"
    
    file_op1 = FileOperator(filename)
    while True:
        name = ask_input(msg)
        if name == 'q':
            break
        print(greeting(name))
        file_op1.append_file(name)
    print(f"End appending file '{filename}'")


# 10.3　异常
# division.py
try:
    print(5/0)
except ZeroDivisionError as e:
    print(f"Oops...{e}")
    print("You can't divide by zero!")

# division.py
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# alice.py
filename = 'chapter_10/alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f"Sorry, the file {filename} does not exist."
    print(msg)
else:
    # Calculate how many words the file contains.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

# word_count.py
def count_words(filename):
    """Calculate how many words a file contains.""" 
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = f"Sorry, the file {filename} does not exist."
        print(msg)
    else:
        # Calculate how many words the file contains.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['chapter_10/alice.txt', 'chapter_10/siddhartha.txt', 'chapter_10/moby_dick.txt', 'chapter_10/little_women.txt']
for filename in filenames:
    count_words(filename)

# Exercise 10-6, 10-7
print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError as e:
        print(f"{e}: You can't add string")
    else:
        print(answer)

# 10.4　存储数据
# number_writer.py
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

# number_reader.py
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

# remember_me.py
import json

filename = 'username.json'
username = input("WHat is our name?")
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print(f"We'll remember you when you come back, {username}!")

# greet_user.py
import json

filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print(f"Welcome back, {username}!")

# remember_me.py
import json

# Load user name if it is stored.
# Else, we promot for username and store it.
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("WHat is our name?")
    with (filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

# Refactor of remember_me.py
import json

def get_stored_username(filename):
    """If a username is stored, get it."""
    # Load user name if it is stored.
    # Else, we promot for username and store it.
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(filename):
    """Promot for username."""
    username = input("WHat is our name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username 

def greet_user(filename):
    """Greet user with his name."""
    username = get_stored_username(filename)
    if username: # not None!
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(filename)
        print(f"We'll remember you when you come back, {username}!")

filename = 'username.json'
greet_user(filename)

"""
10-11 喜欢的数字：编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number! It's _____.”。

10-12 记住喜欢的数字：将练习10-11中的两个程序合而为一。如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。运行这个程序两次，看看它是否像预期的那样工作。

10-13 验证用户：最后一个 remember_me.py 版本假设用户要么已输入其用户名，要么是首次运行该程序。我们应修改这个程序，以应对这样的情形：当前和最后一次运行该程序的用户并非同一个人。

为此，在greet_user()中打印欢迎用户回来的消息前，先询问他用户名是否是对的。如果不对，就调用get_new_username()让用户输入正确的用户名。
"""

# TODO
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }
