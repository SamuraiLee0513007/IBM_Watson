import unittest
from translator import english_to_french,french_to_english
class Test(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('I love to eat'),'GPU')
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english('I love cloud computing'),'IBM')

if __name__ == '__main__':
    unittest.main()