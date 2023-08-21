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


# Response


### Django

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
    "DEFAULT_PAGINATION_CLASS": "jsend.django.utils.JSendLimitOffsetPagination",
    
    # jsend response
    "DEFAULT_RENDERER_CLASSES": [
        "jsend.django.utils.JSendRenderer",
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


### FastAPI
main.py
```python
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from router import router

app = FastAPI()

app.include_router(router)

add_pagination(app)

```

router.py
```python
from fastapi import APIRouter
from fastapi import Query
from pagination import Pagination
from response import Response

router = APIRouter()
```

#### single Object
```python
@router.get(
    "/user",
    response_model=Response[UserOut],
    response_model_exclude_none=True
    )
async def get_user(user_id: int = Query(ge=0)):
    user: UserOut = find_user(user_id)
    return Response(
        data=user,
        status="success"  # default 'success'
    )
```


#### Paginated 
```python
@router.get(
    "/users",
    response_model=Pagination[UserOut],
    response_model_exclude_none=True
    )
async def get_users():
    response = paginate(users)
    response.status = "success"  # default 'success'
    return response
```





# Exception Handling


### Django

settings.py
```python
REST_FRAMEWORK = {
    # jsend exception handler
    "EXCEPTION_HANDLER": "jsend.django.exception.jsend_exception_handler",
    
}

```




### FastAPI
main.py
```python
from fastapi import FastAPI, HTTPException
from api import router
from jsend.fastapi.exception import ExceptionMiddleware

app = FastAPI()

app.include_router(router)

ExceptionMiddleware(app)
```