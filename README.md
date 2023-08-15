# jsend-python
This is a package to response jsend-like format


## requirements
```bash
pip install django djangorestframework
```


## Installation

<!-- ```bash
pip install jsend
``` -->

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



## output

```json
{
    "status": "faild",
    "message": "Any message",
    "data": {
        ...
    },
    "code": "-100",
    "total": 100,
    "offset": 12

}
```
`status: str`
+ required
+ API status as a string, standard values are `success`, `fail` and `error`.


`message: str`
+ optional
+ Default is None and **not** included in response. 

`data: Any`
+ required
+ The original result of API response. 

`code: int`
+ optional
+ Default is None and **not** included in response. 


`total: int`
+ optional
+ Total objects retrieved if the result is paginated.

`count: int`
+ optional
+ Object's count in the data if the result is paginated. 


`offset: int`
+ optional
+ Object's offset if the result is paginated. 

``


