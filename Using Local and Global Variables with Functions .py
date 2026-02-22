

# Using Local and Global variables. Declaring and using functions. Referencing variables, functions, dictionaries and lists. Notes and examples


# This first scrypt doesnt work because the variables first_name and last_name are only local variables, even when they are declared at the top. 
# See ChatGPT question and answer session:Local and Global Variables  with Functions




"""
first_name = ""
last_name = ""

def get_first_name():
    first_name = input("Enter your first name:")
    
    
def get_last_name():
    last_name = input("Enter your last name:")
    
    
def display_full_name(first, last):
    print(f"Hello {first}, {last}")
    

get_first_name()
get_last_name()
display_full_name(first_name, last_name)
    
    
# The correct and industry standard option to make this scrypt run correctly is by using return statements
"""


"""
def get_first_name():
    first_name = input("Enter your first name: ")
    return first_name
    

def get_last_name():
    last_name = input("Enter your last name: ")
    return last_name
    

def display_full_name(first, last):
    print(f"Hello {first} {last}")
    
    
# In this example, we could have used either of these two options below. However, the first method is likely preferred because you can then use 
# those variables again later if need be. ChatGPT says: A sneaky rule: “Inline until it becomes hard to read.” Readability beats cleverness in Python.

1. Store then use
first_name = get_first_name()
last_name = get_last_name()
display_full_name(first_name, last_name)

Or

2. Inline Calls
display_full_name(get_first_name(), get_last_name())
"""
    
    
# Another way to make this scrypt run (second best option), is by using a dictionary instead of variables. We could have used a list instead, and a 
# sample code of the list version is included in a comment section below


"""
# How it Works: data refers to the dictionary object that got passed in. The function is mutating it by assigning a key "first". Because data is not a copy.
It is a reference (a pointer) to the same object.
When you pass a dictionary into a function:
# We could have also used update, like this statement data.update({"first": input("Name: ")})


def get_first_name(data):
    data["first"] = input("Enter your first name: ")
    

def get_last_name(data):
    data["last"] = input("Enter your last name: ")
    

def display_full_name(data):
    print(f"Hello {data['first']} {data['last']}")
    

info = {}

get_first_name(info)
get_last_name(info)
display_full_name(info)


# List version
def get_first_name(data):
    data[0] = input("First: ")

data = [None, None]
"""


# Yet another way (NOT preferred, and ill advised), is by using global variables. 


"""
def get_first_name():
    global first_name
    first_name = input("Enter your first name: ")


def get_last_name():
    global last_name
    last_name = input("Enter your last name: ")


def display_full_name():
    print(f"Hello {first_name} {last_name}")


get_first_name()
get_last_name()
display_full_name()
"""


#


"""

"""


#


"""

"""


#


"""

"""