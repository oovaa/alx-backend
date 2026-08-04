# 0x00-pagination — API Pagination Strategies

[![ALX](https://img.shields.io/badge/ALX-Backend%20Engineering-blue?style=flat-square&logo=linux&logoColor=white)](https://www.alxafrica.com/)

> **Pagination Implementation** — Simple, hypermedia, and deletion-resilient pagination for REST APIs.

---

## 🎯 Overview

This project implements multiple pagination strategies for a REST API using a dataset of popular baby names. Covers simple pagination, hypermedia pagination (HATEOAS), and deletion-resilient pagination.

---

## 📁 Files

| File | Description |
|------|-------------|
| `0-simple_helper_function.py` | Helper function `index_range(page, page_size)` returning start/end indices |
| `1-simple_pagination.py` | `Server` class with `get_page(page, page_size)` — basic pagination |
| `2-hypermedia_pagination.py` | `get_hyper(page, page_size)` — returns dict with `page_size`, `page`, `data`, `next_page`, `prev_page`, `total_pages` |
| `3-hypermedia_del_pagination.py` | `get_hyper_index(index, page_size)` — deletion-resilient pagination using indexed dataset |
| `Popular_Baby_Names.csv` | Dataset (786K rows) — baby names from 1880-2020 |

---

## 🚀 Usage

```python
# Simple pagination
from 1-simple_pagination import Server
server = Server()
page = server.get_page(page=1, page_size=10)

# Hypermedia pagination
from 2-hypermedia_pagination import Server
server = Server()
result = server.get_hyper(page=1, page_size=10)
# result: {'page_size': 10, 'page': 1, 'data': [...], 'next_page': 2, 'prev_page': None, 'total_pages': 19419}

# Deletion-resilient pagination
from 3-hypermedia_del_pagination import Server
server = Server()
result = server.get_hyper_index(index=0, page_size=10)
# Works correctly even if items are deleted from dataset
```

---

## 🧪 Running Tests

```bash
python3 0-main.py   # Test index_range
python3 1-main.py   # Test simple pagination
python3 2-main.py   # Test hypermedia pagination
python3 3-main.py   # Test deletion-resilient pagination
```

---

## 📚 Learning Outcomes

- ✅ Calculate pagination indices correctly
- ✅ Implement basic pagination with boundary handling
- ✅ Build HATEOAS-compliant hypermedia responses
- ✅ Handle dataset mutations without breaking pagination

---

## 📄 License

MIT License - see root [LICENSE](../LICENSE)