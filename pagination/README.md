# Pagination

This project covers pagination techniques for datasets.

## Learning Objectives

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- Code uses the pycodestyle style (version 2.5.*)
- All modules have documentation
- All functions have documentation
- All functions and coroutines are type-annotated

## Tasks

### 0. Simple helper function
Function `index_range` that returns a tuple of start and end indexes for pagination.

### 1. Simple pagination
Server class with `get_page` method for basic pagination.

### 2. Hypermedia pagination
Server class with `get_hyper` method that returns pagination metadata.

### 3. Deletion-resilient hypermedia pagination
Server class with `get_hyper_index` method for deletion-resilient pagination.
