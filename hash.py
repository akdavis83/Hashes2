import hashlib, binascii
text = 'Hello, this is a hash.'
data = text.encode("utf8")
sha256hash = hashlib.sha256(data).digest()
print("SHA256: ", binascii.hexlify(sha256hash))
