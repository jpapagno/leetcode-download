import requests
import os
import src.downloadtests as downloadtests
import re
import src.input_params as input_params
import src.mem as mem
from bs4 import BeautifulSoup

# this is the file that will grep for the title's when passed in a number
#   - input: number
#   - output: downloaded desc and neetcode ans


# this function will look in the src/downloads/neetcode folder to find the solution
# and copy the function definition and place it in the user's code section
def copy_neetcode(num):
    # input is '0001'
    search_string = num
    directory = 'src/downloads/neetcode'

    # Iterate through all files in the directory
    success = False
    for filename in os.listdir(directory):
        # Check if the search string is present in the file name
        if search_string in filename:
            with open(f'src/downloads/neetcode/{filename}') as f:
                with open(f"mycode/{filename}", "w") as f1:
                    for line in f:
                        f1.write(line)
                        if "def" in line:
                            success = True
                            break
    if not success:
        raise ValueError('not success bro, could not find def')

# returns file name if present, else None
def is_filename_in_downloads(directory, num):
    search_string = num
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the search string is present in the file name
        if search_string in filename:
            filename_without_extension = os.path.splitext(filename)[0]
            return filename_without_extension
    return None

def download_num(input_val):
    # input_val = 1

    if type(input_val) != str:
        input_val = str(input_val) 

    while len(input_val) < 4:
        input_val = '0' + input_val

    # before we do any downloading, lets check to see if we already have the desc and neetcode ans downloaded
    # this will allow us to do the same commands whether we're online or offline
    desc_title = is_filename_in_downloads("src/downloads/desc", input_val)
    neet_title = is_filename_in_downloads("src/downloads/neetcode", input_val)
    pickle_title = is_filename_in_downloads('src/downloads/pickles', input_val)
    mycode_title = is_filename_in_downloads('mycode', input_val)

    # case where we have no need to go online and download shit
    if desc_title and neet_title and pickle_title:
        # case that the mycode py file is not present, we need to copy it from neetcode
        if not mycode_title:
            copy_neetcode(input_val)
        print('desc and neet already downloaded, returning saved object')
        return mem.load_object(f'src/downloads/pickles/{pickle_title}')
    
    # Send a GET request to the desired URL
    response = requests.get('https://github.com/neetcode-gh/leetcode/tree/main/python')

    # Get the response text
    response_text = response.text

    # Define the pattern to search for
    pattern = 'title="' + input_val

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

    num_title = response_text[start_index+7:end_index-3]
    title = num_title[5:len(num_title)]

    # check if desc already exists for title, if not, download it
    # print(f'{input_val}-{title}.txt')
    if not os.path.exists(f'src/downloads/desc/{num_title}.txt'):
        downloadtests.download_desc(input_val, title)
    
    # check if neetcode already exists for title, if not, download it
    # print(num_title)
    if not os.path.exists(f'src/downloads/neetcode/{num_title}.py'):
        downloadtests.download_neetcode(num_title, 'src/downloads/neetcode')

    if not mycode_title:
        copy_neetcode(input_val)

    if not os.path.exists(f'src/downloads/pickles/{num_title}.pickle'):
        input_params.get_input_params(num_title)
        
    return mem.load_object(f'src/downloads/pickles/{num_title}')
    # return (f'{input_val}-{title}')

    def download_desc(num, title):
    # title = 'two-sum'
    directory = 'src/downloads/desc'
    # File path
    file_path = os.path.join(directory, num + '-' + title + '.txt')

    # Content to write to the file
    desc_url = 'https://leetcode.com/problems/' + title + '/'

    desc_response = requests.get(desc_url)

    if desc_response.status_code != 200:
        raise ValueError(f'failed to get description for title: {title} \nresponse code: {desc_response.status_code}')

    # Parse the HTML content
    soup = BeautifulSoup(desc_response.content, 'html.parser')

    # Find the content
    desc_content = soup.find('div', class_='_1l1MA').get_text()

    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Write the content to the file
        file.write(desc_content)

    # File successfully written
    print(f"Content written to {file_path}.")

def download_neetcode(num_title, directory):
     # num_title = '0001-two-sum.py'

    py_name = num_title + '.py'
    # File path
    file_path = os.path.join(directory, py_name)

    neet_url = 'https://raw.githubusercontent.com/neetcode-gh/leetcode/main/python/' + py_name

    base_content = 'import Arrays\nimport bisect\nimport collections\nfrom typing import List\n\n'

    neet_response = requests.get(neet_url)

    if neet_response.status_code != 200:
        raise ValueError(f'failed to get neetcode for title: {num_title} \nresponse code: {neet_response.status_code}')

    neet_content = neet_response.text

    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Write the content to the file
        file.write(base_content)
        file.write(neet_content)

    # File successfully written
    print(f"Content written to {file_path}.")

def download_desc(num, title):
    # title = 'two-sum'
    directory = 'downloads/desc'
    # File path
    file_path = os.path.join(directory, num + '-' + title + '.txt')

    # Content to write to the file
    desc_url = 'https://leetcode.com/problems/' + title + '/'

    desc_response = requests.get(desc_url)

    if desc_response.status_code != 200:
        raise ValueError(f'failed to get description for title: {title} \nresponse code: {desc_response.status_code}')

    # Parse the HTML content
    soup = BeautifulSoup(desc_response.content, 'html.parser')

    # Find the content
    desc_content = soup.find('div', class_='_1l1MA').get_text()

    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Write the content to the file
        file.write(desc_content)

    # File successfully written
    print(f"Content written to {file_path}.")