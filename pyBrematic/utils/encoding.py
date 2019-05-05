# -*- coding: utf-8 -*-
from json import JSONEncoder


class DataEncoder(JSONEncoder):
    def default(self, o):
        return o.to_dict()
