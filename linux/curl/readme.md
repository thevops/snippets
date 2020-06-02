# curl

imap via curl
```bash
# https://debian-administration.org/article/726/Performing_IMAP_queries_via_curl
curl --url "imap://mail.example.com/" --user "bobby:tables"
```

get only status code
```bash
curl -s -o /dev/null -w "%{http_code}" http://www.example.org/
```

extract text between tag
```
tag=head
curl -s https://webiste.pl | sed -n "/<$tag>/,/<\/$tag>/p"
```
