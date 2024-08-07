import re
from helper import d
# Task 1: Name Verification

# Problem Statement:  Write a function that takes in a list of names, and verifies that the names are valid names using a regex pattern and match(), and prints the name if it is valid, "Invalid name" if the name is not.

# Use the following list as an argument to test your function.

# Code Example:

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

# Expected Outcome:

# Abraham Lincoln
# Andrew P Garfield
# Invalid name
# Connor Milliken
# Jordan Alexander Williams
# Invalid name
# Invalid name

# two solutions using re.compile():                # Need more examples to use match() method.

d()

def valid_name():
    pattern = re.compile(r'\b[A-Z]+[a-z]*\s[A-z][a-z]?\s*\D+[a-z]*\B')
    for name in names:
        if pattern.match(name):
            print(name)
        else:
            print("Invalid name")

valid_name()

d()

def veri_names(names):
    pattern = re.compile(r'^[A-Z][a-z]*\s[A-Z][a-z]*(\s[A-Z][a-z]*)?$')
    for name in names:
        if pattern.match(name):
            print(name)                                         # Adding Parameter (names)
        else:
            print("Invalid name")

veri_names(names)

d()

# ^^^^ The re.compile() method changed the string pattern into a re.Pattern object that we can work upon. ^^^^
# Next, we used the re.Pattern object inside a re.findall() method to obtain all the possible matches of any three consecutive digits inside the target string.
# Now, the same reagex_pattern object can be used similarly for searching for three consecutive digits in other target strings as well.
# Compiling regular expression objects is useful and efficient when the expression will be used several times in a single program.

# Keep in mind that the compile() method is useful for defining and creating regular expressions object initially and then using that object we can look for occurrences of the same pattern inside various target strings without rewriting it which saves time and improves performance.

# Avoid using the compile() method when you want to search for various patterns inside the single target string. You do not need to use the compile method beforehand because the compiling is done automatically with the execution of other regex methods.

# you should use the compile() method when you’re going to perform a lot of matches using the same pattern. Also, when you are searching for the same pattern over and over again and in multiple target strings