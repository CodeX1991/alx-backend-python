#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""


from typing import Union, List, Tuple


def to_kv(k: str, v: List[Union[int, float]]) -> Tuple[str, float]:
    """Return a tuple"""
    return (k, float(v * v))
