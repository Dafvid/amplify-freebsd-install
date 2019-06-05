# Usage
Less invasive install script for nginx amplify

```sh
pkg install py27-virtualenv
python2 -m virtualenv /path/to/virtualenv --system-site-packages
```
Add `/path/to/virtualenv` to amplify-freebsd-install.sh

`env API_KEY='yourapikey' sh ./amplify-freebsd-install.sh`

If you get an error on `cryptography` check your version of setuptools so it's > 39.6.0.

Otherwise update with `pkg install py27-setuptools`

The `SyntaxError: invalid syntax` message can safely be ignored

Add the `amplify` rc script to `/usr/local/etc/rc.d`

Start with `service amplify start`
