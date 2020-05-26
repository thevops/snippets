# Find, ack, grep

## Find

find biggest files
```bash
find -printf '%s %p\n'| sort -nr | head -10 | awk '{print $1/1024/1024 " MB", $2}'
```

find not newer than date and remove
```bash
find . -not -newermt 2018-01-01 -exec rm {} \;
```

copy files from specific date
```bash
month="Mar-2010"
find . -newermt "01-$month -1 sec" -and -not -newermt "01-$month +1 month -1 sec" -exec cp -p {} /dest/path/ \;
```

files than have perms other than
```bash
find -type f -not -perm 0644
find -type d -not -perm 0755
```

repair this…
```bash
find * -type f -exec chmod 0644 {} \;
find . -type d -exec chmod 0755 {} \;
```

find files with execute permission
```bash
find /some/dir/ -type f ! -user root -perm /u=x,g=x,o=x -exec ls -la {} \;
```


remove files from tmp dir
```bash
find /some/dir/* -user USERNAME -exec rm {} \;
```

find latest modified file
```bash
find ./ -type f -print0 | xargs -0 stat --format '%Y :%y %n' | sort -nr | cut -d: -f2- | head
```

files modified in last 15 days
```bash
find ./ -type f -mtime -15
```

find files and sort
```bash
find . -type f -printf '%TY-%Tm-%Td %TT %p\n' | sort -r
```

find directories with chmod 000
```bash
find . ! -perm -u=r ! -perm -u=w ! -perm -u=x
```




## ack

```bash
ack -f # zwraca wszystkie pliki
ack restrict # szuka slowa: restrict, restricted itp
ack -w slowo # szuka slowa tylko restrict
ack -w --python restrict # szuka w pythonowych plikach
ack -c restrict # zwraca kazdy plik i ile razy wystapilo slowo
ack -ch restrict # zlicza ilosc wystapien ogolnie
ack -cl restrict # zwraca kazdy plik gdzie ilosc jest wieksza od 0
-C # jak w grepie
-g cos # szuka wyrazenia cos w sciezce pliku
tail /var/log/kern.log | ack --cc 'DST=(.*?) ' --output '$1' -h
```

## grep

all IPv4 from file
```bash
grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' file.txt
```

all mails from file
```bash
grep -E -o "\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b" /var/log/mail.log | sort | uniq -i > /file.txt
```


few letters before and after
```bash
echo "some123_string_and_another" | grep -o -P '.{0,3}string.{0,4}'
```

