# Read and display sofar solar SH1ES136 data

These python scripts are made to run on an always-on raspberry pi with a wireless connection to the sofar solar SH1ES136 invertor.
The read_solar.py makes a GET request to http://10.10.100.254/status.html (which is the default ip address of my invertor).
Here we extract the current power, daily total energy and total energy as reported by the invertor.
This is written to a csv file that should be initialised with:

`timestamp;currentpower;yieldtoday;yieldtotal`

By default this csv file is placed in `/var/www/html/` so the script will need write access to that folder.
Using this we can use a webserver (such as nginx) to make the csv file available to read by going to `http://ip.address.of.ip/solar_generated_power.csv`
The idea is to run this script at regular intervals with `crontab -e`, something like:

`* * * * * /usr/bin/python3 /home/pi/read_solar.py`

The `show_solar.py` script reads the csv file and plots the result. The plots are written as a png image and also places in `/var/www/html`.
This second script is also supposed to be run on a regular interval to keep the plots up to date, though it can probably be run every 10 minutes like so:

`*/10 * * * * /usr/bin/python3 /home/pi/show_solar.py`

The `html/index.html` file is a *very* simple html index file to just server up the two plots.

The scripts depend on a few python packages:

```
requests
re
time
os
pandas
matplotlib
datetime
```
