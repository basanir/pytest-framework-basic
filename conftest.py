import pytest
import logging
from utils.logging_util import Logger


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





