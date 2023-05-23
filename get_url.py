import requests
num_to_ans = {1:'https://raw.githubusercontent.com/neetcode-gh/leetcode/main/python/0001-two-sum.py'}
num_to_desc = {1:'https://leetcode.com/problems/two-sum/'}

url = 'https://github.com/neetcode-gh/leetcode/tree/main/python'
req = requests.get(url)
print(req.text)

def get_url(num):
    return (num_to_ans[num], num_to_desc[num])