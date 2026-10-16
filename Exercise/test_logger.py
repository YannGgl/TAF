"""
file: test_logger.py
brief:
usage: python3 test_logger.py
note:
author: Alexandre BIGOT, alexandre.bigot@iphc.cnrs.fr
"""

from TAF_logger import Logger as LOG


def main(debug: bool) -> None:
    """
    Main function
    Args:
    debug (bool): Switch for debugging
    """
    if debug:
        LOG("Debug mode activated!", "DEBUG")

    LOG("Result", "RESULT")
    LOG("Info..", "INFO")
    LOG("Warning!", "WARNING")
    LOG("Error!!", "ERROR")
    LOG("Fatal error!!!", "FATAL")


if __name__ == "__main__":
    DEBUG: bool = True
    main(DEBUG)
