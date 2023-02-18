#!/usr/bin/env python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "UnixOperations@emerson.com"
you = "sahil.suri@emerson.com"

demo_var = "this is a test line"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Unix/Linux Server Count Report"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
        %s <br>
       Here is the <a href="https://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
""" % (demo_var)

# Record the MIME types of both parts - text/plain and text/html.
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('localhost')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()
