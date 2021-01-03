# -*- coding: utf-8 -*-
"""Device class representing a remote-controllable receiver"""
from pyBrematic.utils import Storage
from pyBrematic.action import Action


class AutoPairDevice(object):
    ACTION_OFF = Action.OFF
    ACTION_ON = Action.ON
    ACTION_UP = Action.UP
    ACTION_DOWN = Action.DOWN
    ACTION_PAIR = Action.PAIR
    ACTION_UNPAIR = Action.UNPAIR
    ACTION_UNPAIR_ALL = Action.UNPAIR_ALL

    def __init__(self, device_id, seed=None):
        """
        :param device_id: A unique device identifier
        :param seed: (Optional) The seed used to generate payload data
        """
        self.device_id = device_id
        storage = Storage()
        self.seed = seed or storage.get_seed(device_id)

    def get_signal(self, action):
        """Returns a signal which triggers a device to execute the intended action"""
        raise NotImplementedError("Subclasses must implement this method!")

    @staticmethod
    def join_list(lst, delimeter=","):
        """Join a list together with a certain delimeter

        :param lst: The list to join
        :param delimeter: The delimeter to use to join the list elements
        :return:
        """
        return delimeter.join(lst)
