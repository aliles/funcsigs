try:
    # python 2.x
    import unittest2 as unittest
except ImportError:
    # python 3.x
    import unittest

import doctest

import funcsigs


class TestFunctionSignatures(unittest.TestCase):

    def test_has_version(self):
        self.assertTrue(funcsigs.__version__)

    def test_readme(self):
        doctest.testfile('../README.rst')
