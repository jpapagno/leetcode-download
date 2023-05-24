import requests
import os 
from bs4 import BeautifulSoup

def download_desc(num, title):
    # title = 'two-sum'
    directory = 'downloads/desc'

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

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

def download_neetcode(num_title):
    # num_title = '0001-two-sum.py'
    directory = 'downloads/neetcode'

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
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