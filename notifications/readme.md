# Notifications with curl

curl, notica
```bash
curl -d "d:TEXT" "https://notica.us/?YOURADDRESS"
```



sending encrypted data with termbin.com
```bash
# send
cat somefile.txt | openssl aes-256-cbc -a -salt -k PASSWORD | nc termbin.com 9999

# receive
curl -s http://termbin.com/SOMETHING | openssl aes-256-cbc -a -d -salt -k PASSWORD
```

sprunge
```bash
echo something | curl -F 'sprunge=<-' http://sprunge.us
```
