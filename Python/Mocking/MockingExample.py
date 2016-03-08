import unittest
from unittest.mock import Mock


class Huston(object):
    def __init__(self, rocket):
        self.rocket = rocket

    def launch(self, payload):
        payload.append("explosives")
        self.rocket.shoot_to_the_moon(payload)


class TestHuston(unittest.TestCase):
    def test_launch(self):
        rocket = Mock()
        payload = ["candy"]
        under_test = Huston(rocket)

        under_test.launch(payload)

        assert rocket.shoot_to_the_moon.called
        rocket.shoot_to_the_moon.assert_called_once_with(["candy", "explosives"])
        assert rocket.shoot_to_the_moon.called_twice_with(["candy", "explosives"])
