"""
file: myscript.py
brief: Simple script to show how to define dosctrings
usage: python3 myscript.py
note:
author: Alexandre BIGOT, alexandre.bigot@iphc.cnrs.fr
"""

# import module
import pandas as pd


def sum(x: float | int, y: float | int) -> float:
    """
    Helper function to perform sum

    Args:
        x (float | int): 1st argument
        y (float | int): 2nd argument

    Returns:
        float: Sum of the 2 arguments
    """
    return x + y


def main(debug: bool = False) -> None:
    """
    Main function (like in C++)


    Args:
        debug (bool, optional): Debug flag. Defaults to False.
    """
    if debug:
        print("DEBUG mode activated!")
        # Add other debug specific code..

    print("Hello from script.py")

    a: int = 1  # FIXME: remove this variable
    pi: float = 3.14
    name: str = "Jim"
    names: list[str] = ["Michael", "Jim", "Dwight"]
    dfs: list[pd.DataFrame] = []

    res = sum(1, 2)
    print(res)


if __name__ == "__main__":
    DEBUG: bool = True
    main(DEBUG)
