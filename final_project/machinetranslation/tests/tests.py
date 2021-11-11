import unittest
from ..translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('What time is it?'), 'Quelle heure est-il?')
        self.assertEqual(english_to_french('bird'),'Oiseau')
    
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Quelle heure est-il?'), 'What time is it?')
        self.assertEqual(french_to_english('maman'), 'Mom')
    
    def test_frenchToEnglishNull(self):
        self.assertRaises(ValueError, french_to_english, None)
    
    def test_englishToFrenchNull(self):
        self.assertRaises(ValueError, english_to_french, None)

if __name__=='__main__':
    unittest.main()
