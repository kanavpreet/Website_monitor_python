import request
import smtplib
import os
from  linode_api4 import LinodeClient,Instance

EMAIL_ADDRESS=os.environ.get('EMAIL_ID')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASS') 

def notify_user():
with smptplib.SMTP('GMAIL.COM',587) as smtp:
      smtp.ehlo()
      smtp.starttls()
      smtp.ehlo()
      smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD) 
      subject='Website is Down!!'
      body="Website is down , we are restarting the movie"
      msg = f'Subject: {subject}\n\n{body}'
      smtp.sendmail(EMAIL_ADDRESS, 'INSERT_RECEIVER_ADDRESS', msg)
 
 
####To reboot the server, we are doing from linode lib. First we need to setup linode ##
##set linode token o site##
 def reboot_server():
    client =LinodeClient(LINODE_TOKEN)
    server=client.load(Instance, <>)
     server.reboot() 


try:
r=request.get ('https://onlinebookstore.com',timeout=5)
##trying to get request status from website and setting up the timeout for 5 sec.

if r.status_code !=200:
# Not ok status
notify_user()
reboot_server()
else:
#Status is ok
except Exception as e:
 notify_user()
 reboot_server()

 
      
 
