#!/usr/bin/python3
import unittest
import url_obfuscator
from random import seed

class TestUrlObfus(unittest.TestCase):
    def test_ip(self):
        self.assertEqual(url_obfuscator.ip_lookup("www.github.oneonsot"), "IP error")

    def test_split_ip(self):
        self.assertEqual(url_obfuscator.split_ip("127.0.0.1"), [127,0,0,1])

    def test_ip_octal(self):
        seed(1)
        ip = url_obfuscator.split_ip("127.0.0.1")
        ip = '.'.join([url_obfuscator.to_oct(i) for i in ip])
        self.assertEqual(ip, "00177.000000.00.0001")

    def test_ip_hex(self):
        ip = url_obfuscator.split_ip("127.0.0.1")
        ip = '.'.join([url_obfuscator.to_hex(i) for i in ip])
        self.assertEqual(ip, "0x7f.0x00.0x00.0x01")

    def test_ip_dword(self):
        ip = url_obfuscator.split_ip("127.0.0.1")
        self.assertEqual(url_obfuscator.ip_dword(ip), 2130706433)
        self.assertEqual(url_obfuscator.ip_dword(ip[1:]), 1)

    def test_dummy_auth(self):
        seed(1)
        self.assertEqual(url_obfuscator.dummy_auth(), "i)A0@")

    def test_hext_obfus(self):
        self.assertEqual(url_obfuscator.hext_obfus("////"), "////")
        seed(1)
        self.assertEqual(url_obfuscator.hext_obfus("/test_string.html"), "/te%73t%5f%73%74%72in%67.%68%74m%6c")


if __name__ == '__main__':
    unittest.main()
