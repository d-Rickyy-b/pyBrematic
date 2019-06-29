# -*- coding: utf-8 -*-
import json
import logging
import os
import random

from pyBrematic.utils import singleton, DataEncoder


@singleton
class Storage(object):

    def __init__(self, path=None):
        if path is None:
            self.path = self._get_current_path()
        else:
            self.path = os.path.dirname(path)
        self.devices = []
        self._load(self.path)

    @property
    def data(self):
        return dict(data=dict(devices=self.devices))

    def _load(self, path):
        """Loads the stored data from the disk"""
        logging.debug("Loading storage")
        if not os.path.exists(path):
            with open(self.path, "w", encoding="utf-8") as f:
                self.devices = []
                f.write(json.dumps(self.data))
            return

        with open(self.path, "r", encoding="utf-8") as f:
            content = f.read()
            jcontent = json.loads(content)
            devices = jcontent.get("data").get("devices")

            devs = []

            for device in devices:
                devs.append(Device(device.get("device_id"), device.get("seed")))

            self.devices = devs

    def _store(self, path):
        """Store the current data on the drive"""
        logging.debug("Storing data")

        with open(path, "w", encoding="utf-8") as f:
            f.write(self._to_json())

    def add_device(self, device_id, seed=None):
        for device in self.devices:
            if device.device_id == device_id:
                logging.warning("Device with the id '{}' is already stored!".format(device_id))
                return

        self.devices.append(Device(device_id, seed))
        self._store(self.path)

    def get_seed(self, device_id, loop_prevent=0):
        for device in self.devices:
            if device.device_id == device_id:
                return device.seed

        # Add the device if it's not present already
        self.add_device(device_id)
        if loop_prevent > 2:
            raise Exception("Something went wrong while storing new device!")
        return self.get_seed(device_id, loop_prevent+1)

    @staticmethod
    def _get_current_path():
        """Return the current path with the filename 'storage.json' appended to it"""
        current_path = os.path.dirname(os.path.abspath(__file__))
        storage_file = os.path.join(current_path, "storage.json")

        return storage_file

    def _delete_all(self):
        with open(self.path, "w", encoding="utf-8") as f:
            self.devices = []
            f.write(json.dumps(self.data))

    def _to_json(self):
        """Return the current data as json object"""
        return json.dumps(self.data, cls=DataEncoder)

    def _to_dict(self):
        """Return the current data as dict"""
        return self.data


class Device(object):

    def __init__(self, device_id, seed=None):
        """
        Device class which holds data of a certain 433 MHz device
        :param device_id: A unique identifier of the device
        :param seed: (Optional) The seed used to generate payload data
        """
        self.device_id = device_id
        self.seed = seed or self._generate_seed()

    @staticmethod
    def _generate_seed():
        return random.randint(0, 2 ** 63 - 1)

    def to_json(self):
        return json.dumps(self.to_dict(), cls=DataEncoder, sort_keys=True)

    def to_dict(self):
        return dict(device_id=self.device_id, seed=self.seed)
