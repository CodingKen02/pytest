"""
Created by: Kennedy Keyes and Javier Davis (add netIDs!)
Assignment: Software Testing Group Project
Course: CSE Methods and Tools in Software Development

"""

import pytest
import math

##--------------------------------------------------------------------------

## openFile function below:

def openFile(filename):
    infile = open(filename, "r")

    print("File opened.")

## openFile test function with 2 distinct tests (file existence & data type) below:

## File Existence: the first 2 tests -> 1st passes/2nd fails
## Data Types: the last 4 tests -> 3rd fails/4th passes/5th fails/6th fails
## (Data Types used: floats/boolean/complex numbers/strings -> no .txt file type)
## Note: I think boolean converts into objects/bytes that the computer is able to read

@pytest.mark.parametrize("filenames, expected", [("testing.txt", "File opened."), 
("hello.txt", "File opened."), (53.4, "File opened."), (True, "File opened."), 
(10j, "File opened."), ("testing", "File opened.")])
def test_openFile(capsys, filenames, expected):
    openFile(filenames)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected

##--------------------------------------------------------------------------

## numbers function below:

def numbers(num1, num2):
    return num1 / num2

## numbers test function with 2 distinct tests (math correctness & data type) below:

## Math Correctness: the first 2 tests-> 1st passes/2nd fails
## Data Types: the last 4 tests-> 3rd passes/4th fails/5th fails/6th passes
## (Data Types used: integers/strings/floats & boolean/complex numbers)

@pytest.mark.parametrize("num1, num2, quotient", [(4, 2, 2), (2, 1, 3), 
(49, 7, 7), ("six", "three", "two"), (6.1, 2.9, True), (10j, 5, 2j)])
def test_numbers(num1, num2, quotient):
    assert numbers(num1, num2) == quotient

##--------------------------------------------------------------------------

## dist function below:

def dist(x1, y1, x2, y2):
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist

## dist test function with 2 distinct tests (data type & math correctness) below:

## Data Types: the first 4 tests-> 1st fails/2nd passes/3rd passes/4th fails
## Math Correctness: the last 2 tests-> 5th fails/6th passes
## (Data Types used: complex numbers/floats & integers/boolean/strings)

@pytest.mark.parametrize("x1, y1, x2, y2, distance", [(10j, 10j, 10j, 10j, 0), (1.0, 1.0, 1, 1, 0.0),
(True, True, True, True, False), ("one", "one", "one", "one", "zero"), (8, 4, 3, 3, 3), 
(3, 1, 5, 4, 3.6055512754639892931192212674705)])
def test_dist(x1, y1, x2, y2, distance):
    assert dist(x1, y1, x2, y2) == distance

##--------------------------------------------------------------------------

## below are the functions to test

"""
import math

## COMPLETED -------------------------------------------------------------KK
## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    infile = open(filename, "r")

    print("File opened.")

## COMPLETED -------------------------------------------------------------KK
## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    return num1 / num2

## COMPLETED -------------------------------------------------------------KK
## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    div = num1 / num2

    print("Your numbers divided is:", div)

## returns the squareroot of a particular number
def sq(num):
    return math.sqrt(num)

## grabs user's name
## greets them by their entire name
## names should be strings that only accept letters! (A-Z, a-z)
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    print("Your item at", index, "index is", numbers[index]) 

"""