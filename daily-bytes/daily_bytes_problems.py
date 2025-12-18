############################################################################
# Daily Coding Problems
############################################################################

#### Problem 1 ####
    # “Cat”, return “taC”
    # “The Daily Byte”, return "etyB yliaD ehT”
    # “civic”, return “civic”

### Solution:
# Define function
def reverse_string(s: str):
    letters = []

    for i in s:
        letters.append(i)
    
    letters_reversed = letters[::-1] # [::-1] indexing to print reverse list order
    reversed_string = "".join(letters_reversed) ## .join() = converts a list to string

    return reversed_string

# Test
reverse_string("Cat") 
reverse_string("The Daily Byte")
reverse_string("civic")

#### Problem 2: 12/14/25 ####
    # Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
    # "level", return true
    # "algorithm", return false
    # "A man, a plan, a canal: Panama.", return true

### Solution:
def is_palindrome(s: str):
    letters = []
    s = s.lower() # Make lowercase
    
    # Capture sequence
    for i in s:
        if i.isalpha():
            letters.append(i)
    
    # Test for identical reverse
    if letters[::-1] == letters[::1]:
        return True
    else:
        return False

is_palindrome('level')
is_palindrome('A man, a plan, a canal: Panama.')


#### Problem 3: 12/15/25 ####
    # Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position.
    # "LR", return true
    # "URURD", return false
    # "RUULLDRD", return true

### Solution:
def predict_vacuum_path(vacuum_path: str):
    x = 0 # L - R axis
    y = 0 # U - D axis
    moves = [] # init list to store sequence 

    # Iterate over sequence
    for single_move in vacuum_path:
        if single_move == "L":
            x += 1
        elif single_move == "R":
            x += -1
        elif single_move == "U":
            y += 1
        elif single_move == "D":
            y += -1
        else:
            return "Sequence contains non-directional values. Please enter only L, R, U and D."
    
    # Return answer
    if x + y == 0:
        return True
    else:
        return False

# Test
predict_vacuum_path('LR')
predict_vacuum_path('RUULsLDRD')


#### Problem 4: 12/16/25 ####
    # Given a string, return whether or not it uses capitalization correctly.
    # A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

### Solution:
def check_capitalization(s: str):
    # If all letters after 1st are captial
    if s[1:len(s)].islower(): # This accounts for String and string
        return True
    # If all letters are upper
    elif s.isupper():
        return True
    else:
        return False
    
# Test
check_capitalization('USA')
check_capitalization('Calvin')
check_capitalization('compUter')
check_capitalization('coding')

#### Problem 5: 12/17/25 ####
    # Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
    # Note: neither binary string will contain leading 0s unless the string itself is 0

### Solution:
s1 = "101"
s2 = "1"
def add_binary_string(s1: str, s2: str):
    sum = int(s1,2) + int(s2,2)
    bin_sim = str(bin(sum))[2:]

    return bin_sim

add_binary_string("100", "1") # Returns 101
add_binary_string("11", "1") # Returns 100
add_binary_string("1", "0") # Returns 1


#### Problem 6: 12/18/25 ####
    # Given an array of strings, return the longest common prefix that is shared amongst all strings.
    # Note: you may assume all strings only contain lowercase alphabetical characters.

### Solution:
def find_common_prefix(list_of_strings, lst):
    for i in list_of_strings:
        