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

show memory consumed in MB
```bash
ps -eo size,pid,user,command --sort -size | awk '{ hr=$1/1024 ; printf("%13.2f Mb ",hr) } { for ( x=4 ; x<=NF ; x++ ) { printf("%s ",$x) } print "" }'
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
