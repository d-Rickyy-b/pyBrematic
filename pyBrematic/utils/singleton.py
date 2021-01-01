# -*- coding: utf-8 -*-
from functools import wraps

__instances = {}


def singleton(cls):
    @wraps(cls)
    def get_instance(*args, **kwargs):
        instance = __instances.get(cls, None)
        if not instance:
            instance = cls(*args, **kwargs)
            __instances[cls] = instance
        return instance

    return get_instance


def _delete_all_instances():
    global __instances
    __instances = {}
