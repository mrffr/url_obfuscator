#!/usr/bin/env python3

import argparse
from random import randint
from urllib.parse import urlparse, urlunparse
import socket


def ip_lookup(hostname):
    try:
        res = socket.gethostbyname(hostname)
    except socket.gaierror:
        res = "IP error"
    return res


def to_oct(n):
    leading_zero = '0' * randint(1, 6)
    return '{}{:o}'.format(leading_zero, n)


def to_hex(n):
    return '0x{:02x}'.format(n)


def split_ip(ip_str):
    return [int(i) for i in ip_str.split('.')]


def ip_dword(ip):
    "convert rightmost portion of ip to decimal"
    r = 0
    v = 1
    for i in reversed(ip):
        r += i * v
        v <<= 8
    return r


def dummy_auth():
    "add random text before @ as dummy auth"
    leng = randint(0, 20)
    st = ""
    for i in range(leng):
        c = chr(randint(33, 126))
        # some characters noticed not working on chromium
        if c == '/' or c == '?' or c == '#' or c == '\\':
            continue
        st += c
    return st + '@'


def hext_obfus(text):
    "obscure text in path by replacing with hex values; apart from /"
    st = ""
    for c in text:
        if c != '/' and randint(0, 1):  # 50% chance per char
            c = '%{:x}'.format(ord(c))
        st += c
    return st


def obscure_ip(ip_str):
    "randomly obscures ip by using oct, hex or decimal"
    ip = split_ip(ip_str)
    st = []
    for i in range(len(ip)):
        choice = randint(0, 2)
        if choice == 0:
            st.append(to_oct(ip[i]))
        elif choice == 1:
            st.append(to_hex(ip[i]))
        else:
            st.append(str(ip_dword(ip[i:])))  # rest of ip
            break
    return '.'.join(st)


def obfuscate_url(url, change_hostname, add_auth):
    ob = list(urlparse(url))

    if change_hostname:
        ip = ip_lookup(ob[1])
        if ip == "IP error":
            return ip
        ob[1] = obscure_ip(ip)

    if add_auth:
        ob[1] = dummy_auth() + ob[1]

    ob[2] = hext_obfus(ob[2])

    return urlunparse(ob)


def main():
    parser = argparse.ArgumentParser(description='Obfuscate a url.')
    parser.add_argument('url', type=str)
    parser.add_argument(
        '--no_host', help='keep hostname useful due to CDN like cloudflare',
        action='store_false')
    parser.add_argument(
        '--no_auth', help='no dummy auth added to hostname',
        action='store_false')
    args = parser.parse_args()
    print(obfuscate_url(args.url, args.no_host, args.no_auth))
    return


if __name__ == "__main__":
    main()
