import unittest
from translator import english_to_french, french_to_english


#from translator import english_to_french, french_to_english
#from .subpackage.module import CONSTANT


class testE2F (unittest.TestCase):
    def test1 (self):
        self.assertNotEqual (english_to_french, False)
        self.assertEqual (english_to_french('Hello'),'Bonjour')
        self.assertEqual (english_to_french("Road"),"Route")
        self.assertEqual (english_to_french("City"),"Ville")

class testF2E (unittest.TestCase):
    def test2 (self):
        self.assertNotEqual (french_to_english, False)
        self.assertEqual (french_to_english("Bonjour"),"Hello")
        self.assertEqual (french_to_english("Route"),"Road")
        self.assertEqual (french_to_english("Ville"),"City")


unittest.main()