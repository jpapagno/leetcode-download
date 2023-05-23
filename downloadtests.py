import requests
import os 
from bs4 import BeautifulSoup



directory = 'downloads/desc'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# File path
file_path = os.path.join(directory, 'two-sum.txt')

# Content to write to the file
url = 'https://leetcode.com/problems/two-sum/'

response = requests.get(url)
# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the content
content = soup.find('div', class_='_1l1MA').get_text()


# Open the file in write mode
with open(file_path, 'w') as file:
    # Write the content to the file
    file.write(content)

# File successfully written
print(f"Content written to {file_path}.")