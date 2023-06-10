import pytest

@pytest.mark.log_level("DEBUG")
def test_example_first(logger):
    logger.info('This is an info log message')
    # Rest of your test here...
    logger.info('This is another info log message')
    logger.debug('This is a debug log message')

def test_example(logger):
    logger.info('This is an info log message')
    # Rest of your test here...
    logger.info('This is another info log message')

    logger.error('This is an error log message')

    logger.warning('This is a warning log message')

    logger.critical('This is a critical log message')

    logger.debug('This is a debug log message')

@pytest.mark.log_level("DEBUG")
def test_example2(logger):
    logger.debug('This is a debug log message')
    logger.info('This is an info log message')

def test_example3(logger):
    logger.info('This is an info log message')
    # Rest of your test here...
    logger.info('This is another info log message')
    logger.error('This is an error log message')
    logger.warning('This is a warning log message')
    logger.critical('This is a critical log message')
    logger.debug('This is a debug log message')


