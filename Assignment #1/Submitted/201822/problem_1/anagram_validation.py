#!/usr/bin/env python3
'''
***  Assignment - Problem Set #1: The Solution
1: Write a function to check whether two given strings are anagram of each other or not
What is anagram?
An anagram of a string is another string that contains same characters, only the order of characters can be different.

Example:
    I/P: Str1= “abcd”, Str2= “dabc”
    O/P: Input strings are anagram of each other
'''

#These are the output messages we want to display, so let's store them in seperate meaningful variables - useful for unittest as well.
global msg_min_char_required
msg_min_char_required = "String supplied must contain at least 2 letters. Please check your strings and try again."
global msg_identical_char_order
msg_identical_char_order = "The supplied strings are close to identical. Please supply a string with different order of character(s)."
global msg_match
msg_match = "Input strings are anagram of each other"
global msg_no_match
msg_no_match = "Input strings are NOT anagram of each other"


#Function: anagram_validator
#INPUT: Takes in two strings - e.g. Str1= “abcd”, Str2= “dabc”
#OUTPUT: Returns a string - a msg as defined in the above global variables. 
def anagram_validator(string1, string2):
    print("\n\nCOMPARING: \n\t>1st String: \"{}\" \n\t>2nd String: \"{}\"".format(string1,string2))

    #Anagrams strings can contain spaces, and different case chars, but for easy comparison let's remove the spaces and make them all lowercase for both strings.
    str1 = convert_to_no_space_lower_string(string1)
    str2 = convert_to_no_space_lower_string(string2)

    # validate the strings supplied are infact alphabets only.
    # Validate for alphabets only (NOTE: it's possible for anagrams to contain non-alhpabets - e.g. friends' or friend's)
    # if (convertToLowerAlpha(.isalpha()) or (Str2.isalpha()):
    #  outputString = "Non-Alphabets detected in supplied strings. Please check your strings and try again."

    msg = msg_no_match                              # Default msg when the strings are not anagrams.

    if ((len(str1) < 2) or (len(str2) < 2)):        # Lowest possible anagram string should contain at minimum 2 chars.
        msg = msg_min_char_required
    elif (len(str1) == len(str2)):                  # For it to be an anagram string, both strings character count should match, not including white spaces.
        if (str1 == str2):                          # If both strings have same char order, they can't be an anagram, they are too close to being identical
            msg = msg_identical_char_order
        elif (is_same_sorted_string(str1, str2)):   # Sort the order of the chars (without the spaces, all lowercase) to see if both strings have the same char order
            msg = msg_match
    print ("\t=>RESPONSE: "+msg)
    return msg


#Function: convert_to_no_space_lower_string
#INPUT: Takes in a strings - e.g. Str1= “abcd” or Str2= “dabc”
#OUTPUT: Returns a string with no white spaces, and in lowercase.
def convert_to_no_space_lower_string(str):
    # remove leading & trailing spaces
    str = str.strip()
    # remove blank spaces
    str = str.replace(" ", "")
    # return a lowercase string for easy comparison.
    return str.lower()


#Function: is_same_sorted_string
#INPUT: Takes in 2 strings - e.g. Str1= “abcd” or Str2= “dabc”
#OUTPUT: Returns a boolean - True if both list (convered from string) match and False if they don't.
def is_same_sorted_string(str1, str2):
    # compare two lists, are they the same? e.g. ['a', 'b', 'c', 'd'] == ['w', x', 'y', 'z'] ?
    return (sort_string(str1) == sort_string(str2))


#Function: sort_string
#INPUT: Takes in a strings - e.g. “abcd” or “dabc”
#OUTPUT: Returns a sorted list - e.g “dabc” -to-> ['a', 'b', 'c', 'd']
def sort_string(str):
    # Take the iterable string 'myString', and return a new sorted list
    return sorted(str)


# Local script test only. Please see UnitTest for comprehensive coverage.
def main():
    print ("Testing Started...")
    anagram_validator("a", "d")
    anagram_validator("ee", "ee")
    anagram_validator("abcd", "dabc")
    anagram_validator("Tom Marvolo Riddle", "I am Lord Voldemort")
    anagram_validator("friend's", "friends'")


#Keep track of where this script is being called from - directly or from an import
if __name__ == "__main__":
  print ("*** Running from {} ***".format(__file__))
  main()
else:
  print ("*** Imported from {} ***".format(__name__))
