#!/usr/bin/env python

import smtplib
import subprocess

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# fromaddr == my email address
# toaddr == recipient's email address
fromaddr = "UnixOperations@emerson.com"
toaddr = [ "sahil.suri@emerson.com", "amit.kumar@emerson.com" ]
cc = [ "sahil.suri@emerson.com", "abc@example.com" ]
toaddrs =  toaddr + cc 


#Server count for assets#
linux_phy=subprocess.check_output("/export/home/rlampart/bin/ExtractServers.sh -o LINUX -t PHY -c", shell=True)
linux_vir=subprocess.check_output("/export/home/rlampart/bin/ExtractServers.sh -o LINUX -t VIR -c", shell=True)
linux_con_hosts=subprocess.check_output("/export/home/rlampart/bin/ExtractServers.sh -o LINUX -t PHY | grep lxc | wc -l", shell=True)
linux_con=subprocess.check_output("/export/home/rlampart/bin/ExtractServers.sh -v u7c -c", shell=True)

sol_phy=subprocess.check_output("/export/home/rlampart/bin/ExtractServers.sh -o GLO | egrep -c '\-p$'", shell=True)
sol_guest=subprocess.check_output("/export/home/rlampart/bin/ExtractServers.sh -o GLO | egrep -c '\-g$'", shell=True)
sol_zon=subprocess.check_output("/export/home/rlampart/bin/ExtractServers.sh -o ZON -c", shell=True)

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Unix/Linux Server Count Report"
msg['From'] = fromaddr
msg['To'] = ",".join(toaddr)
msg['Cc'] = ",".join(cc)

# Create the body of the message (a plain-text and an HTML version).
html = """\
<html>
<head>
  <style>
  table,
  th, td {
      padding: 10px;
      border: 1px solid black;
      border-collapse: collapse;
    }
  </style>
  </head>
  <body>
  Hello,<br><br>
  Please find below UNIX/LINUX server asset report.</br><br>
  <b>Linux</b><br>
  <table cellpadding="0" cellspacing="0" cellpadding="5" >    
  <tr><td>Physical servers (including container hosts)</td><td>%s</td></tr> 
   <tr><td>Virtual servers</td><td>%s</td></tr>
   <tr><td>Container hosts</td><td>%s</td></tr>
   <tr><td>Containers (containers excluding physical hosts)</td><td>%s</td></tr>
   </table>
   <br><b>Solaris</b><br>
  <table cellpadding="0" cellspacing="0" cellpadding="5">    
  <tr><td>Physical servers (Primary domains) </td><td>%s</td></tr> 
   <tr><td>Guest domains</td><td>%s</td></tr>
   <tr><td>Local Zones</td><td>%s</td></tr>
   </table>
   <br>** This is an auto-generated email. Please do not reply. **<br>
  </body>
</html>
""" % (linux_phy, linux_vir, linux_con_hosts, linux_con, sol_phy, sol_guest, sol_zon)

# Record the MIME types of both parts - text/plain and text/html.
email_body = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(email_body)

# Send the message via local SMTP server.
s = smtplib.SMTP('localhost')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(fromaddr, toaddrs, msg.as_string())
s.quit()
