#!/usr/bin/env python3
'''
This module provides utility functions for pagination, including calculating the range of indices for items on a specific page.
'''


from typing import Tuple
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert (page > 0)
        assert (page_size > 0)


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
