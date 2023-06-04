

# returns the leetcode, {title}.py's answer for the input
# input_list : the inputs for the function, example: [[1,2,3], 3] 
def return_output(input_list, title, function_name):
    num_inputs = len(input_list)

    module = importlib.import_module(f'src.downloads.neetcode.{title}')
    function = getattr(module.Solution, function_name)

    if num_inputs > 3:
        raise ValueError('over three inputs not suppported')

    if num_inputs == 1:
        return function(module.Solution, cur[0])
    elif num_inputs == 2:
        return function(module.Solution, cur[0], cur[1])
    else:
        return function(module.Solution, cur[0], cur[1], cur[2])