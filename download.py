import requests
import os
import downloadtests
import re
import input_params
import mem
# this is the file that will grep for the title's when passed in a number
#   - input: number
#   - output: downloaded desc and neetcode ans

# returns file name if present, else None
def is_filename_in_downloads(folder, num):
    directory = f'downloads/{folder}'
    search_string = num

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the search string is present in the file name
        if search_string in filename:
            filename_without_extension = os.path.splitext(filename)[0]
            print(f"Found matching file: {filename_without_extension}")
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
    desc_title = is_filename_in_downloads("desc", input_val)
    neet_title = is_filename_in_downloads("neetcode", input_val)
    pickle_title = is_filename_in_downloads('pickles', input_val)
    if desc_title and neet_title and pickle_title:
        print(pickle_title)
        print('desc and neet already downloaded, returning title')
        return mem.load_object(f'downloads/pickles/{pickle_title}')
    
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
    print(num_title, title)

    # check if desc already exists for title, if not, download it
    # print(f'{input_val}-{title}.txt')
    if not os.path.exists(f'downloads/desc/{num_title}.txt'):
        downloadtests.download_desc(input_val, title)
    
    # check if neetcode already exists for title, if not, download it
    # print(num_title)
    if not os.path.exists(f'downloads/neetcode/{num_title}.py'):
        downloadtests.download_neetcode(num_title)

    if not os.path.exists(f'downloads/pickles/{num_title}.pickle'):
        input_params.get_input_params(num_title)
        
    return mem.load_object(f'downloads/pickles/{num_title}')
    # return (f'{input_val}-{title}')