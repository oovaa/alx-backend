#!/usr/bin/env python3
'''
This module provides utility functions for pagination, including calculating the range of indices for items on a specific page.
'''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Returns a tuple representing the start and end indices of a given page.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indices of the page.

    Example:
        >>> index_range(1, 10)
        (0, 10)
        >>> index_range(2, 10)
        (10, 20)
    '''
    last = page * page_size
    first = last - page_size
    return (first, last)
