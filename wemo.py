#!/usr/bin/env python

# Tom Luo
# tom.luo@csoxfordalumni.org
# Calgary

import subprocess as s
import sys
from datetime import datetime,date,timedelta
from astral import Astral
#sudo pip install astral

city_name = 'Calgary'
a = Astral()
a.solar_depression = 'civil'
city = a[city_name]
print('Information for %s/%s\n' % (city_name, city.region))
timezone = city.timezone
print('Timezone: %s' % timezone)
print('Latitude: %.02f; Longitude: %.02f\n' % (city.latitude, city.longitude))
#sun = city.sun(date=datetime.date(2009, 4, 22), local=True)
sun = city.sun(date.today(), local=True)
print('Dawn:    %s' % str(sun['dawn']))
print('Sunrise: %s' % str(sun['sunrise']))
print('Noon:    %s' % str(sun['noon']))
print('Sunset:  %s' % str(sun['sunset']))
print('Dusk:    %s' % str(sun['dusk']))

now = datetime.now()
dawn = sun['dawn']
sunrise = sun['sunrise']
sunset = sun['sunset']
dusk = sun['dusk']

print "now"
print now.day, now.hour, now.minute


if (now.hour == sunset.hour and now.minute == sunset.minute) or (now.hour == dawn.hour and now.minute == dawn.minute):
   print "turn on light at sunse or dawn"
   s.Popen(["wemo", "switch", "East", "on"])
elif (now.hour == dusk.hour and now.minute == dusk.minute) or (now.hour == sunrise.hour and now.minute == sunrise.minute):
   print "turn off light at dusk or sunrise"
   s.Popen(["wemo", "switch", "East", "off"])
elif (now.hour == 21 or now.hour == 8):
   s.Popen(["wemo", "switch", "East", "off"])
