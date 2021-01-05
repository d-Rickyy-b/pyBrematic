# -*- coding: utf-8 -*-
import json
import logging
import unittest

from pyBrematic.utils import Storage
from pyBrematic.utils.singleton import _delete_all_instances
from pyBrematic.utils.storage import Device


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.storage = Storage()

    def tearDown(self):
        self.storage._delete_all()
        _delete_all_instances()

    def test_init(self):
        self.assertEqual([], self.storage.devices)

    def test_load(self):
        path = self.storage._get_current_path()
        with open(path, "w", encoding="utf-8") as f:
            f.write('{"data": {"devices": [ \
            {"device_id":0,"seed":2312378238912}, \
            {"device_id":1,"seed":5151515151822}, \
            {"device_id":2,"seed":7673490234723}, \
            {"device_id":3,"seed":5388254612384}  \
            ]}}')

        self.storage._load(path)

        self.assertEqual(4, len(self.storage.devices))

        for d in self.storage.devices:
            if d.device_id == 0:
                self.assertEqual(2312378238912, d.seed)
            elif d.device_id == 1:
                self.assertEqual(5151515151822, d.seed)
            elif d.device_id == 2:
                self.assertEqual(7673490234723, d.seed)
            elif d.device_id == 3:
                self.assertEqual(5388254612384, d.seed)

    def test_store(self):
        self.maxDiff = None
        path = self.storage._get_current_path()
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        devs = [Device(0, 879123789812), Device(1, 903482973490), Device(2, 834348900123), Device(3, 499832476341)]
        self.storage.devices = devs
        self.storage._store(path)

        with open(path, "r", encoding="utf-8") as f:
            content2 = f.read()
            content2 = json.loads(content2)

        self.assertNotEqual(content, content2, "The storage file did not change!")

        test = [dict(device_id=0, seed=879123789812),
                dict(device_id=1, seed=903482973490),
                dict(device_id=2, seed=834348900123),
                dict(device_id=3, seed=499832476341)]

        testd = dict(data=dict(devices=test))
        self.assertEqual(sorted(testd.items()), sorted(content2.items()))

        test_devices = testd.get("data").get("devices")
        stored_devices = content2.get("data").get("devices")

        self.assertEqual(4, len(test_devices))
        self.assertEqual(4, len(stored_devices))

        # Workaround for behaviour in python 3.4 where dicts are not sorted.
        # We need to loop through all elements in each lists and compare the right ones.
        # If found we assert they are equal. If not, we fail the test.
        for devt in test_devices:
            counter = 0
            for devs in stored_devices:
                if devt.get("device_id") == devs.get("device_id"):
                    self.assertEqual(devt.get("seed"), devs.get("seed"))
                    break

                counter += 1
                if counter >= len(test_devices):
                    self.fail("Couldn't find fitting device_id!")

    def test_add_device(self):
        device_id = 1337
        seed = 420

        self.storage.add_device(device_id, seed)

        self.assertEqual(1, len(self.storage.devices))

        dev = self.storage.devices[0]
        self.assertEqual(dev.device_id, device_id)
        self.assertEqual(dev.seed, seed)

    def test_duplicate_storage(self):
        # Set log-level to "ERROR" to prevent text output during test execution
        logging.getLogger().setLevel(logging.ERROR)
        self.storage.add_device(1337)
        self.assertEqual(1, len(self.storage.devices))

        self.storage.add_device(1337)
        self.assertEqual(1, len(self.storage.devices))

        self.storage.add_device(42)
        self.assertEqual(2, len(self.storage.devices))

    def test_get_seed(self):
        device_id = 1337

        seed = self.storage.get_seed(device_id)
        second_seed = self.storage.get_seed(device_id)

        self.assertEqual(type(seed), int)
        self.assertEqual(seed, second_seed)

    def test_singleton(self):
        storage2 = Storage()

        self.assertEqual(self.storage, storage2)
