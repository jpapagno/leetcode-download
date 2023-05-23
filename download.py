import requests
from os import getcwd

url = 'https://raw.githubusercontent.com/neetcode-gh/leetcode/main/python/0001-two-sum.py'
req = requests.get(url)

# Check if the request was successful
if not req.status_code == 200:
    print('Request failed with status code:', response.status_code)
    return

cwd = getcwd()
f = open('leetcode.py', "a")
f.write('import Arrays\nimport bisect\nimport collections\nfrom typing import List\n\n')
f.write(req.text)
f.close()