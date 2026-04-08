from Crypto.Util.number import bytes_to_long

msg = b"42ctf{s1z3_m4tt3rs}"
m = bytes_to_long(msg)

# load public key
from Crypto.PublicKey import RSA
key = RSA.import_key(open("public.pem").read())

n = key.n
e = key.e

# ensure vulnerability condition
assert m**3 < n

# textbook RSA
c = pow(m, e, n)

# export
with open("ciphertext.txt", "w") as f:
    import base64
    f.write(base64.b64encode(c.to_bytes((c.bit_length()+7)//8, "big")).decode())
