#!/bin/bash
ufw allow 8000
sed -i "s/Listen 81/Listen 10000/" /etc/apache2/ports.conf
/etc/init.d/apache2 start
python3 -m app