# pytest-framework-basic
It contains basic pytest framework to quickly start automation 

## Create a virtual env 
virtualenv -p /path/to/python/ ~/.pytest_env

## Install pip requirements
pip insatll -r requirements.txt


## Features

### conftest.py
#### logger
Is called at function scope with autouse set to Ture.
Default log level is set to INFO, it can be chnaged at a test script function level by setting a marker log_level
``` @pytest.mark.log_level("DEBUG") ```

### utils
#### logging_util.py
This module enables to create a logger object in conftest.py
It prints log statements to console as well as file
``` [2023-06-10 14:25:38] [api_tests_test_feature.py::test_example_first  ] [INFO    ] This is an info log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example_first  ] [INFO    ] This is another info log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example_first  ] [DEBUG   ] This is a debug log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example        ] [INFO    ] This is an info log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example        ] [INFO    ] This is another info log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example        ] [ERROR   ] This is an error log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example        ] [WARNING ] This is a warning log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example        ] [CRITICAL] This is a critical log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example2       ] [DEBUG   ] This is a debug log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example2       ] [INFO    ] This is an info log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example3       ] [INFO    ] This is an info log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example3       ] [INFO    ] This is another info log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example3       ] [ERROR   ] This is an error log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example3       ] [WARNING ] This is a warning log message
[2023-06-10 14:25:38] [api_tests_test_feature.py::test_example3       ] [CRITICAL] This is a critical log message ```

