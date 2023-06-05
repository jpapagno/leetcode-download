import requests
import os
import re
from src.helpers import mem, input_params, helper
from bs4 import BeautifulSoup

def copy_neetcode(title):
    # input is '0001'
    search_string = title
    directory = 'downloads/neetcode'

    # Iterate through all files in the directory
    success = False
    for filename in os.listdir(directory):
        # Check if the search string is present in the file name
        if search_string in filename:
            with open(f'downloads/neetcode/{filename}') as f:
                with open(f"mycode/{filename}", "w") as f1:
                    for line in f:
                        f1.write(line)
                        if "def" in line:
                            success = True
                            break
    if not success:
        raise ValueError('not success bro, could not find def')

def download_neetcode(title):
    # num_title = '0001-two-sum.py'
    directory = 'downloads/neetcode'
    py_name = title + '.py'
    # File path
    file_path = os.path.join(directory, py_name)

    neet_url = 'https://raw.githubusercontent.com/neetcode-gh/leetcode/main/python/' + py_name

    base_content = 'import Arrays\nimport bisect\nimport collections\nfrom typing import List\n\n'

    neet_response = requests.get(neet_url)

    if neet_response.status_code != 200:
        raise ValueError(f'failed to get neetcode for title: {title} \nresponse code: {neet_response.status_code}')

    neet_content = neet_response.text

    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Write the content to the file
        file.write(base_content)
        file.write(neet_content)

    # File successfully written
    print(f"Content written to {file_path}.")

def download_desc(title):
    # title = '0001-two-sum'

    num = title[:4]
    name = title[5:]

    directory = 'downloads/desc'
    # File path
    file_path = os.path.join(directory, num + '-' + name + '.txt')

    # Content to write to the file
    desc_url = 'https://leetcode.com/problems/' + name + '/'

    desc_response = requests.get(desc_url)

    if desc_response.status_code != 200:
        raise ValueError(f'failed to get description for name: {name} \nresponse code: {desc_response.status_code}')

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
