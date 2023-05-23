# leetcode-download
Download leetcode problems to practice offline


STEPS:
1. Get already made basic tests from leetcode
2. Get the params that are passed into the function
    - maybe sting manipulation
    - maybe grep
3. Generate random tests
    - either used locally stored randomly gened tests
    - generate new random tests on the spot
4. maybe implement a timer thing so the tests will only run for a specific amt of time


todo:
1. parse output for basic tests
    - probably slap it into the input function
    - connect the parsed output and input to the testing function
2. find a way to download specific leetcode desc's and neetcode answers
    - curl https://github.com/neetcode-gh/leetcode/tree/main/python | grep 'title="0001'
    - This will get the title that we can slap onto the base github raw url, 
        https://raw.githubusercontent.com/neetcode-gh/leetcode/main/python/####-TITLE
    - 