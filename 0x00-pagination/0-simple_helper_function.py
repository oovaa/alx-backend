#!/usr/bin/env python3
'''
task 0
'''


def index_range(page, page_size):
    last = page * page_size
    first = last - page_size
    return (first, last)
