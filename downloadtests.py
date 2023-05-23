import requests
from os import getcwd

url = 'https://leetcode.com/problems/two-sum/'
req = requests.get(url)
print(req.text)
cwd = getcwd()
f = open('out.txt', "w")
f.write(req.text)
f.close()