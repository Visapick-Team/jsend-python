from enum import Enum


class Status(str, Enum):
    success = "success"
    fail = "fail"
    error = "error"
