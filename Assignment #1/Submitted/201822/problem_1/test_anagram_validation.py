#!/usr/bin/env python3
'''
***  Assignment - Problem Set #1: The UnitTest
1: Write a function to check whether two given strings are anagram of each other or not
What is anagram?
An anagram of a string is another string that contains same characters, only the order of characters can be different.

Example:
    I/P: Str1= “abcd”, Str2= “dabc”
    O/P: Input strings are anagram of each other
'''

import unittest
import anagram_validation

#These are the output messages from 'anagram_validation', let's retreive those messages (they are global variables, so re-use them in this unittest).
msg_min_char_required = anagram_validation.msg_min_char_required
msg_identical_char_order = anagram_validation.msg_identical_char_order
msg_match = anagram_validation.msg_match
msg_no_match = anagram_validation.msg_no_match

#Postive Path:
class TestValidAnagrams(unittest.TestCase):
	def test_single_word_string(self):
		result = anagram_validation.anagram_validator("abcd","dabc")
		self.assertEqual(result, msg_match)
		result = anagram_validation.anagram_validator("listen","silent")
		self.assertEqual(result, msg_match)
		result = anagram_validation.anagram_validator("hydroxydeoxycorticosterones","hydroxydesoxycorticosterone")
		self.assertEqual(result, msg_match)

	def test_with_minimum_supported_chars(self):
		result = anagram_validation.anagram_validator("ab","ba")
		self.assertEqual(result, msg_match)

	def test_strings_with_space_chars(self):
		result = anagram_validation.anagram_validator("rail safety","fairy tales")
		self.assertEqual(result, msg_match)

	def test_strings_with_mixed_case_chars(self):
		result = anagram_validation.anagram_validator("Tom Marvolo Riddle","I am Lord Voldemort")
		self.assertEqual(result, msg_match)	

	def test_strings_with_special_chars(self):
		result = anagram_validation.anagram_validator("friend's","friends'")
		self.assertEqual(result, msg_match)


#Negative Path:
class TestInvalidAnagrams(unittest.TestCase):
	def test_non_matching(self):
		result = anagram_validation.anagram_validator("cow","cows")
		self.assertEqual(result, msg_no_match)
		result = anagram_validation.anagram_validator("radio","frequency")
		self.assertEqual(result, msg_no_match)
		result = anagram_validation.anagram_validator("planet","hearts")
		self.assertEqual(result, msg_no_match)
		result = anagram_validation.anagram_validator("Lorem Ipsum is simply dummy text","printing and typesetting industry")
		self.assertEqual(result, msg_no_match)		
		result = anagram_validation.anagram_validator("<_)*$%^&#@!~", "abc")
		self.assertEqual(result, msg_no_match)		

	def test_with_less_than_minimum_supported_chars(self):
		result = anagram_validation.anagram_validator("","")
		self.assertEqual(result, msg_min_char_required)
		result = anagram_validation.anagram_validator("", "dabc")
		self.assertEqual(result, msg_min_char_required)
		result = anagram_validation.anagram_validator("abcd", "")
		self.assertEqual(result, msg_min_char_required)
		result = anagram_validation.anagram_validator("a", "d")
		self.assertEqual(result, msg_min_char_required)
		result = anagram_validation.anagram_validator("e", "e")
		self.assertEqual(result, msg_min_char_required)

	def test_with_identical_chars(self):
		result = anagram_validation.anagram_validator("ee","ee")
		self.assertEqual(result, msg_identical_char_order)
		result = anagram_validation.anagram_validator("us","us")
		self.assertEqual(result, msg_identical_char_order)


#Keep track of where this script is being called from - directly or from an import.
if __name__ == "__main__":
  print ("*** Running from {} ***".format(__file__))
  unittest.main()
else:
  print ("*** Imported from {} ***".format(__name__))
