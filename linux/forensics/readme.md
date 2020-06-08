
# find processes that hide as system threads
system threads not have maps
```bash
ps auxw | awk '{print $11,$2}' | grep ^\\[ | awk '{print $2}' | xargs -I % sh -c 'echo PID: %; cat /proc/%/maps' 2> /dev/null
```

system threads not have binary files
```bash
ps auxww | awk '{print $11,$2}' | grep ^\\[ | awk '{print $2}' | xargs -I % sh -c 'echo PID: %; sha1sum /proc/%/exe' 2> /dev/null
```
