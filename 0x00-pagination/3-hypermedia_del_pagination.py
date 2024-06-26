#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a subset of data from the dataset based on the given index
        and page size.

        Args:
            index (int): The starting index of the subset. Defaults to None.
            page_size (int): The number of items to include in the subset.
            Defaults to 10.

        Returns:
            dict: A dictionary containing the index, next_index, page_size,
            and data of the subset.
        """
        assert (type(index) is int and index > 0)
        data = self.dataset()[index: index + page_size]
        next_index = index + page_size
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }


# s = Server()

# l = s.indexed_dataset()
# for i in l:
#     print(i, l[i])
