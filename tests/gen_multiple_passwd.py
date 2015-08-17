#!/usr/bin/python

import json
import random
import string
import sys


def random_string(length):
    return ''.join(random.choice(string.ascii_uppercase) for i in range(length))


start = 1025

with open(sys.argv[1], 'wb') as f:
    r = {
        'server': '0.0.0.0',
        'local_port': 1081,
        'timeout': 600,
        'method': 'aes-256-cfb'
    }
    ports = {}
    for i in range(start, start + 25):
        ports[str(i)] = random_string(8)

    r['port_password'] = ports
    print(r)
    f.write(json.dumps(r, indent=4).encode('utf-8'))
