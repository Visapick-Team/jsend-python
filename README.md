# jsend-python
This is a package to response jsend-like format




## Installation

```bash
pip install jsend
```

```bash
pip install git+https://github.com/Visapick-Team/jsend-python.git
```


## Django example

settings.py
```python
INSTALLED_APPS = [
    ...
    "jsend",
]
```

```python
REST_FRAMEWORK = {
    # jsend limit/offset pagination 
    "DEFAULT_PAGINATION_CLASS": "jsend.utils.JSendLimitOffsetPagination",
    
    # jsend response
    "DEFAULT_RENDERER_CLASSES": [
        "jsend.utils.JSendRenderer",
    ],
}

```




