import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime


#configurable variables, set to the correct values from read_solar.py
topath='/var/www/html/'
filename='solar_generated_power.csv'
figurename_power='power_vs_time.png'
figurename_daily='daily_yield.png'
figurename_total='total_yield.png'

#configure the x-scale of the plots
daystoshowpower=2
daystoshowenergy=31


solardata=pd.read_csv(topath+filename, sep=';')
solardata['date']=pd.to_datetime(solardata.timestamp, unit='s')

#plot power over last 2 days
fig1=plt.figure(figsize=(16,8))
plt.subplots_adjust(bottom=0.05)
plt.xticks( rotation=25 )
plt.rcParams.update({'font.size': 18})
ax=plt.gca()
ax.xaxis.set_major_formatter(md.DateFormatter('%a %H:%M'))
dstart_pow=datetime.datetime.now()-datetime.timedelta(days=daystoshowpower)
dend_pow=datetime.datetime.now()
plt.plot(solardata.date,solardata.currentpower,linewidth=5)
plt.ylabel('Generated power [W]')
plt.xlim([dstart_pow,dend_pow])
fig1.savefig(topath+figurename_power)

#plot daily yeild over last month
totdaily=solardata.set_index('date').groupby(pd.Grouper(freq='D')).agg('max')['yieldtoday']
fig2=plt.figure(figsize=(16,8))
plt.subplots_adjust(bottom=0.05)
plt.xticks( rotation=25 )
plt.rcParams.update({'font.size': 18 })
dstart=datetime.datetime.now()-datetime.timedelta(days=daystoshowenergy)
dend=datetime.datetime.now()
ax=plt.gca()
ax.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d'))
plt.plot(totdaily,linewidth=5)
plt.xlim([dstart,dend])
plt.ylabel('Energy per day [kWh]')
fig2.savefig(topath+figurename_daily)

# Plot total energy over the last month
fig3=plt.figure(figsize=(16,8))
plt.subplots_adjust(bottom=0.2)
plt.xticks( rotation=25 )
plt.rcParams.update({'font.size': 18 })
ax=plt.gca()
ax.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d'))
plt.plot(solardata[(solardata.date>dstart) & (solardata.date<dend)].date,solardata[(solardata.date>dstart) & (solardata.date<dend)].yieldtotal,'o')
plt.xlim([dstart,dend])
plt.ylim([min(solardata[(solardata.date>dstart) & (solardata.date<dend)].yieldtotal),solardata.tail(1).yieldtotal.values])
plt.ylabel('Total energy over time [kWh]')
fig3.savefig(topath+figurename_total)

