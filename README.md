# Assignment

This is a QA Assignment to automate Sennder Sprintboard.

## Pre-requisites 

The only pre-requisites are:
- Install Python3.7 or higher 
- Install pip latest version 
- Install chrome

You don't need any IDE to run this assignment. It can be run from your system's command-line

## Steps for installation
### Step 1: clone git repo
Open the command-line and clone the git repo
```
git clone git@github.com:priya-sachdeva/sennder-assignment.git
```

###Step 2: install requirements.txt
Point the command-line to the root folder (i.e. *sennder-assignment*) and run this command:
```
pip3 install -r requirements.txt
```

###Step 3: Run tests
> NOTE: Please get in touch with *Vaughn Morgan* from the Sennder recruiting team for the password for the user. It's mentioned in the assignment pdf 

Run the following command to execute the tests:
```
USER_NAME="sennderqa3@gmail.com"  PWD=<pwd-in-double=quotes> pytest
```
so, let's say if the password is **asdR#!asd&Pnh%**, then the command should be:
```
USER_NAME="sennderqa3@gmail.com"  PWD=asdR#!asd&Pnh% pytest
```
## Description
The main components of the framework are:
- pytest
- selenium
- chromedriver

Because of lack of time, I have used only chrome as the browser to run the tests.

### Workflow
pytest takes care of most of the stuff in itself so there is very little amount of pre-requisites that need to be done

1. **pytest.ini**

    This file can be used to configure pytest (base_url, tests path etc). 
    I have used this file specify the path where the test files - that are to be executed - are kept
   

2. **conftest.py**

    This file is used store general setup and teardown for your test execution. For example, I have used this file to: 
    - open the browser before the test execution begins
    - close the browser once the test execution is complete
    
    **NOTE**: To spend moderate amount of time and keeping the assignment simple, the functions to activate and quit the browser, are in the same file as the main functions. An alternative to this could be that we create a separate ```utils```directory to store all setup and teardown functions


3. **data**
    
    I have used this directory to store selectors in a python file. We can also create a separate python file in this directory to store other static data, like
    - store credentials
    - store test data
    etc.


4. **functions**

    This is the main directory that contains all the functions to be executed. Webdriver is instantiated in this file, which is then used in all functions to execute the logic


5. **tests**

    This is the directory that contains the test to be executed. Consider this quivalent to the test cases you would have for manual testing

## Thank You!
Thank you for the opportunity. It was fun doing the assignment.

In case the assignment does not run, feel free to contact me at:
> priyaarsd@gmail.com

 

Have a nice day :)

