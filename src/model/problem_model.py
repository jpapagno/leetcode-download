import os
import re
import src.models.input_model as input_model
import importlib
import argparse

class Problem:
    def __init__(self, title, function_name):
        # '0001-two-sum'
        self.title = title
        self.function_name = function_name
        self.base_inputs = []
        self.base_outputs = []

        self.input_object = input_model.Input_Model()
        # the indexes allign from input to output
        self.sm_inputs = []
        self.sm_outputs = []
        self.create_sm()

    # this function will return the types of the inputs
    # example: inputs: [1, 2, 3], 2 -> [List, int]
    def get_input_types(self):
        if len(self.base_inputs[0]) == 0:
            raise ValueError('base inputs not populated yet')
        type_list = []
        for cur_input in self.base_inputs[0]:
            if type(cur_input) == list:
                if len(cur_input) == 0:
                    raise ValueError('input list has no elements')
                list_elem_type = type(cur_input[0])
            type_list.append(type(cur_input))
        return type_list

    def get_num_inputs(self):
        if len(self.base_inputs[0]) == 0:
            raise ValueError('base inputs not populated yet')
        return len(self.base_inputs[0])

    # this function will test the users code that lives in mycode against the ans's code
    def run_base_tests(self, model):
        print(model.base_inputs)
        title = model.title
        inputs = model.base_inputs
        num_inputs = model.get_num_inputs()
        function_name = model.function_name

        module = importlib.import_module(f'src.downloads.neetcode.{title}')
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
            return True
        else:
            print('you idiot')
            return False