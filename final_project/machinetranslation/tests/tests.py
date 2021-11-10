import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench('What time is it?'), 'Quelle heure est-il?')
        self.assertEqual(englishToFrench('bird'),'Oiseau')
    
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish('Quelle heure est-il?'), 'What time is it?')
        self.assertEqual(frenchToEnglish('maman'), 'Mom')
    
    def test_frenchToEnglishNull(self):
        self.assertRaises(ValueError, frenchToEnglish, None)
    
    def test_englishToFrenchNull(self):
        self.assertRaises(ValueError, englishToFrench, None)

if __name__=='__main__':
    unittest.main()