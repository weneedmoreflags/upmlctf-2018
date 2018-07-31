import sys

def rev(x):
    u = hex(x)[2:]
    u = '0' * (2 - len(u)) + u
    return int(u[::-1], 16)

l = bytearray(open(sys.argv[1], mode = 'rb').read())
l = l[::-1]

for i in range(len(l)): l[i] = rev(l[i])

open(sys.argv[2], mode = 'wb').write(l)
