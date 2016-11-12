import sys
import subprocess
import shlex
import json
import urllib

args = str(sys.argv)

cmdtorun = shlex.split("rtl_433 -R 68 -F json -U -q")
process = subprocess.Popen(cmdtorun, stdout=subprocess.PIPE)
while True:
    output = process.stdout.readline()
    josn = json.loads(output)
    wuformatted = {
        "action": "updateraw",
        "ID": args[1],
        "PASSWORD": args[2],
        "dateutc": josn['time'],
        "windspeedmph": josn['speed'] / 1.609344,
        "windgustmph": josn['gust'] / 1.609344,
        "humidity": josn['humidity'],
        "tempf": (josn['temperature_C'] * 1.8) + 32
    }
    requestdata = urllib.urlencode(wuformatted)
    url = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?%s" % requestdata
    result = urllib.urlopen(url)
    print(result.read().decode('utf-8'))