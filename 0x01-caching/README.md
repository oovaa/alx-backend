# 0x01-caching — Caching Strategies

[![ALX](https://img.shields.io/badge/ALX-Backend%20Engineering-blue?style=flat-square&logo=linux&logoColor=white)](https://www.alxafrica.com/)

> **Cache Implementation** — FIFO, LIFO, LRU, MRU, and LFU caching algorithms with a common base class.

---

## 🎯 Overview

Implements multiple cache eviction policies inheriting from a shared `BaseCaching` class. Each cache has a maximum size (`MAX_ITEMS = 4`) and implements `put(key, item)` and `get(key)` methods.

---

## 📁 Files

| File | Description |
|------|-------------|
| `base_caching.py` | Abstract base class with `MAX_ITEMS`, `cache_data`, `put()`, `get()` |
| `0-basic_cache.py` | Basic cache (no eviction — for testing base class) |
| `1-fifo_cache.py` | **FIFO** (First-In-First-Out) eviction |
| `2-lifo_cache.py` | **LIFO** (Last-In-First-Out) eviction |
| `3-lru_cache.py` | **LRU** (Least Recently Used) eviction |
| `4-mru_cache.py` | **MRU** (Most Recently Used) eviction |
| `100-lfu_cache.py` | **LFU** (Least Frequently Used) eviction |

---

## 🚀 Usage

```python
from 3-lru_cache import LRUCache

cache = LRUCache()
cache.put("key1", "value1")
cache.put("key2", "value2")
print(cache.get("key1"))  # "value1"

# When MAX_ITEMS exceeded, LRU key is discarded
cache.put("key3", "value3")
cache.put("key4", "value4")
cache.put("key5", "value5")  # Discards "key1" (least recently used)
```

---

## 🧪 Running Tests

```bash
python3 0-main.py   # Test basic cache
python3 1-main.py   # Test FIFO
python3 2-main.py   # Test LIFO
python3 3-main.py   # Test LRU
python3 4-main.py   # Test MRU
python3 100-main.py # Test LFU
```

---

## 📚 Learning Outcomes

- ✅ Implement cache eviction policies (FIFO, LIFO, LRU, MRU, LFU)
- ✅ Use inheritance for shared cache infrastructure
- ✅ Handle edge cases: None keys, missing keys, updates
- ✅ Track access order and frequency for LRU/MRU/LFU

---

## 📄 License

MIT License - see root [LICENSE](../LICENSE)