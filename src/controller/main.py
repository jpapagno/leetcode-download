import src.download as download
import src.input_params as input_params
import sys
import importlib
import argparse

# will download stuff and return the model that pickle grabs or creates
def download_command(num):
    print(f"Downloading desc, neetcode, and creating pickle for number {num}")
    return download.download_num(num)

# will return true or false if the user has passed all of the example tests 
def run_base_tests(model):
    return model.run_base_tests(model)

def run_full_tests(model):
    print(model.get_input_types())
    print(f"FULLLLLLLL TESTSSSS")

def maybe_full_tests(model):
    count = 0
    while count < 3:
        answer = input('Base tests have passed, would you like to run full tess? (y/n): ')
        if answer.lower() == 'y':
            run_full_tests(model)
            return
        if answer.lower() == 'n':
            sys.exit()
            return
        print("Invalid input. Please enter 'y' or 'n'.")
        count += 1
    return

def delete_command(num):
    print(f"Deleting desc, neetcode, pickle, and mycode for number {num}")

def reset_command(num):
    print(f"Resetting mycode of number {num} to be blank again")

def status_command(num):
    print(f"Displaying user's status of number {num}")

def main():
    parser = argparse.ArgumentParser(description='Example command-line tool')

    subparsers = parser.add_subparsers(dest='command', metavar='COMMAND')
    subparsers.required = True

    download_parser = subparsers.add_parser('download', help='Download desc, neetcode, and create pickle')
    download_parser.add_argument('num', type=int, help='The number')

    run_parser = subparsers.add_parser('run', help='Run mycode against neetcode')
    run_parser.add_argument('num', type=int, help='The number')
    run_parser.add_argument('-full', action='store_false', help='Run on random tests')

    delete_parser = subparsers.add_parser('delete', help='Delete desc, neetcode, pickle, and mycode')
    delete_parser.add_argument('num', type=int, help='The number')
    delete_parser.add_argument('-rm', action='store_true', help='Remove files')

    reset_parser = subparsers.add_parser('reset', help='Reset mycode to blank')
    reset_parser.add_argument('num', type=int, help='The number')

    status_parser = subparsers.add_parser('status', help='Display user status')
    status_parser.add_argument('num', type=int, help='The number')

    args = parser.parse_args()

    if args.command == 'download':
        download_command(args.num)
    elif args.command == 'run':
        model = download_command(args.num)
        passed = False
        if args.full:
            passed = run_base_tests(model)
        else:
            run_full_tests(model)
        if passed:
            maybe_full_tests(model)
    elif args.command == 'delete':
        delete_command(args.num)
    elif args.command == 'reset':
        reset_command(args.num)
    elif args.command == 'status':
        status_command(args.num)

if __name__ == '__main__':
    main()