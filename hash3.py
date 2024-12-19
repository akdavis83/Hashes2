import hashlib, binascii
text = 'Hello, this is a hash.'
data = text.encode("utf8")
ripemd160 = hashlib.new('ripemd160', data).digest()
print("RIPEMD-160:", binascii.hexlify(ripemd160))


