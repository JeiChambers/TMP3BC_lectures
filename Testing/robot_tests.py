import unittest
from robot import Robot

class RobotTests(unittest.TestCase):
    def setUp(self):
        self.ultron = Robot("Ultron", battery=50)

    def test_charge(self):
        self.ultron = Robot("Ultron", battery=50)
        self.ultron.charge()
        self.assertEqual(self.ultron.battery, 100)

    def test_say_name(self):
        self.assertEqual(
            self.ultron.say_name(),
            "I herald the destruction of the Avengers! I'm ULTRON"
            )
        self.assertEqual(self.ultron.battery, 49)


if __name__ == "__main__":
    unittest.main()