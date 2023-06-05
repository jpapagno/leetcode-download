import sys
import importlib
import argparse
from src.helpers import download, input_params, helper, mem
from src.model import problem_model
import os

class Controller:
    def __init__(self, args): 
        if not args.num:
            raise ValueError('failed to provide num')

        self.args = args
        title = helper.get_title(args.num)
        # if the pickled object already exists, we have already downloaded this problem
        if os.path.exists(f'downloads/pickles/{title}.pickle'):
            print('FOUND PICKLE!')
            self.model = mem.load_object(f'downloads/pickles/{title}')
        else:
            print('using that precise wifi')
            # else we need to create a new Problem (download it from internet)
            self.model = problem_model.Problem(args.num)

    def main(self):
        if self.args.command == 'run':
            passed = False
            if self.args.full:
                self.model.run_full_tests()
            else:
                if self.model.run_base_tests():
                    self.maybe_full_tests()
        elif self.args.command == 'delete':
            self.model.delete_command()
        elif self.args.command == 'reset':
            self.model.reset_command()
        elif self.args.command == 'status':
            self.model.status_command()

    def maybe_full_tests(self):
        count = 0
        while count < 3:
            answer = input('Base tests have passed, would you like to run full tess? (y/n): ')
            if answer.lower() == 'y':
                self.model.run_full_tests()
                return
            if answer.lower() == 'n':
                sys.exit()
                return
            print("Invalid input. Please enter 'y' or 'n'.")
            count += 1
        return