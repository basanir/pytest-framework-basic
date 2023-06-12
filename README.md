# pytest-framework-basic
It contains basic pytest framework to quickly start automation 

#### Create a virtual env 
virtualenv -p /path/to/python/ ~/.pytest_env

#### Install pip requirements
pip insatll -r requirements.txt


## Current Features

#### Custom Logger
The custom logger module, logging_util, utilizes Python's inherent logging library. It creates distinct log files for each test module while logging the initiation and conclusion of each test. The logger also allows for adjusting the log level through the use of pytest markers.

#### Configuration of Tests
The conftest.py is leveraged to provide the custom logger to all tests. Additionally, there's an implemented mechanism to control the log level from the command line, utilizing pytest's addoption functionality.

#### API Helper Module
The API Helper class simplifies the process of making requests to a REST API. It uses the requests library and offers methods for GET, POST, PUT, PATCH, and DELETE HTTP methods. This class also provides the ability to set the authorization token and manage headers.

#### Configuration Manager
The configuration manager reads an .ini configuration file to ascertain the base URL for the API under test. Command line options for pytest are available to determine the environment in which the tests should be executed.

#### Enhanced API Test Reporting
The framework facilitates advanced reporting for API tests, including logging the response when a test fails. This is achieved through a customized pytest hook within the conftest.py file.

#### Test Script
The test_feature.py test script provides a practical example of how these tools can be used to write effective API tests. This script includes both positive and negative tests, and demonstrates how to use the custom logger.

#### Test Execution
Several pytest command line options are available to control test execution, including -k for executing specific tests and --log-level to control the logging level.

#### Getting Started

To execute the tests, the following command can be used:
```
pytest --env=dev --log-level=TEST

 ```

