# metrics

## ps
```bash
ps -ax -o pid,user:20,%mem,%cpu,etime,cmd --sort=-%cpu
ps -T -o lstart,pcpu,pmem,cmd -p
```


## stats

dstat
```bash
dstat -t -l -c -m -s -d -r -n -N eth0
```

cpu
```bash
mpstat -P ALL {sec} {delay}
```

mem
```bash
vmstat -wt -SM {sec} {delay}
```

io
```bash
iostat -k(x) {sec} {delay}
# or
iotop
```

network 
```bash
iftop
# or
iftop -t -i eth0 -Nn
# or
ifstat -i eth0 -t {sec} {delay}
```
