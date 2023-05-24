class Problem:
    def __init__(self, title):
        # '0001-two-sum'
        self.title = title
        self.base_inputs = []

    def get_input_types(self):
        if len(self.base_inputs[0]) == 0:
            raise ValueError('base inputs not populated yet')
        type_list = []
        for cur_input in self.base_inputs[0]:
            type_list.append(type(cur_input))
        return type_list

