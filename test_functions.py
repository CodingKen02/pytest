"""
Created by: Kennedy Keyes and Javier Davis
Assignment: Software Testing Group Project
Course: CSE Methods and Tools in Software Development
Program: Creation of test functions

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

@pytest.mark.parametrize("filenames", ["testing.txt", "hello.txt", 53.4, True, 10j, "testing"])
def test_openFile(filenames):
    assert openFile(filenames) == None

##--------------------------------------------------------------------------

## numbers function below:

def numbers(num1, num2):
    return num1 / num2

## numbers test function with 2 distinct tests (math correctness & data type) below:

## Math Correctness: the first 2 tests-> 1st passes/2nd fails
## Data Types: the last 4 tests-> 3rd passes/4th fails/5th passes/6th passes
## (Data Types used: integers/strings/floats & boolean/complex numbers)

@pytest.mark.parametrize("num1, num2, quotient", [(4, 2, 2), (2, 1, 3), 
(49, 7, 7), ("6", "3", None), (6.1, True, 6.1), (10j, 5, 2j)])
def test_numbers(num1, num2, quotient):
    assert numbers(num1, num2) == quotient

##--------------------------------------------------------------------------

## dist function below:

def dist(x1, y1, x2, y2):
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist

## dist test function with 2 distinct tests (math correctness & data type) below:

## Math Correctness: the first 2 tests-> 1st fails/2nd passes
## Data Types: the last 4 tests-> 3rd fails/4th passes/5th passes/6th fails
## (Data Types used: complex numbers/floats & integers/boolean & integers/strings)

@pytest.mark.parametrize("x1, y1, x2, y2, distance", [(8, 4, 3, 3, 3), 
(3, 1, 5, 4, 3.6055512754639892931192212674705), (10j, 10j, 10j, 10j, None), 
(1.0, 1.0, 1, 1, 0.0), (True, True, True, True, 0), ("1", "1", "1", "1", None)])
def test_dist(x1, y1, x2, y2, distance):
    assert dist(x1, y1, x2, y2) == distance

##--------------------------------------------------------------------------

## isPalindrome function below (a palindrome is a word that is the same backwards & forwards):

def isPalindrome(temp):
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False

## isPalindrome test function with 2 distinct tests (palindrome correctness & data type) below:

## Palindrome Correctness: the first 2 tests-> 1st passes/2nd fails
## Data Types: the last 5 tests-> 3rd fails/4th fails/5th fails/6th fails/7th passes
## (Data Types used: integer/boolean/complex number/float/string)

@pytest.mark.parametrize("strings, boolean", [("racecar", True), ("anna", False), 
(101, None), (True, None), (3j, None), (10.3, None), ("1010", False)])
def test_isPalindrome(strings, boolean):
    assert isPalindrome(strings) == boolean

##--------------------------------------------------------------------------

## divide function below:

def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    div = num1 / num2

    print("Your numbers divided is:", div)

## divide test function with 2 distinct tests (math correctness & data type) below:

## Math Correctness: the first 2 tests-> 1st fails/2nd passes
## Data Types: the last 4 tests-> 3rd passes/4th passes/5th passes/6th fails
## (Data Types used: boolean/strings/floats/integers)

def test_divide():
    num1 = iter([2])
    num2 = iter([2])
    assert divide == "Your numbers divded is: 1"

def test_divide2():
    num1 = iter([50])
    num2 = iter([2])
    assert divide

def test_divide3():
    num1 = iter([True])
    num2 = iter([True])
    assert divide

def test_divide4():
    num1 = iter(["0"])
    num2 = iter(["4"])
    assert divide

def test_divide5():
    num1 = iter([100.0])
    num2 = iter([5.0])
    assert divide

def test_divide6():
    num1 = iter([7])
    num2 = iter([7])
    assert divide == 1

##--------------------------------------------------------------------------

## sq function below:

def sq(num):
    return math.sqrt(num)

## sq test function with 2 distinct tests (math correctness & data type) below:

## Math Correctness: the first 2 tests-> 1st passes/2nd fails
## Data Types: the last 5 tests-> 3rd fails/4th passes/5th passes/6th passes
## (Data Types used: string/boolean/float/integer)

def test_sq():
    assert sq(49) == 7

def test_sq2():
    assert sq(49) == 9

def test_sq3():
    assert sq("100") == None

def test_sq4():
    assert sq(False) == 0

def test_sq5():
    assert sq(144.0) == 12.0

def test_sq6():
    assert sq(36) == 6

##--------------------------------------------------------------------------

## greetUser function below:

def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

## greetUser test function with 1 distinct test (data/input correctness) below:

## Input Correctness: 1st passes/2nd passes/3rd passes/4th passes/5th passes/6th fails

def test_greetUser():
    greetUser("Javier", "Ivan", "Davis")

def test_greetUser2(capsys):
    greetUser("Javier", "Ivan", "Davis")

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip()
       
def test_greetUser3():
    greetUser("N1yana", "Ama!ya", "C0hran")

def test_greetUser4():
    greetUser("Javier", "1van", "Davis")   

def test_greetUser5():
    greetUser("Jayce", "King", "Davis")

def test_greetUser6(capsys):
    first = (["Javier"])
    middle = (["Ivan"])
    last =  (["Davis"])
    assert greetUser == "Glad to have you!"

##--------------------------------------------------------------------------

## displayItem function below:

def displayItem(numbers, index):
    print("Your item at", index, "index is", numbers[index]) 

## displayItem test function with 2 distinct tests (order correctness & data type) below:

## Order Correctness: the first, second & last test-> 1st passes/2nd passes/6th fails
## Data Types: the middle tests-> 3rd passes/4th passes/5th passes
## (Data Types used: floats/strings/boolean)

def test_displayItem(capsys):
    numbers = iter([1, 2, 3, 4, 5, 6])
    index = iter([5])
    assert displayItem

def test_displayItem2(capsys):
    numbers = iter([32, 43, 96, 674, 35, 36])
    index = iter([16])
    assert displayItem

def test_displayItem3(capsys):
    numbers = iter([12, 23, 36, 44, 25, 56.3])
    index = iter([6.0])
    assert displayItem

def test_displayItem4(capsys):
    numbers = iter(["s", 23, 36, 44, 25, 22])
    index = iter(["b"])
    assert displayItem

def test_displayItem5(capsys):
    numbers = iter([12, 23, 36, 44, 25, 56, 60])
    index = iter([True])
    assert displayItem

def test_displayItem6(capsys):
    numbers = iter([1, 2, 3, 4, 5, 6])
    index = iter([2])
    assert displayItem == "Your item at 2 index is 6"

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

## COMPLETED -------------------------------------------------------------JD
## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    div = num1 / num2

    print("Your numbers divided is:", div)

## COMPLETED -------------------------------------------------------------JD
## returns the squareroot of a particular number
def sq(num):
    return math.sqrt(num)

## COMPLETED -------------------------------------------------------------JD
## grabs user's name
## greets them by their entire name
## names should be strings that only accept letters! (A-Z, a-z)
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

## COMPLETED -------------------------------------------------------------JD
## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    print("Your item at", index, "index is", numbers[index]) 

"""