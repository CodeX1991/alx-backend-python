#!/usr/bin/env python3
"""Complex types - mixedlist"""


from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Return their sum as a float"""
    return float(sum(mxd_list))
