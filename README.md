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

1. find a way to download specific leetcode desc's and neetcode answers
    - curl https://github.com/neetcode-gh/leetcode/tree/main/python | grep 'title="0001'
    - This will get the title that we can slap onto the base github raw url, 
        https://raw.githubusercontent.com/neetcode-gh/leetcode/main/python/####-TITLE
        - do we slap this into a file? Do we keep this locally in a map string in 
    - maybe we have a dir that is all the ones that you've downloaded and each is in a seperate py or txt file
        - one py file for the neetcode ans
        - one txt file for the desc or maybe already parsed input
    - I like this idea, maybe an optional flag that overwrites existing files or maybe 
    - DONEEEEEE

2. parse output for basic tests
    - probably slap it into the input function
    - connect the parsed output and input to the testing function

    - create model to represent the thing that holds the parsed desc
    - model can have fields like 