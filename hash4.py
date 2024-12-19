import hashlib, binascii
text = 'Hello, this is a hash.'
data = text.encode("utf8")
sha512hash = hashlib.sha512(data).digest()
print("SHA512: ", binascii.hexlify(sha512hash))
