import requests
from bs4 import BeautifulSoup

def manual_comma_split(some_input):
    inside_list = False
    ret_list = []
    working_string = ""
    # 'Input: s = [1,2,3], numRows = 3\n'
    for i, curChar in enumerate(some_input):

        if inside_list:
            if curChar == ']':
                inside_list = False
            else:
                working_string += curChar
        elif curChar == "," or i == len(some_input)-1:
            ret_list.append(working_string)
            working_string = ""
        elif curChar == '[':
            inside_list = True
        else:
            working_string += curChar
    return ret_list



# Define the URL of the LeetCode problem
url = 'https://leetcode.com/problems/zigzag-conversion/'

# Send GET request to retrieve the HTML content
response = requests.get(url)

# Check if the request was successful
# if not response.status_code == 200:
#     print('Request failed with status code:', response.status_code)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the content
content = soup.find('div', class_='_1l1MA').get_text()

# find input params
example1 = content.find("Example 1:") if "Example 1:" in content else 0
example2 = content.find("Example 2:") if "Example 2:" in content else 0
example3 = content.find("Example 3:") if "Example 3:" in content else 0
example4 = content.find("Example 4:") if "Example 4:" in content else 0

example1 = content[example1:example2]
ex1_output_og_spot = example1.find("Output:")
ex1_input = example1[example1.find("Input:"):ex1_output_og_spot]

i = ex1_output_og_spot
while not example1[i] == "\n":
    i += 1
ex1_output = example1[ex1_output_og_spot:i]
print(ex1_input)
print(ex1_output)

# ABOVE IS RETURNING THIS STRING FOR THE ex1_input and ex1_output
# ex1_input = 'Input: s = "PAYPALISHIRING", numRows = 3\n'
# ex1_output = 'Output: "PAHNAPLSIIGYIR"'

input_params = manual_comma_split(ex1_input)
print(input_params)
new_input_params = []
for cur in input_params:
    equals_split_list = cur.split('=')
    cur_param = equals_split_list[len(equals_split_list)-1][1:].replace('\n', "")
    new_input_params.append(cur_param)
print(new_input_params)

# int: if int(cur)
# list: if theres a comma
# string: else
newer_input_params = []
for cur in new_input_params:
    
    try:
        newer_input_params.append(int(cur))
        print('this is now an int:', cur)
        continue
    except:
        None
    
    if ',' in cur:
        try:
            newer_input_params.append(list(map(int, cur.split(','))))
            continue
        except:
            newer_input_params.append(cur.split(','))
            continue
    if '"' in cur or "'" in cur:
        # string case
        cur = cur[1:len(cur)-1]
        newer_input_params.append(cur)

for cur in newer_input_params:
    print(cur, type(cur))
return newer_input_params