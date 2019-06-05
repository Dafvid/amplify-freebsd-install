## amplify-freebsd-install
Less invasive install script for nginx amplify

```sh
pkg install py27-virtualenv
python2 -m virtualenv /path/to/virtualenv
```
Add `/path/to/virtualenv` to amplify-freebsd-install.sh

`env API_KEY='yourapikey' sh ./amplify-freebsd-install.sh`

Add the amplify rc script to `/usr/local/etc/rc.d`

Start with `service amplify start`
