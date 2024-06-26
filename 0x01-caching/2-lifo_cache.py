
from base_caching import BaseCaching


class LIFOCache(BaseCaching):

    def __init__(self):
        super().__init__()
        self.id = 0
        self.track = {}

    def put(self, key, item):
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
