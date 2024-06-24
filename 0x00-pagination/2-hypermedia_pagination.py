#!/usr/bin/env python3
'''
This module provides utility functions for pagination, including calculating
the range of indices for items on a specific page.
'''


from typing import Dict, Tuple
import csv
import math
from typing import List
import math


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
        '''
        task 1
        '''
        assert (type(page) == int and page > 0)
        assert (type(page_size) == int and page_size > 0)
        self.dataset()
        set_range = index_range(page, page_size)

        if set_range[0] > len(self.__dataset):
            return []
        return self.__dataset[set_range[0]:set_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        data = self.get_page(page, page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }


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
