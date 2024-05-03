#!/usr/bin/env python3
"""More involved type annotations"""

from typing import Mapping, Union, TypeVar, Any

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """If kwy is present, return key value"""
    if key in dct:
        return dct[key]
    else:
        return default
