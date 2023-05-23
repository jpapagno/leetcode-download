import Arrays
import bisect
import collections
from typing import List
import mycode
import download
import leetcode

def main(lst, num):
    # Create an instance of the Solution class
    solution = leetcode.Solution()

    # Call the process_list function inside the Solution class
    return solution.twoSum(lst, num)

if __name__ == '__main__':
    # Example usage
    test_lists = tests.getLists(0, )
    test_inputs = [([1, 2, 3, 4, 5], 5), ([1, 2], 0)]
    # base_output = []
    # mycode_out = []

    failed_tests = []
    failed_tests_base = []
    failed_tests_mycode = []
    success = True
    for i, cur in enumerate(test_inputs):
        cur_base = main(cur[0], cur[1])
        cur_mycode = mycode.twoSum(cur[0], cur[1])
        # base_output.append(cur_base)
        # mycode_out.append(cur_mycode)
        # if the current test case fails, add it to the failing lists
        if not cur_base == cur_mycode:
            success = False
            failed_tests.append(cur)
            failed_tests_base.append(cur_base)
            failed_tests_mycode.append(cur_mycode)

    for i in range(len(failed_tests)):
        print('Current test case that is failing:', failed_tests[i])
        print('Expected result:', failed_tests_base[i])
        print('mycode result:', failed_tests_mycode[i])
    # print(base_output)
    # print(mycode_out)
    print('Does my code work?:', success)
    # my_list = [1, 2, 3, 4, 5]
    # my_number = 5
    # print(main(my_list, my_number))