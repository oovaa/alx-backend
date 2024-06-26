#!/usr/bin/env python3

from psutil import swap_memory
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.track = list()

    def handle_none_full_cache(self, key, item):
        self.track.append(key)
        self.cache_data[key] = item

    def handle_full_cache(self, key, item):
        to_remove = self.track.pop(0)
        if to_remove in self.cache_data:
            self.cache_data.pop(to_remove)
            print('DISCARD:', to_remove)
        else:
            print(f"Attempted to remove non-existent key: {to_remove}")
        self.track.append(key)
        self.cache_data[key] = item

    def swap(self, key):
        self.track.remove(key)
        self.track.append(key)

    def put(self, key, item):
        if item is None or key is None:
            return
        if key in self.cache_data:
            self.swap(key)
            self.cache_data[key] = item
        elif len(self.cache_data) < self.MAX_ITEMS:
            self.handle_none_full_cache(key, item)
        else:
            self.handle_full_cache(key, item)

    def get(self, key):
        if key in self.cache_data and key is not None:
            if key in self.track:
                self.swap(key)
            return self.cache_data[key]
        return None
