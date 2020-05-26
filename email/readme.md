# Email

check open relay
`nmap --script smtp-open-relay.nse -p 25,465,587,110,143,993,995 mail.domain.pl`

check SSL cert
`nmap --script ssl-cert -p 25,465,587,110,143,993,995 mail.domain.pl`

check commands
`nmap --script smtp-commands.nse -Pn -pT:25,465mail.domain.pl.pl`


default tls
`openssl s_client -connect mail.domain.pl:465`


testssl
```bash
# apt-get install testssl.sh
testssl mail.domain.pl:465
testssl mail.domain.pl:993
testssl -t smtp mail.domain.pl:25
testssl -t smtp mail.domain.pl:587
```
