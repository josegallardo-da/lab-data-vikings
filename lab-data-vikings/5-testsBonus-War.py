import unittest
from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon
from inspect import signature


class TestWar(unittest.TestCase):
    @classmethod
    def setUp(cls):
        def generateViking():
            cls.name = 'Harald'
            cls.strength = 150
            cls.health = 300
            return Viking(cls.name, cls.health, cls.strength)

        def generateSaxon():
            cls.health = 60
            cls.strength = 25
            return Saxon(cls.health, cls.strength)

        cls.viking = generateViking()
        cls.saxon = generateSaxon()
        cls.war = War()
        cls.war.addSaxon(cls.saxon)
        cls.war.addViking(cls.viking)

    def testAddVikingRaiseError(self):
        self.assertRaisesRegex(ValueError, "*Viking", self.war.addViking(self.saxon))
        pass
    
    def testAddSaxonRaiseError(self):
        self.assertRaisesRegex(ValueError, "*Saxon", self.war.addSaxon(self.viking))
        pass

if __name__ == '__main__':
    unittest.main()
