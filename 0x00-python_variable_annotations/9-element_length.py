#!/usr/bin/env python3
"""Let's duck type an iterable object"""

from typing import Iterator, Sequence, List, Tuple


def element_length(lst: Iterator[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return the length of the List"""
    return [(i, len(i)) for i in lst]
