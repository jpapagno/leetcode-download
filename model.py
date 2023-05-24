import os
import re
class Problem:
    def __init__(self, title, function_name):
        # '0001-two-sum'
        self.title = title
        self.function_name = function_name
        self.base_inputs = []

    def get_input_types(self):
        if len(self.base_inputs[0]) == 0:
            raise ValueError('base inputs not populated yet')
        type_list = []
        for cur_input in self.base_inputs[0]:
            type_list.append(type(cur_input))
        return type_list

    def get_num_inputs(self):
        if len(self.base_inputs[0]) == 0:
            raise ValueError('base inputs not populated yet')
        return len(self.base_inputs[0])

        
