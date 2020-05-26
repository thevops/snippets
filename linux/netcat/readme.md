# Netcat

copying files with netcat

```bash
# run receiver
nc -l -p PORT -q 5 | pv | gzip -dc | tar -xf -

# then run sender
tar -cf - PLIK --owner=0 --group=0 | pv -s $(du -sb . | awk '{print $1}') | gzip -9 -c | nc IP PORT -q 5
```

