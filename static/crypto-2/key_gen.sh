openssl genpkey \
  -algorithm RSA \
  -pkeyopt rsa_keygen_bits:512 \
  -pkeyopt rsa_keygen_pubexp:3 \
  -out private.pem
openssl rsa -in private.pem -pubout -out public.pem
openssl rsa -in private.pem -text -noout
