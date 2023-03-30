#!/usr/bin/env python3
"""sum Mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    type-annotated function sum_mixed_list which takes a list
    mxd_lst of integers and floats and returns their sum as a float.

    mxd_lst : int,float
    return : float
    """
    return sum(mxd_lst)
