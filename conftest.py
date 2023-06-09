import pytest
from utils.logging_util import Logger

@pytest.fixture(scope="session", autouse=True)
def logger(request):
    log_name = request.node.nodeid.split("::")[0].replace("/", "_")
    logger = Logger(log_name).get_logger()
    return logger

@pytest.fixture(scope="function", autouse=True)
def log_test_start_finish(request, logger):
    test_name = request.node.nodeid
    logger.info(f'\nStarting test: {test_name}')
    yield  # This is where the test runs.
    logger.info(f'\nFinishing test: {test_name}')

