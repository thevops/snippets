# openssl

check
```bash
openssl s_client -servername domena.pl -connect domena.pl:443
openssl rsa -check -in priv.key
openssl x509 -text -noout -in certificate.crt
```

check MD5
```bash
openssl x509 -noout -modulus -in crt.crt | openssl md5
openssl rsa -noout -modulus -in priv.key | openssl md5
openssl req -noout -modulus -in csr.csr | openssl md5
```

get cert from website
```bash
echo -n | openssl s_client -connect strona.pl:443 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > strona.cert
```