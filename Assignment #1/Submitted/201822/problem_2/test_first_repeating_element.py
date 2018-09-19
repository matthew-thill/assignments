#!/usr/bin/env python3
'''
***  Assignment - Problem Set #2: The UnitTest
2: Find the first repeating element in an array of integers
Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest.

Example:
    I/P: arr=[100,5,3,1,0,5,-8]
    O/P: 5 [5 is the first element that repeats]
'''

import unittest
import first_repeating_element

'''
IMPORTANT: For a given example:
	result = first_repeating_element.find_first_repeating_number([100,5,3,1,0,5,-8])
'result' is a list, and we are interested in the: 
	- first element: result[0] - is a boolean - True if there's a repeating number, False if not.
	- & last element: result[2] - is an intager if result[0] is 'True', or empty string if result[0] is False.
'''

#Positive Path:
class TestPositivePath(unittest.TestCase):
	def test_first_repeating_element_found(self):
		result = first_repeating_element.find_first_repeating_number([100,5,3,1,0,5,-8])
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], 5)

		result = first_repeating_element.find_first_repeating_number([100,-8,3,1,0,-5,-8,9,4,3,2,6,4,5,0,-5,2,-1,0,6,7,1,-200])
		self.assertEqual(result[0], True)			
		self.assertEqual(result[2], -8)

		result = first_repeating_element.find_first_repeating_number([100,3,3,1,0,5,-8,9,4,3,2,6,4,5,0,-5,2,-1,0,6,7,1,-200])
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], 3)

		#Both inner and outer counters are right next to each other, so this check should be instant (more visible if you uncomment DEBUG print statments)
		result = first_repeating_element.find_first_repeating_number([100,100,3,1,0,5,-8,9,4,3,2,6,4,5,0,-5,2,-1,0,6,7,1,-200])
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], 100)

		result = first_repeating_element.find_first_repeating_number([100,1,2,3,4,5,6,7,8,9,10,10,100])
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], 100)

		#This should take a bit longer, as inner and outer counters of the loop traverse through the entire array until they reach the last to elements.
		#(more apparent if you uncomment DEBUG print statments)
		result = first_repeating_element.find_first_repeating_number([0,1,2,3,4,5,6,7,8,9,10,100,100])
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], 100)

		#Although there are other repeating numbers in the array, the first element is the first value to be identified (w/ smallest index) to repeat
		result = first_repeating_element.find_first_repeating_number([0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,0,1,0])
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], 0)

	def test_with_minimum_supported_array_elements(self):
		result = first_repeating_element.find_first_repeating_number([10,10])
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], 10)
	

#Negative Path:
class TestNegativePath(unittest.TestCase):
	def test_no_repeating_element_found(self):
		#As expected when there are no repeating numbers, an appropriate message to the effect is displayed.
		result = first_repeating_element.find_first_repeating_number([0,1,2,3,4,5,6,7,8,9,10,100])
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], '')	

	def test_with_less_than_minimum_supported_array_elements(self):
		#This should be an instant response as there are no elements to traverse through. It's more apparent if you uncomment DEBUG print statments.
		result = first_repeating_element.find_first_repeating_number([])
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], '')

		result = first_repeating_element.find_first_repeating_number([100])
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], '')


#Keep track of where this script is being called from - directly or from an import?
if __name__ == "__main__":
  print ("*** Running from {} ***".format(__file__))
  unittest.main()
else:
  print ("*** Imported from {} ***".format(__name__))
