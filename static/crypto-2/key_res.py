import base64
import gmpy2
from Crypto.Util.number import long_to_bytes

# Load ciphertext
with open("ciphertext.txt") as f:
    c_b64 = f.read()

c_bytes = base64.b64decode(c_b64)
c = int.from_bytes(c_bytes, "big")

# Cube root attack
m, exact = gmpy2.iroot(c, 3)

if not exact:
    print("Not vulnerable")
    exit()

plaintext = long_to_bytes(m)
print(plaintext.decode())
