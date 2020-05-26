# iptables


the most effective drops
`iptables -I PREROUTING -t raw -d IP -j DROP`

bulk remove rules (first column in 'iptables -S' is '-A')
`iptables -S | grep | awk '{$1=""; print $0}' | while read line; do echo "iptables -D $line"; done`
