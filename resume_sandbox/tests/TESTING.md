#### NAMES: Nicole Lincoln, Josh White, David Havrilla
#### PROJECT: Resume Sandbox

# Automatic Test Instructions:
1. Locate the file 'test_db.py' in the ./tests directory.
2. Execute 'test_db.py' by running the following command in the same directory:

> \>\>\> python3 test_db.py

3. This test script will test four of the tables utilized in Resume Sandbox that
   are defined in 'schema.sql'. If all of the files have been correctly
   downloaded, then the following output should be produced in the terminal:

> Testing 'openings' table functionality. . .<br>
> Passed!<br>
> .<br>
> Testing 'resumes' table functionality. . .<br>
> Passed!<br>
> .<br>
> Testing 'skills' table functionality. . .<br>
> Passed!<br>
> .<br>
> Testing 'user' table functionality. . .<br>
> Passed!<br>
> .<br>
> ----------------------------------------------------------------------<br>
> Ran 4 tests in 0.030s<br>
><br>
> OK<br>

# User Acceptance Testing:
## 1. Register a new user name

#### Description:
    Test the user registration page

#### Pre-conditions:
    Username and password have not been previously registered.

#### Test steps:
    1. Navigate to registration page (Register button)
    2. Provide new username
    3. Provide password
    4. Click Register button

#### Expected result:
    User should be able to register

#### Actual result:
    User is navigated to login page with successful registration

#### Status (Pass/Fail):
    Pass

#### Notes:
    N/A

#### Post-conditions:
    - The username and password (encrypted) are registered in the database.
    - User is subsequently be able to login using credentials provided.


## 2. Verify Login

#### Description:
    Test the login page

#### Pre-conditions:
    User has valid user name and password

#### Test steps:
    1. Navigate to login page
    2. Provide valid username
    3. Provide valid password
    4. Click login button

#### Expected result:
    User should be able to login

#### Actual result:
    User is navigated to home page with successful login.

#### Status (Pass/Fail):
    Pass

#### Notes:
    N/A

#### Post-conditions:
    - User is validated with database and successfully signed into their account.
    - The account session details are logged in database.


## 3.  New Skills Entry

#### Description:
    Test the Add New Skills page

#### Pre-conditions:
    User is logged into their account and at home page

#### Test steps:
    1. Click on "New Skills"
    2. Add new skill into text box.   
    3. Click Add button

#### Expected result:
    User should have a new skill registered to their account

#### Actual result:
    User is navigated to home page, where newly entered skill shows under "Here are your 5 most recently added skills"

#### Status (Pass/Fail):
    Pass

#### Notes:
    N/A

#### Post-conditions:
    - User sees new skills on their home page
    - The account session details are logged in database in "Skills" table.


## 4.  New Current Openings Entry

#### Description:
    Test the New Opening page

#### Pre-conditions:
    User is logged into their account and at home page

#### Test steps:
    1. Click on "New Opening"
    2. Add Position, Company, Posting URL, and Application Deadline   
    3. Click Create button

#### Expected result:
    User should have a new Current Opening showing up on their homepage

#### Actual result:
    User is navigated to home page, where Current Openings has a new opening.

#### Status (Pass/Fail):
    Pass

#### Notes:
    N/A

#### Post-conditions:
    - User sees new opening on their home page. Only information that was entered is shown.
    - The account session details are logged in database in "Openings" table.
