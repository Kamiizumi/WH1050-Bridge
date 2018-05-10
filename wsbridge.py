""" Script to parse rtl_433 output and send to Weather Underground """

import sys
import subprocess
import shlex
import json
import urllib
import urllib.parse
import urllib.request
from meteocalc import Temp, dew_point

RTL_COMMAND = shlex.split("rtl_433 -R 69 -F json -U -q")
RTL_PROCESS = subprocess.Popen(RTL_COMMAND, stdout=subprocess.PIPE)
while True:
    try:
        RTL_PROCESS_OUTPUT = RTL_PROCESS.stdout.readline().decode('utf-8')

        OUTPUT_AS_JSON = json.loads(RTL_PROCESS_OUTPUT)
        REPORTED_TEMP = Temp(OUTPUT_AS_JSON['temperature_C'], 'c')
        CALCULATED_DEW_POINT = dew_point(temperature=REPORTED_TEMP, humidity=OUTPUT_AS_JSON['humidity'])
        REQUEST_OBJECT = {
            "action": "updateraw",
            "ID": sys.argv[1],
            "PASSWORD": sys.argv[2],
            "dateutc": OUTPUT_AS_JSON['time'],
            "windspeedmph": OUTPUT_AS_JSON['speed'] / 1.609344,
            "windgustmph": OUTPUT_AS_JSON['gust'] / 1.609344,
            "humidity": OUTPUT_AS_JSON['humidity'],
            "tempf": REPORTED_TEMP.f,
            "dewptf": CALCULATED_DEW_POINT.f
        }

        REQUEST_ENCODED = urllib.parse.urlencode(REQUEST_OBJECT)
        REQUEST_URL = \
            "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?%s" \
            % REQUEST_ENCODED

        REQUEST_RESULT = urllib.request.urlopen(REQUEST_URL)
        print(REQUEST_RESULT.read().decode('utf-8'))

    except Exception as exception:
        print(exception)
