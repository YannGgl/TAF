"""
file: test_snippet.py
brief: Simple test of snippet features : created the 'test_snippet.py' file,
        started typing 'py_tmplf_taf' and autocompleted w/ tab.
        Created the whole structure down here :)
usage: python3 test_snippet.py
note:
author: Name, email address
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


if __name__ == "__main__":
    DEBUG: bool = True
    main(DEBUG)
