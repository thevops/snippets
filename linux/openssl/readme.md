# openssl

## HTTPS

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

## MAIL

IMAP via SSL uses port 993
POP3 via SSL uses port 995
SMTP via SSL uses port 465
```
openssl s_client -showcerts -connect mail.example.com:993 -servername mail.example.com
```

SMTP via TLS/StartTLS uses port 25 or 587
```
openssl s_client -starttls smtp -showcerts -connect mail.example.com:25  -servername mail.example.com
```
