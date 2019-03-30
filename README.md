# Solution of Code-Challenges
Solution of Scripts for each code challenge 

# Prerequisites
You only need to have Python3 downloaded and installed

A text Editor example Sublime , Atom , Note++

# Installation
Clone (or download) the repo

git clone https://github.com/sanamsanam/Code-Challenge.git

Navigate into the folder and .py file for each script

cd Code-Challenge

python3 icecream.py (example)


# List of Code Challenges:
## 1: Palindrome 
A palindrome is a word that reads the same backward or forward.
Write a function that checks if a given word is a palindrome. Character case should be ignored.

For example, is_palindrome("Deleveled") should return True as character case should be ignored, resulting in "deleveled", which is a palindrome since it reads the same backward and forward.

## 2: Merge Names
Implement the unique_names method. When passed two arrays of names, it will return an array containing the names that appear in either or both arrays. The returned array should have no duplicates.
For example, calling

unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])
should return an array containing Ava, Emma, Olivia, and Sophia in any order.

## 3: Ice Cream Machine
Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping. If there are no ingredients or toppings, the method should return an empty list.

For example,
IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops()

should return
[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

## 4:  Pipeline
As part of a data processing pipeline, complete the implementation of the pipeline method:
The method should accept a variable number of functions, and it should return a new function that accepts one parameter arg.

The returned function should call the first function in the pipeline with the parameter arg, and call the second function with the result of the first function.

The returned function should continue calling each function in the pipeline in order, following the same pattern, and return the value from the last function.

For example, pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2) then calling the returned function with 3 should return 5.0.

## 5:  File Owners
Implement a group_by_owners function that:

Accepts a dictionary containing the file owner name for each file name.

Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary:

{
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
the group_by_owners function should return

{
    'Randy': ['Input.txt', 'Output.txt'],
    'Stan': ['Code.py']
}

## 6: Song
A playlist is considered a repeating playlist if any of the songs contain a reference to a previous song in the playlist. Otherwise, the playlist will end with the last song which points to None.
Implement a function is_repeating_playlist that returns true if a playlist is repeating or false if it is not.

For example, the following code prints "True" as both songs point to each other.

