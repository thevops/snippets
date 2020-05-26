# SWAP


check some configurations
```bash
cat /proc/sys/vm/swappiness
/etc/sysctl.conf => vm.swappiness = 10
sysctl -p
```

create swapfile
```bash
dd if=/dev/zero of=test.img bs=1024 count=$((1048576*1))
# or
fallocate -l 2G /swapfile
chown root:root /swapfile
chmod 0600 /swapfile
mkswap /swapfile
swapon /swapfile
# vim /etc/fstab and paste: /swapfile none swap sw 0 0
```