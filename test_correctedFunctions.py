"""
Created by: Kennedy Keyes and Javier Davis (add netIDs!)
Assignment: Software Testing Group Project
Course: CSE Methods and Tools in Software Development
Program: Corrections for test functions (some are intended to still fail)

"""

import pytest
import math

##--------------------------------------------------------------------------

## openFile correction function below:

def openFile(filename):
    try:
        infile = open(filename, "r")

        print("File opened.")

    except TypeError: ## Invalid Data Type
        print("Sorry, please try to enter a string.")

    except:
        print("No file or file type exists.")


## openFile test function with 2 distinct tests (file existence & data type) below:

## File Existence: the first 2 tests -> 1st passes/2nd fails
## Data Types: the last 4 tests -> 3rd fails/4th passes/5th fails/6th fails
## (Data Types used: floats/boolean/complex numbers/strings -> no .txt file type)
## Note: I think boolean converts into objects/bytes that the computer is able to read

## Note: Deleted the "expected" variable since there is no return value

@pytest.mark.parametrize("filenames", ["testing.txt", "hello.txt", 53.4, True, 10j, "testing"])
def test_openFile(filenames):
    assert openFile(filenames) == None

##--------------------------------------------------------------------------

## numbers correction function below:

def numbers(num1, num2):
    try:
        return num1 / num2
    
    except:
        print("An error has occured.")

## numbers test function with 2 distinct tests (math correctness & data type) below:

## Math Correctness: the first 2 tests-> 1st passes/2nd fails
## Data Types: the last 4 tests-> 3rd passes/4th fails/5th passes/6th passes
## (Data Types used: integers/strings/floats & boolean/complex numbers)

@pytest.mark.parametrize("num1, num2, quotient", [(4, 2, 2), (2, 1, 3), 
(49, 7, 7), ("6", "3", 2), (6.1, True, 6.1), (10j, 5, 2j)])
def test_numbers(num1, num2, quotient):
    assert numbers(num1, num2) == quotient

##--------------------------------------------------------------------------

## dist correction function below:

def dist(x1, y1, x2, y2):
    try:
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
        dist = math.sqrt(dist)

        return dist

    except TypeError: ## Invalid Data Type
        print("Sorry, please try to enter a numeric value.")

    except:
        print("An error has occured.")

## dist test function with 2 distinct tests (math correctness & data type) below:

## Math Correctness: the first 2 tests-> 1st fails/2nd passes
## Data Types: the last 4 tests-> 3rd fails/4th passes/5th passes/6th fails
## (Data Types used: complex numbers/floats & integers/boolean & integers/strings)

@pytest.mark.parametrize("x1, y1, x2, y2, distance", [(8, 4, 3, 3, 3), 
(3, 1, 5, 4, 3.6055512754639892931192212674705), (10j, 10j, 10j, 10j, 0), 
(1.0, 1.0, 1, 1, 0.0), (True, True, True, True, 0), ("1", "1", "1", "1", 0)])
def test_dist(x1, y1, x2, y2, distance):
    assert dist(x1, y1, x2, y2) == distance

##--------------------------------------------------------------------------

## isPalindrome correction function below:

def isPalindrome(temp):
    try: 
        test = temp[::-1]

        if(test == temp):
            return True

        else:
            return False

    except:
        print("An error has occured.")

## isPalindrome test function with 2 distinct tests (palindrome correctness & data type) below:

## Palindrome Correctness: the first 2 tests-> 1st passes/2nd fails
## Data Types: the last 4 tests-> 3rd fails/4th fails/5th fails/6th fails/7th passes
## (Data Types used: integer/boolean/complex number/float/string)

@pytest.mark.parametrize("strings, boolean", [("racecar", True), ("anna", False), 
("101", True), (True, True), (3j, False), (10.3, False), ("cat", False)])
def test_isPalindrome(strings, boolean):
    assert isPalindrome(strings) == boolean

##--------------------------------------------------------------------------

## below are the given functions to test

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

## COMPLETED -------------------------------------------------------------KK
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