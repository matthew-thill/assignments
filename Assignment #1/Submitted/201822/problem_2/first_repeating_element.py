#!/usr/bin/env python3
'''
***  Assignment - Problem Set #2: The Solution
2: Find the first repeating element in an array of integers
Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest.

Example:
    I/P: arr=[100,5,3,1,0,5,-8]
    O/P: 5 [5 is the first element that repeats]
'''

#Function: find_first_repeating_number
#INPUT: Takes in an array of integers. e.g. [100,5,3,1,0,5,-8]
#OUTPUT: Returns a list '[boolean, the message, the repeating #): 
#   find_first_repeating_number(arr)[0]: Boolean - True or False if a repeating number found.
#   find_first_repeating_number(arr)[1]: Exact message displayed when found or not.
#   find_first_repeating_number(arr)[2]: Repeating # found; if no repeat #, use empty str (''); if find_first_repeating_number(arr)[0] is True, return #.
def find_first_repeating_number(arr):
    print("\n\nARRAY SOURCE: \t{}".format(arr))

    #Flag initially set to not found - e.g. False.
    is_repeating = False

    #Outer loop index, "ref_index" (or ref. counter) used as a point of reference to compare against inner loop.
    #We have an outer loop and an inner loop index, and they should never overlap. So when we reach the end of an 
    #array (e.g. the last element in the array) the outer loop would never point to the last element as it will 
    #always be one less - e.g. outer loop index/counter would be 'n-1' (when we get to the last cycle in the loops) 
    # when inner loop index/counter is 'n'.
    for ref_index in range(0, len(arr) - 1):
#        print("\n*** DEBUGGING: ref_index: "+str(arr[ref_index]))

        #Inner loop: traverses through the array to verify if there is a matching number w/ the outer loop index
        #Inner loop should shrink from the left as the offset of ref_index moves one index over to the right.
        for current_index in range (ref_index + 1, len(arr)):
#            print("\t*** DEBUGGING: current_index: "+str(arr[current_index])+"\n\t\t\tremaining to verify in inner loop: "+(str(arr[current_index:])))

            #MATCH: When the reference index value and the current index value in the inner loop are the same.
            if (arr[ref_index] == arr[current_index]):
#                print("\n\t\t*** DEBUGGING: REPEATING NUMBER FOUND!!! ***")
                msg = "\t=>RESULT: {} is the first element that repeats".format(arr[current_index])
                print (msg)
                is_repeating = True
                #no need to traverse through the loops as the first repeating element has been found!
                return [is_repeating, msg, arr[current_index]]

    if not is_repeating:    #If no repeating integers found display not found msg.
        msg = "\t=>RESULT: No repeating element was found in the array."
        print (msg)
    
    #For consistancey we need a 3rd element [2], even if we find no repeating number, we must be aware '' is just a placeholder and not 
    #actually the repeating #. Especially since element [0] has been flagged as False - no repeat found in the array.
    return [is_repeating, msg, '']  


# Local script test only. Please see UnitTest for comprehensive coverage.
def main():
    print ("Testing Started...\n")
    find_first_repeating_number([100,5,3,1,0,5,-8])
    find_first_repeating_number([0,1,2,3,4,5,6,7,8,9,10,100])


#Keep track of where this script is being called from - directly or from an import.
if __name__ == "__main__":
  print ("*** Running from {} ***".format(__file__))
  main()
else:
  print ("*** Imported from {} ***".format(__name__))