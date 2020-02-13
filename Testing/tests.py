import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """Eat should have a positive message for healthy eating habits"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because my body is a temple."
        )

    def test_eat_junk(self):
        """Eat should have a negative message for crappy eating habits"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO."
        )

    def test_eat_healthy_boolean(self):
        """is_healthy must be a bool"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares")


    def test_short_nap(self):
        """Nap should indicate you are refreshed"""
        self.assertEqual(
            nap(1), 
            "I'm feeling refreshed after my 1 hour nap."
        )

    def test_long_nap(self):
        """Nap should indicate you are distressed"""
        self.assertEqual(
            nap(3), 
            "Ugh, I overslept. I didn't mean to nap for 3 hours!"
        )

    def test_is_funny_tim(self): 
        """Tim Should not be funny!"""
        self.assertEqual(is_funny("Tim"), False)
            # self.assertFalse(is_funny("Tim"), "Tim should not be funny!")

    def test_is_funny_anyone_else(self):
        """Anyone but Tim should be funny!"""
        self.assertTrue(is_funny("Blue"), "Blue should be funny!")
        self.assertTrue(is_funny("Reina"), "Reina should be funny!")
        self.assertTrue(is_funny("Mirriam"), "Mirriam should be funny!")

    def test_laugh(self):
        """Should return one of three laughs."""
        self.assertIn(laugh(), ('lol', 'haha', 'jajaja'))
        

if __name__ == "__main__":
    unittest.main()

