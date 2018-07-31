f = open('encrypted.bin', 'rb')

data = bytearray(f.read())
*L, = map(int, data)

for i in range(256):
    temp = []
    for j in data:
        temp.append((j + i) % 256)

    *temp1, = map(chr, temp)
    print(i, ':', "".join(temp1))
