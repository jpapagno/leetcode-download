import os
import re
from src.model import input_model
from src.helpers import helper, input_params, mem, download
import importlib
import argparse

class Problem:
    def __init__(self, num):
        # self.title example: '0001-two-sum'
        self.title = helper.get_title(num)

        # create some download folders if they do not exist already
        helper.create_download_dir()
        self.download_all()

        self.function_name = helper.get_function_name(self.title)
        
        self.base_inputs = []
        self.populate_base_inputs()
        # number of inputs this problem uses
        self.input_amt = len(self.base_inputs[0])

        self.base_outputs = []
        self.populate_base_outputs()

        mem.save_object(self)

        self.input_object = input_model.Input_Model()
        # the indexes allign from input to output
        self.sm_inputs = []
        self.sm_outputs = []
        self.populate_sm_tests()

    # this function will test the users code that lives in mycode against the ans's code
    def run_base_tests(self):
        success = True
        for i, cur in enumerate(self.base_inputs):
            neetcode_ans = self.base_outputs[i]
            my_ans = helper.run_function(cur, self.title, self.function_name, False)
            # if the current test case fails, add it to the failing lists
            if my_ans == neetcode_ans:
                print('\u2713' + f" PASS: {cur} -> {my_ans}")
            else:
                print('\u2716' + f" FAIL:")
                print(f'Actual: {cur} -> {my_ans}')
                print(f'Expected: {cur} -> {neetcode_ans}')
                success = False
        if success:
            print('Passed base example input, congrats!')
            return True
        else:
            print('you idiot')
            return False

    def run_full_tests(self):
        print('RUNNING FULLLLL TESTS INSIDE OF THE PROBLEM BABY')

    def populate_base_inputs(self):
        # get contents of the title
        directory = f'downloads/desc'
        filename = f'{self.title}.txt'
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
            # add the parsed input to the base_inputs
            self.base_inputs.append(input_params.get_example_input(example_content))

    def populate_base_outputs(self):
        for i, cur in enumerate(self.base_inputs):
            neetcode_ans = helper.run_function(cur, self.title, self.function_name, True)
            self.base_outputs.append(neetcode_ans)
        if not len(self.base_inputs) == len(self.base_outputs):
            raise ValueError('base input len does not match base output len')

    def download_all(self):
        if not os.path.exists(f'downloads/desc/{self.title}.txt'):
            download.download_desc(self.title)
    
        if not os.path.exists(f'downloads/neetcode/{self.title}.py'):
            download.download_neetcode(self.title)

        if not os.path.exists(f'mycode/{self.title}.py'):
            download.copy_neetcode(self.title)

    def populate_sm_tests(self):

        counter = 0
        for i in range(100):

            cur_input = helper.create_sm_input(self)
            neetcode_ans = helper.run_function(cur_input, self.title, self.function_name, True)
            
            if counter >= 10:
                break
