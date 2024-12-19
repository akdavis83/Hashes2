import hashlib, binascii
text = 'Hello, this is a hash.'
data = text.encode("utf8")
sha3_256 = hashlib.sha3_256(data).digest()
print("SHA3-256: ", binascii.hexlify(sha3_256))


