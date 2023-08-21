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




## FastAPI example
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

### single Object
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


### Paginated 
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





