#!/usr/bin/env python3

'''
This module defines the BasicCache class which inherits
 from BaseCaching.
The BasicCache class implements a basic caching system
that stores key-value pairs.
'''


from base_caching import BaseCaching


class LIFOCache(BaseCaching):

    """
    LIFOCache class represents a Last-In-First-Out (LIFO) cache.

    Attributes:
        id (int): The ID of the cache.
        track (dict): A dictionary to track the cache items.
    """

    def __init__(self):
        """
        Initializes a new instance of the LIFOCache class.

        The __init__ method is called when a new LIFOCache object is
        created.
        It initializes the cache ID and the track dictionary.
        """
        super().__init__()
        self.id = 0
        self.track = {}

    def put(self, key, item):
        """
        Adds a key-value pair to the cache.

        Args:
            key: The key to be added.
            item: The value associated with the key.

        Returns:
            None
        """
        if key is not None and item is not None:
            if len(self.cache_data
                   ) == self.MAX_ITEMS and key not in self.cache_data:
                to_pop_key = self.track[max(self.track.keys())]
                poped = self.cache_data.pop(to_pop_key)
                print('DISCARD:', to_pop_key)
                self.track.pop(max(self.track.keys()))

            self.track[self.id] = key
            self.id += 1
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
