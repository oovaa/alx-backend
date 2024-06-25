#!/usr/bin/env python3
'''
task 0
'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class represents a basic caching mechanism.

    Attributes:
        cache_data (dict): A dictionary to store key-value pairs for caching.

    Methods:
        __init__(): Initializes an instance of the BasicCache class.
        put(key, item): Adds a key-value pair to the cache_data dictionary.
        get(key): Retrieves the value associated with the given key from the
        cache_data dictionary.

    """

    def __init__(self):
        """
        Initializes an instance of the BasicCache class.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds a key-value pair to the cache_data dictionary.

        Args:
            key: The key to be added.
            item: The value associated with the key.

        Returns:
            None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache_data
        dictionary.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        if key is not None:
            return self.cache_data.get(key, None)
