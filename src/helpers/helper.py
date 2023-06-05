
import sys
import importlib
import argparse
import requests
import os
import re

# returns the leetcode, {title}.py's answer for the input
# input_list : the inputs for the function, example: [[1,2,3], 3] 
def return_output(input_list, title, function_name):
    num_inputs = len(input_list)

    module = importlib.import_module(f'downloads.neetcode.{title}')
    function = getattr(module.Solution, function_name)

    if num_inputs > 3:
        raise ValueError('over three inputs not suppported')

    if num_inputs == 1:
        return function(module.Solution, cur[0])
    elif num_inputs == 2:
        return function(module.Solution, cur[0], cur[1])
    else:
        return function(module.Solution, cur[0], cur[1], cur[2])

def get_title(num):
    if type(num) != str:
        num = str(num) 
    
    while len(num) < 4:
        num = '0' + num
    
    # Send a GET request to the desired URL
    response = requests.get('https://github.com/neetcode-gh/leetcode/tree/main/python')

    # Get the response text
    response_text = response.text

    # Define the pattern to search for
    pattern = 'title="' + num

    # Search for the pattern in the response text using regex
    matches = re.finditer(pattern, response_text)

    # Print the matches
    flag = False
    for match in matches:
        flag = True
        start_index = match.start()
        end_index = match.end()

    # this will error out if it cant find the problem in the neetcode github
    if not flag:
        raise ValueError(f'failed to find title: {pattern} from neetcode god')


    while response_text[end_index-3:end_index] != '.py':
        end_index+=1

    return response_text[start_index+7:end_index-3]

def get_function_name(title):
    directory = f'downloads/neetcode'
    neet_title = f'{title}.py'
    for filename in os.listdir(directory):
        # Check if the search string is present in the file name
        if neet_title == filename:
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file_obj:
                content = file_obj.read()
            break

    # Define the pattern to search for
    pattern = 'def'

    # Search for the pattern in the response text using regex
    matches = re.finditer(pattern, content)
    for match in matches:
        start_index = match.start()
        end_index = match.end()

    while content[end_index] != '(':
        end_index += 1

    return content[start_index+4:end_index]

def setup_parser():
    parser = argparse.ArgumentParser(description='Example command-line tool')

    subparsers = parser.add_subparsers(dest='command', metavar='COMMAND')
    subparsers.required = True

    run_parser = subparsers.add_parser('run', help='Run mycode against neetcode')
    run_parser.add_argument('num', type=int, help='The number')
    run_parser.add_argument('-full', action='store_true', help='Run on random tests')

    delete_parser = subparsers.add_parser('delete', help='Delete desc, neetcode, pickle, and mycode')
    delete_parser.add_argument('num', type=int, help='The number')
    delete_parser.add_argument('-rm', action='store_true', help='Remove files')

    reset_parser = subparsers.add_parser('reset', help='Reset mycode to blank')
    reset_parser.add_argument('num', type=int, help='The number')

    status_parser = subparsers.add_parser('status', help='Display user status')
    status_parser.add_argument('num', type=int, help='The number')

    args = parser.parse_args()
    return args

def create_download_dir():
    dirs = ['downloads', 'downloads/pickles', 'downloads/neetcode', 'downloads/desc', 'mycode']
    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)