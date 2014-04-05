__author__ = 'Administrator'
#coding=utf-8

import paramiko,time,re

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.88.11",22,"admin", "admin")
myssh = ssh.invoke_shell()
print "Interactive SSH session established"
# Strip the initial router prompt
#output = myssh.recv(1000)
# See what we have
#print output
#stdin, stdout, stderr = ssh.exec_command("more /var/log/syslog")
myssh.send("dis interface GigabitEthernet 0/0/3\n")
time.sleep(1)
myssh.send(" \n \n \n \n")
time.sleep(3)
myssh.send(" \n")
time.sleep(1)
myssh.send("dis cu\n")
myssh.send(" \n \n \n \n \n")
time.sleep(3)
output = myssh.recv(12000)
#print output
text = output
mypattern  = r'  ---- More ----.*\[42D.*\[42D'
match = re.search(mypattern, text)
if match:
        result = match.group()
        newtext = re.sub(mypattern, "", text)
       # print result  #+ "===Yes==="
        print newtext
else:
         result = "===NO==="
         print result


#print stdout.readlines()

ssh.close()

