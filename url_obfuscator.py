#!/usr/bin/python3

from random import randint, seed
from urllib.parse import urlparse, urlunparse
from socket import gethostbyname

def ip_lookup(url):
    try:
        res = gethostbyname(url)
    except:
        res = "IP error"
    return res

def to_oct(n):
    leading_zero = '0' * randint(1,6)
    return '{}{:o}'.format(leading_zero, n)

def to_hex(n): return '0x{:02x}'.format(n)

def split_ip(ip): return [int(i) for i in ip.split('.')]

def ip_dword(ip):
    "convert rightmost portion of ip to decimal, given full ip 32 bit max"
    r = 0
    v = 1
    for i in reversed(ip):
        r += i * v
        v <<= 8 
    return r

def dummy_auth():
    "add random text before @ as dummy auth"
    leng = randint(0, 20)
    str = ""
    for i in range(leng): str += chr(randint(33,126))
    return str + '@'

def hext_obfus(text):
    "obscure text in path by replacing with hex values; apart from /"
    str = ""
    for c in text:
        if c != '/' and randint(0,1):
            c = '%{:x}'.format(ord(c))
        str += c
    return str


if __name__ == "__main__":
    seed(1)
    url = "http://github.com/test_path.htm"
    o = list(urlparse(url))
    print(o)
    ip = ip_lookup(o[1])
    if ip != "IP error":
        o[1] = ip
    o[1] = dummy_auth() + o[1]
    o[2] = hext_obfus(o[2])
    print(urlunparse(o))

    tt = split_ip("127.0.0.1")
    print(ip_dword(tt))
