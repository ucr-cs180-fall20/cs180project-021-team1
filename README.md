# cs180project-021-team1
cs180project-021-team1 created by GitHub Classroom

# Testing Extra Credit
On every push to the project or by doing so manually, continuous integrations tests can be ran through Github Actions.
In the Root directory you will find a list of required packages under `requirements.txt`.

We are using the package `unittest` (built-in) then paired with the Django testing framework, we run the
`manage.py test` command to run our tests.

This command runs the unit tests under `/mysite/fifa/tests.py` which are then ran by Github Actions upon firing.
In the `test.py` file we test the output for:
- top and lowest rated players
  - ensure we receive a list of length 100
- top 10 best hits among players
  - ensure we receive a list of length 10
- top 10 team average ratings
  - ensure we receive a list of length 10
  
We also test for frontend html pages loading:
- homepage.html
  - ensure we receive status code 200
  - ensure template is used 
- add.html
  - ensure we receive status code 200
  - ensure template is used 
- search.html
  - ensure we receive status code 200
  - ensure template is used 
- comAge.html
  - ensure we receive status code 200
  - ensure template is used 
