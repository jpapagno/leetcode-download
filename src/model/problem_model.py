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

    # this function will test the users code that lives in mycode against the ans's code
    def run_base_tests(self):
        num_inputs = self.input_amt

        mycode_module = importlib.import_module(f'mycode.{self.title}')
        mycode_function = getattr(mycode_module.Solution, self.function_name)

        if num_inputs > 3:
            raise ValueError('over three inputs not suppported')

        success = True
        for i, cur in enumerate(self.base_inputs):
            neetcode_ans = self.base_outputs[i]
            if num_inputs == 1:
                cur_mycode = mycode_function(mycode_module.Solution, cur[0])
            elif num_inputs == 2:
                cur_mycode = mycode_function(mycode_module.Solution, cur[0], cur[1])
            else:
                cur_mycode = mycode_function(mycode_module.Solution, cur[0], cur[1], cur[2])
            print(cur_mycode)
            print(neetcode_ans)
            # if the current test case fails, add it to the failing lists
            if not cur_mycode == neetcode_ans:
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
        if not self.base_inputs:
            raise ValueError('base inputs must be populated before base outputs get populated')
        num_inputs = self.input_amt

        module = importlib.import_module(f'downloads.neetcode.{self.title}')
        function = getattr(module.Solution, self.function_name)

        if num_inputs > 3:
            raise ValueError('over three inputs not suppported')

        for i, cur in enumerate(self.base_inputs):
            if num_inputs == 1:
                neetcode_ans = function(module.Solution, cur[0])
            elif num_inputs == 2:
                neetcode_ans = function(module.Solution, cur[0], cur[1])
            else:
                neetcode_ans = function(module.Solution, cur[0], cur[1], cur[2])
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

