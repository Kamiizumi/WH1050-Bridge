import sys
import subprocess
import shlex
import json
import urllib
from meteocalc import Temp, dew_point

args = str(sys.argv)

cmdtorun = shlex.split("rtl_433 -R 68 -F json -U -q")
process = subprocess.Popen(cmdtorun, stdout=subprocess.PIPE)
while True:
    output = process.stdout.readline()
    josn = json.loads(output)
    reportedTemp = Temp(josn['temperature_C'], 'c')
    calculatedDewPoint = dew_point(temperature=reportedTemp, humidity=josn['humidity'])
    wuformatted = {
        "action": "updateraw",
        "ID": sys.argv[1],
        "PASSWORD": sys.argv[2],
        "dateutc": josn['time'],
        "windspeedmph": josn['speed'] / 1.609344,
        "windgustmph": josn['gust'] / 1.609344,
        "humidity": josn['humidity'],
        "tempf": reportedTemp.f,
        "dewptf": calculatedDewPoint.f
    }
    requestdata = urllib.urlencode(wuformatted)
    url = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?%s" % requestdata
    result = urllib.urlopen(url)
    print(result.read().decode('utf-8'))