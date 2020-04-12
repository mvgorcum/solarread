import requests
import re
import time
import os

#configurable variables
topath='/var/www/html/'
filename='solar_generated_power.csv'
hostname='10.10.100.254'
username='admin'
password='admin'

#test if the inverter is accesible
isup = os.system("ping -c 1 " + hostname)

#read data from inverter
if isup == 0:
    session = requests.Session()
    session.auth = (username, password)
    ts = int(time.time()) 
    auth = session.post('http://' + hostname)
    response = session.get('http://' + hostname + '/status.html')
    blaat=response.content
    for line in response.content.decode("utf-8").splitlines():
        if re.search('var webdata_now_p', line):
            powernow=float(re.findall(r"[-+]?\d*\.\d+|\d+",line)[0])
        if re.search('var webdata_today_e', line):
            energytoday=float(re.findall(r"[-+]?\d*\.\d+|\d+",line)[0])
        if re.search('var webdata_total_e', line):
            energytotal=float(re.findall(r"[-+]?\d*\.\d+|\d+",line)[0])
    appendvar=str(ts)+';'+str(powernow)+';'+str(energytoday)+';'+str(energytotal)+'\n'
    f=open(topath+filename,'a+')
    f.write(appendvar)
    f.close()