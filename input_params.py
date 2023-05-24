import requests
from bs4 import BeautifulSoup
import os
import model
import mem

def correct_types(old_list):
    output_list = []
    for cur in old_list:
        try:
            output_list.append(int(cur))
            continue
        except:
            None

        if ',' in cur:
            try:
                output_list.append(list(map(int, cur.split(','))))
            except:
                output_list.append(cur.split(','))

        elif '"' in cur or "'" in cur:
            # string case
            cur = cur[1:len(cur)-1]
            output_list.append(cur)

        else:
            raise ValueError('found type I cannot convert', cur)
    return output_list


def manual_comma_split(some_input):
    inside_list = False
    ret_list = []
    working_string = ""
    # 'Input: s = [1,2,3], numRows = 3\n'
    for i, curChar in enumerate(some_input):

        if inside_list:
            if curChar == ']':
                inside_list = False
            else:
                working_string += curChar
        elif curChar == "," or i == len(some_input)-1:
            ret_list.append(working_string)
            working_string = ""
        elif curChar == '[':
            inside_list = True
        else:
            working_string += curChar
    return ret_list

def get_example_input(input_content):
    ex1_output_og_spot = input_content.find("Output:")
    ex1_input = input_content[input_content.find("Input:"):ex1_output_og_spot]

    i = ex1_output_og_spot
    while not input_content[i] == "\n":
        i += 1
    ex1_output = input_content[ex1_output_og_spot:i]

    # ABOVE IS RETURNING THIS STRING FOR THE ex1_input and ex1_output
    # ex1_input = 'Input: s = "PAYPALISHIRING", numRows = 3\n'
    # ex1_output = 'Output: "PAHNAPLSIIGYIR"'

    input_params = manual_comma_split(ex1_input)
    new_input_params = []
    for cur in input_params:
        equals_split_list = cur.split('=')
        cur_param = equals_split_list[len(equals_split_list)-1][1:].replace('\n', "")
        new_input_params.append(cur_param)

    # int: if int(cur)
    # list: if theres a comma
    # string: else
    newer_input_params = correct_types(new_input_params)
    return newer_input_params

# this function takes in a title, and parses input and output data to return a model of the problem
def get_input_params(title):
    cur_problem = model.Problem(title)

    # get contents of the title
    directory = f'downloads/desc'
    filename = f'{title}.txt'
    found_file = False
    for file in os.listdir(directory):
        if file == filename:
            found_file = True
            file_path = os.path.join(directory, file)
            with open(file_path, 'r') as file_obj:
                content = file_obj.read()
            break
    if not found_file:
        raise ValueError(f'could not find file {filename} in dir {directory}')

    # find input params
    examples = []
    for i in range(4):
        cur_example = f"Example {i+1}:"
        if cur_example in content: 
            examples.append(content.find(cur_example))
        
    for i, cur in enumerate(examples):
        if i+1 < len(examples):
            example_content = content[cur:examples[i+1]]
        else:
            example_content = content[cur:len(content)]
        cur_problem.base_inputs.append(get_example_input(example_content))

    mem.save_object(cur_problem)