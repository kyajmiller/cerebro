from TestThis import TestThis
import unittest
from ClassModels.DumbClass import DumbClass
from ClassModels.SUDBConnect import SUDBConnect



class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)
  def test_me(self):
        self.assertEqual("x","x")

  def testTestThis(self):
      example=TestThis("Hello world")
      self.assertEqual("Hello world",example.getVal())
  def testClassy(self):
      dumber=DumbClass("test")
      self.assertEqual("test",dumber.getVal())


if __name__ == '__main__':
    unittest.main()