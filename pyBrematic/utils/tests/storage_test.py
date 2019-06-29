# -*- coding: utf-8 -*-
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

        devs = list()
        devs.append(Device(0, 879123789812))
        devs.append(Device(1, 903482973490))
        devs.append(Device(2, 834348900123))
        devs.append(Device(3, 499832476341))

        self.storage.devices = devs

        # self.storage.add_device(device_id, seed)
        self.storage._store(path)

        with open(path, "r", encoding="utf-8") as f:
            content2 = f.read()

        self.assertNotEqual(content, content2)
        self.assertEqual('{"data" : { \
                            "devices" : [ \
                                {"device_id":0,"seed":879123789812}, \
                                {"device_id":1,"seed":903482973490}, \
                                {"device_id":2,"seed":834348900123}, \
                                {"device_id":3,"seed":499832476341} \
                            ] \
                        }}'.replace(" ", ""), content2.replace(" ", ""))

    def test_add_device(self):
        device_id = 1337
        seed = 420

        self.storage.add_device(device_id, seed)

        self.assertEqual(1, len(self.storage.devices))

        dev = self.storage.devices[0]
        self.assertEqual(dev.device_id, device_id)
        self.assertEqual(dev.seed, seed)

    def test_get_seed(self):
        device_id = 1337

        seed = self.storage.get_seed(device_id)
        second_seed = self.storage.get_seed(device_id)

        self.assertEqual(type(seed), int)
        self.assertEqual(seed, second_seed)

    def test_singleton(self):
        storage2 = Storage()

        self.assertEqual(self.storage, storage2)
