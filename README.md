# leetcode-download
Download leetcode problems to practice a given problem offline


Venv notes-
    - its in the myenv dir
    - activate with 'source myenv/bin/activate'
    - deactivate with 'deactivate'

Right now this only supports leetcode problems that fit the following specs:
- are in neetcode list
- only use lists, strings, or ints as inputs
- only python

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
    - DONEEEEE

3. Main
    - when main is called for the first time, create a file that is exactly the solution in another foldert that the user will code in
    - then main will call that file to test against your code
    - This will allow the user to work on multiple problems at the same time
    - This will also give the user the starting code for the problem
        - the class and the function and any other boilerplate
    - and we have a reset.py NUM that will reset the user's file to its og state, in case you accidently got rid of the function and input code
    - DONEEEE

4. todo still
    - create random tests baised on inputs to really test the code
    - create a more streamlined main method/ create a binary that you make calls to
    - implement a problem search feature
        - this would run through neetcode's github thing that shows the user the possible problems the user can select
    - implement a console promt thing and more clean terminal command
        - imeplement a front end that allows user to click buttons to do the commands

- Steamlined main method:
    - make main take in the command that you want to use
    - commands:
        - download NUM : download desc, neetcode, and create pickle
        - run NUM : run mycode NUM against neetcode NUM on base tests
            - add error msg if code hasnt been downloaded yet
        - run -full NUM : run mycode NUM against neetcode NUM on random tests
        - download NUM -rm : delete that num's desc, neetcode, pickle, and mycode
        - reset NUM : reset mycode of that number to be blank again
        - status NUM : display user's status of number
            - is currently downloaded
            - availble to download from neetcode
            - has completed base tests in the past
            - has completed full tests in the past
    - DONEEE

* still todo:
    - create script to create lists and string of size 3, ints of size _, and test on actual until we get a certain amount of non-null tests
    - small: create script to create lists, strings, and ints with an upper constraint of what the example tests are
        - test runtime against small and provide an insite to how your code is doing against small inputs
    - medium: double the upper constraint of the example tests
    - large: test runtime on these

* notes:
    - create randomized sm, md, lg datasets to test actual vs expected results
        - should I have predefined datasets or have the problem create its own per problem
            - Maybe at the time of downloading, I can add a field in the model to be the sm, md, lg randomized datasets with the answer 
                - if the answer is None, then remove the test meaning we gave it an input that is beyond its constraint
                - I like this because it creates a long download time, but it shortens the time it would take to run the full tests bc we already know the ans and dont need to run ans's code
        - I could parse the constraints from the desc
            
        


tickets:
    - implement full tests
    - implement time complexity test
    - clean up code design + add comments
    - fix parsing input bug for lists with strings
        - lists of strings will be read in like this: ['"hi"'], notice the extra quotes