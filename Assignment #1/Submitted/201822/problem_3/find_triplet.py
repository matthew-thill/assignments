#!/usr/bin/env python3
'''
***  Assignment - Problem Set #3: The Solution
3: Find a triplet that sum to a given value X.
Write a function to find if there is a triplet in integer array whose sum is equal to the given value x. If there is such a triplet present in array, then print the triplet and return true. Else return false. Just print first triplet if there are multiple triplets matching value x.

Example:
    I/P : array [12, 3, 4, 1, 6, 9,-6] and given sum x =24 
    O/P : (12, 3 and 9)
'''

#Function: get_triplet
#INPUT: Takes in an array of integers and a sum value, 'x'. E.g. [12, 3, 4, 1, 6, 9,-6], and a sum value - 'x' (e.g. sum x=24)
#OUTPUT: Returns a list '[boolean, the message, an array of triplet): 
#   get_triplet(arr)[0]: Boolean - True or False if a triplet exists
#   get_triplet(arr)[1]: Exact message displayed when found or not.
#   get_triplet(arr)[2]: An array of triplet if one exists; if no triplet exists return an empty array

def get_triplet (arr, sum_x):
    print("\n\nFor ARRAY SOURCE: {}, SUM X=\"{}\":".format(arr,sum_x))

    #Flag initially set to not found - e.g. False.
    is_triplet = False

    #We have an outer loop and 2 inner loop indexes, and they should never overlap. So when we reach the end of an 
    #array (e.g. the last element in the array) the outer loop would never point to the last element as it will 
    #always be two less - e.g. outer loop index would be 'n-2', while mid loop index is 'n-1' and inner loop index is 'n'. 
    #e.g. outer loop index would never point to the last two elements.
    for outer_loop_index in range(0, len(arr) - 2):
#        print("*** DEBUGGING: outer_loop_index: "+str(arr[outer_loop_index]))

        #Mid loop should shrink from the left as the offset of outer_loop_index moves one index over to the right.
        #Mid loop index should never point to the last element of an array.
        for mid_loop_index in range(outer_loop_index + 1, len(arr) - 1):
#            print("\t*** DEBUGGING: mid_loop_index: "+str(arr[mid_loop_index]))

            #Inner loop: traverse through the array to verify if the sum of three indexes (e.g. outer, mid & inner) make up a triplet
            #for inner_loop_index in range (outer_loop_index + 2, len(arr)):
            for inner_loop_index in range (mid_loop_index + 1, len(arr)):
#                print("\t\t*** DEBUGGING: inner_loop_index: {} remaining to verify in inner loop: {}".format(arr[inner_loop_index], arr[inner_loop_index:]))
                #Add up all 3 values from each of the 3 different positions/index.
                triplet_sum = arr[outer_loop_index] + arr[mid_loop_index] + arr[inner_loop_index]
                if (triplet_sum == sum_x):
#                    print("\t\t\t*** DEBUGGING: TRIPLET FOUND!!! ***")
                    msg = "[{},{} and {}] are TRIPLET for the given sum x={} in the array: {}".format(arr[outer_loop_index], arr[mid_loop_index], arr[inner_loop_index], sum_x, arr)
                    print ("\t\t\t=>RESULT: {}".format(msg))

                    is_triplet = True
                    #no need to traverse through the loops if the first triplet has been found!
                    return [is_triplet, msg, [arr[outer_loop_index], arr[mid_loop_index], arr[inner_loop_index]]]


    #If no triplet found, display not found message for the corresponding array and sum, x.
    if not is_triplet:
        msg = "No triplet found for the sum x={} in the array: {}".format(sum_x, arr)
        print ("\t\t\t=>RESULT: {}".format(msg))
    #return [is_triplet, msg, [arr[outer_loop_index], arr[mid_loop_index], arr[inner_loop_index]]]

    #For consistancey we need a 3rd element [2], even if we find no triplet, we must be aware '[]' is just a place holder 
    #Especially since element [0] has been flagged as False - no triplet exist in the array.
    return [is_triplet, msg, []]


# Local script test only. Please see UnitTest for comprehensive coverage.
def main():
    print ("Testing Started...\n")
    get_triplet([12, 3, 4, 1, 6, 9,-6], 24)
    get_triplet([12, 3, 4, 1, 6, 9,-6], 200)


#Keep track of where this script is being called from - directly or from an import.
if __name__ == "__main__":
  print ("*** Running from {} ***".format(__file__))
  main()
else:
  print ("*** Imported from {} ***".format(__name__))
