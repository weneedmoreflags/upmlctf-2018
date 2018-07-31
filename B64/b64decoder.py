msg = 'RKBoNZxWMHInBXFTMn3VBJBdMpxVAL/cB46nR3xeA4hZ'
abc = './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

a = [abc.index(i) for i in msg]
print("Этап 1: ", a)

a = ''.join(['{:0>6}'.format(bin(i)[2:]) for i in a])
print("Этап 2: ", a)


ans = ""
for i in range(0, len(a) - 1, 8):
    ans += chr(int(a[i:i+8], 2))

print("Ответ: ", ans)
