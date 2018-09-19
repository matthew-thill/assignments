#!/usr/bin/env python3
'''
***  Assignment - Problem Set #3: The UnitTest
3: Find a triplet that sum to a given value X.
Write a function to find if there is a triplet in integer array whose sum is equal to the given value x. If there is such a triplet present in array, then print the triplet and return true. Else return false. Just print first triplet if there are multiple triplets matching value x.

Example:
    I/P : array [12, 3, 4, 1, 6, 9,-6] and given sum x =24 
    O/P : (12, 3 and 9)
'''

import unittest
import find_triplet

'''
IMPORTANT: For a given example:
	result = find_triplet.get_triplet([12, 3, 4, 1, 6, 9,-6], 24)
'result' is a list, and we are interested in the:
	- first element: result[0] - is a boolean - True if there's a triplet, False if not.
	- & last element: result[2] - is an array if result[0] is 'True' with the triplet numbers, or an empty array if result[0] is False.
'''

#Positive Path:
class TestPositivePath(unittest.TestCase):
	def test_triplet_exists(self):
		result = find_triplet.get_triplet([12, 3, 4, 1, 6, 9,-6], 24)
		#self.assertEqual(sorted(result[2]), sorted([12,3,9]))		
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], [12,3,9])

		#This should take a bit longer, as inner and outer counters of the loop traverse through the entire array until they reach the very end of the 
		#loop or last three elements.
		result = find_triplet.get_triplet([100,-8,-1,-2,0,-5,-8,-1,-4,0,2,-6,4,5,0,-5,2,-1,0,-6,7,1,-200], -192)
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], [7,1,-200])

		#All three counters (outer, mid & inner indexes) are right next to each other at the start, so this result should be instant 
		#(more visible if you uncomment DEBUG print statments)
		result = find_triplet.get_triplet([100,3,3,1,0,5,-8,9,4,3,2,6,4,5,0,-5,2,-1,0,6,7,1,-200], 106)
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], [100,3,3])

		result = find_triplet.get_triplet([100,100,3,1,0,5,-8,9,4,3,2,6,4,5,0,-5,2,-1,0,6,7,1,-200], 5)
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], [3, 1, 1])

		result = find_triplet.get_triplet([100,1,2,3,4,5,6,7,8,9,10,10,100], 15)
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], [1, 4, 10])

		result = find_triplet.get_triplet([12, 3, 4, 1, 6, 9,-6], 12)
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], [12, 6, -6])


	def test_with_minimum_supported_array_size(self):
		result = find_triplet.get_triplet([12, 3, 4], 19)	
		self.assertEqual(result[0], True)
		self.assertEqual(result[2], [12,3,4])



#Negative Path:
class TestNegativePath(unittest.TestCase):
	def test_non_nonexistent_triplet(self):
		result = find_triplet.get_triplet([12, 3, 4, 1, 6, 9,-6], 200)
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], [])

		result = find_triplet.get_triplet([100,5,3,1,0,5,-8], 24)	
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], [])

		result = find_triplet.get_triplet([12, 3, 0], 9)	
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], [])


	def test_with_less_than_minimum_supported_array_size(self):
		result = find_triplet.get_triplet([12, 3], 15)	
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], [])

		result = find_triplet.get_triplet([12], 12)	
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], [])	

		#This should be an instant response as there are no elements to traverse through. It's more apparent if you uncomment DEBUG print statments.
		result = find_triplet.get_triplet([], 0)	
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], [])


	def test_counter_position_for_overlap(self):
		#Last 3 elements of an array should not be overlaped by the 3 counters
		arr=[2, 1, 5, 1, 6, 29,-6]
		result = find_triplet.get_triplet(arr, arr[-1]*3)	#arr[-1]*3 = -18
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], [])

		result = find_triplet.get_triplet(arr, arr[-2]*3)	#arr[-2]*3 = 58
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], [])

		result = find_triplet.get_triplet(arr, arr[-3]*5)	#arr[-3]*5 = 30
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], [])

		#First 3 elements of an array should not be overlaped by the 3 counters
		result = find_triplet.get_triplet(arr, arr[2]*3)	#arr[2]*3=15
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], [])

		result = find_triplet.get_triplet(arr, arr[1]*3)	#arr[2]*3=3
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], [])

		result = find_triplet.get_triplet(arr, arr[0]*3)	#arr[2]*3=6
		self.assertEqual(result[0], False)
		self.assertEqual(result[2], [])



#Keep track of where this script is being called from - directly or from an import?
if __name__ == "__main__":
  print ("*** Running from {} ***".format(__file__))
  unittest.main()
else:
  print ("*** Imported from {} ***".format(__name__))
