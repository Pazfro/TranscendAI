import logging

from transcendai.logger_config import logger


def test_logger_level():
    """Ensure the logger's level is set correctly, e.g., INFO."""
    assert logger.level == logging.INFO


def test_logger_handler_count():
    """Check that the two handlers are configured."""
    assert len(logger.handlers) == 2


def test_logger_formatter():
    """Ensure the logger's formatter includes the function name for
    debugging."""
    formatter = logger.handlers[0].formatter
    assert formatter is not None
    assert "%(funcName)s" in formatter._fmt


def test_logger_output(caplog):
    """Use pytest's caplog to capture log output and verify log messages."""
    with caplog.at_level(logging.INFO):
        logger.info("Test log message")
    assert "Test log message" in caplog.text
