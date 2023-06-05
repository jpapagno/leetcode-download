import os
import re

# this function will take in the desired type, and depth of the list (if any) and return a randomized input
def create_an_input(input_type, list_depth):
    print('hi')

class Input_Model:
    def __init__(self):
        # once populated, example input will be the leetcode Example #1 example
        # for example, for twoSum, example_input will be [[2, 7, 11, 15], 9]
        self.example_input = []
        self.sm_input = []
        self.sm_output = []

    # this function will create 10 small tests that are valid, and populate the sm_input and sm_outout feilds
    # a valid small test is one that fits within these constraints:
    # answer(input) != Null, len(list) < 3, int < 100, len(str) < 5 
    def create_sm(self):
        for i, cur in enumerate(example_input):
            cur_type = type(cur)
            list_depth = 0
            while cur_type == list:
                # increment the depth of our list that we will call later
                list_depth += 1
                # cur is now the first elem in the list
                cur = cur[0]
                # now the type that we are dealing with gets reassigned to be the elem type instead of list
                cur_type = type(cur)
            
            randomized_input = create_an_input(cur_type, list_depth)
            self.sm_input.append(randomized_input)
            self.sm_output.append(leetcode())
            


        

    