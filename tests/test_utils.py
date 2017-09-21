import unittest

from expynent.utils import is_private


class UtilsTestCase(unittest.TestCase):
    def test_is_private(self):
        private_attr = '_IP_CUSTOM'
        public_attr = 'IPv6'
        self.assertTrue(is_private(private_attr))
        self.assertFalse(is_private(public_attr))
