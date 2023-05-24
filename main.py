import download
import input_params
import sys
import importlib

def main(num):
    # download the desc and neetcode
    model = download.download_num(num)
    title = model.title
    inputs = model.base_inputs
    num_inputs = model.get_num_inputs()
    success = False
    function_name = model.function_name

    module = importlib.import_module(f'downloads.neetcode.{title}')
    function = getattr(module.Solution, function_name)

    mycode_module = importlib.import_module(f'mycode.{title}')
    mycode_function = getattr(mycode_module.Solution, function_name)

    if num_inputs > 3:
        raise ValueError('over three inputs not suppported')

    success = True
    for i, cur in enumerate(inputs):

        if num_inputs == 1:
            cur_mycode = mycode_function(mycode_module.Solution, cur[0])
            neetcode_ans = function(module.Solution, cur[0])
        elif num_inputs == 2:
            cur_mycode = mycode_function(mycode_module.Solution, cur[0], cur[1])
            neetcode_ans = function(module.Solution, cur[0], cur[1])
        else:
            cur_mycode = mycode_function(mycode_module.Solution, cur[0], cur[1], cur[2])
            neetcode_ans = function(module.Solution, cur[0], cur[1], cur[2])
        print(cur_mycode)
        print(neetcode_ans)
        # if the current test case fails, add it to the failing lists
        if not cur_mycode == neetcode_ans:
            success = False
            print('hi')
    if success:
        print('Passed base example input, congrats!')
    else:
        print('you idiot')



if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Get the parameter from the command-line argument
        parameter = sys.argv[1]
        # Call the main function with the parameter
        main(parameter)
    else:
        print("No parameter provided.")
