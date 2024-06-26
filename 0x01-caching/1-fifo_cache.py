#!/usr/bin/env python3

'''
This module defines the BasicCache class which inherits
 from BaseCaching.
The BasicCache class implements a basic caching system
that stores key-value pairs.
'''

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class represents a First-In-First-Out (FIFO) caching mechanism.

    It inherits from the BaseCaching class and implements the put and get
    methods.
    """

    def __init__(self):
        """
        Initializes an instance of the FIFOCache class.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache.

        If the cache is full, it removes the oldest item (the first item that
        was added).

        Args:
            key: The key of the item to be added.
            item: The item to be added to the cache.
        """
        if key is not None and item is not None:
            if len(self.cache_data
                   ) >= self.MAX_ITEMS and key not in self.cache_data:
                first_key = next(iter(self.cache_data))
                print('DISCARD:', first_key)
                self.cache_data.pop(first_key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The item associated with the given key, or None if the key is not
            found in the cache.
        """
        return self.cache_data.get(key, None)
