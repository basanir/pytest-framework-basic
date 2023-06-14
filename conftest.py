import pytest
import logging
from utils.logging_util import Logger
from utils.api_helper import APIHelper
from utils.config_parser import ConfigParser
from utils.database_util import DBUtil


# Modify logger fixture to use logging_level
@pytest.fixture(scope="function", autouse=True)
def logger(request):
    log_name = request.node.nodeid.split("::")[0].replace("/", "_")
    marker = request.node.get_closest_marker("log_level")
    if marker is None:
        # Default log level
        level = logging.INFO
    else:
        level_str = marker.args[0]
        level = getattr(logging, level_str.upper(), logging.INFO)
    logger_obj = Logger(log_name, level=level)  # use logging_level here
    return logger_obj.get_logger()

# Add hook to log test outcome
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Only log when the actual test is run, not during setup/teardown
    if call.when == 'call':
        logger = item._request.getfixturevalue("logger")
        outcome = 'PASSED' if call.excinfo is None else 'FAILED'
        logger.info(f"Test outcome: {outcome}")

# create a fixture for APIHelper class
@pytest.fixture(scope="session")
def api_helper(config):
    """
    Create an APIHelper instance for the API under test.

    Args:


    Returns:
        An APIHelper instance.
    """
    base_url = config.get("base_url")
    api = APIHelper(base_url)
    return api

# create a fixture for ConfigParser class
@pytest.fixture(scope="session")
def config(request):
    """
    Create a ConfigParser instance for the config file.
    """
    env = request.config.getoption("--env")
    config_file = "config.ini"
    config = ConfigParser(config_file, env=env)
    return config

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")

@pytest.fixture()
def db_util(config, logger):
    """
    Create a DBUtil instance for the database under test.

    Args:
        config (ConfigParser): A ConfigParser instance.
        logger (Logger): A Logger instance.

    Returns:
        A DBUtil instance.
    """
    host = config.get("host")
    user = config.get("user")
    password = config.get("password")
    database = config.get("database")
    db = DBUtil(host, user, password, database, logger)
    yield db
    db.disconnect()




