# Report

The PDF report can be found [here](./report.pdf).


# Development

In order to run the app launch the following commands:
- pip3 install –r requirements.txt
- python3 setup.py develop
- FLASK_APP=myservice flask run

# Test

## Python
To run python test case, run `pytest` in the root folder.

## Postman
The Postman test collection can be found [here](./Homework1-Test.postman_collection.json) while the test run result is [here](./Homework1-Test.postman_test_run.json).

## Flask profiler

To run profiler run:
 - `python3 ./myservice/app.py`

and navigate to [http://127.0.0.1:5000/flask-profiler](http://127.0.0.1:5000/flask-profiler)


## Boom

 To simulate concurrent request to the service run
 - `boom http://127.0.0.1:5000/doodles -c 10 -d 10`