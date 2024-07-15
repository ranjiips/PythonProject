# PythonProject
Pytest:
for pytest execution, from command line/Terminal use the below command
py.test -v -s - to run all the test methods in the project (-s to print statements; -v for verbose)
py.test file_name.py - to run the specific test case file
py.test file_path - to run the all the test case in the given path
py.test file_name.py::method_name - to run the specific method from the given file
for Ordering, install the below
"pip install pytest-ordering"

py.test

To capture the reports, run the below command:
py.test -v -s --html=reports\htmlreport.html


use the below command line arguments to run the test
py.test -v -s --html=reports\htmlreport.html --browser chrome
