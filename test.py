import unittest
import url_obfuscator

class TestUrlObfus(unittest.TestCase):
    def test_ip(self):
        self.assertEqual(url_obfuscator.ipv4_lookup("www.facebook.oneonestkst")[0], 2)
        self.assertEqual(url_obfuscator.ipv4_lookup("www.facebook.com")[1], "31.13.73.39")

if __name__ == '__main__':
    unittest.main()
