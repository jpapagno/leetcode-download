import download
import input_params
import sys
import downloads/neetcode

def main(num):
    # download the desc and neetcode
    model = download.download_num(num)
    print(model.get_input_types())

    inputs = model.get_example_input
    success = False
    for i, cur in enumerate(inputs):
        cur_mycode = mycode.twoSum(cur[0], cur[1])
        neetcode_ans
        mycode_ans = 
        # if the current test case fails, add it to the failing lists
        if not cur_base == cur_mycode:
            success = False
            failed_tests.append(cur)
            failed_tests_base.append(cur_base)
            failed_tests_mycode.append(cur_mycode)

    # for i in range(len(failed_tests)):
    #     print('Current test case that is failing:', failed_tests[i])
    #     print('Expected result:', failed_tests_base[i])
    #     print('mycode result:', failed_tests_mycode[i])
    # # print(base_output)
    # # print(mycode_out)
    # print('Does my code work?:', success)
    # # my_list = [1, 2, 3, 4, 5]
    # # my_number = 5
    # # print(main(my_list, my_number))



if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Get the parameter from the command-line argument
        parameter = sys.argv[1]
        # Call the main function with the parameter
        main(parameter)
    else:
        print("No parameter provided.")
