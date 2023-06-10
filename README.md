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
It prints log statements to console as well as file(testdir+test_file_name+timestamp.log)

