**check number of arguments**
```bash
[ $# -lt 1 ] && { echo "not enough arguments"; exit 1; }
echo "do something"
```

**check for exit all vim prcesses in loop and notify if true**
```bash
while :; do [[ "$(ps axuf|grep [v]im | wc -l)" != "0" ]] && date && sleep 1 || break; done; echo "send notify"
```