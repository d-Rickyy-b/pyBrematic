# -*- coding: utf-8 -*-

from random import seed, randint


class Rand(object):

    def __init__(self, generator_seed):
        seed(generator_seed)

    def next_bool(self):
        return randint(0, 1) == 1
