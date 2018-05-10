# WH1050 Bridge

Bridges a Fine Offset WH1050 weather station to the Weather Underground service, using an RTL-SDR.

## Requirements

To use the script the following hardware and software is required:

- Python 3+
- [WH1050 / WH1070](http://www.foshk.com/weather_professional/wh1070.html) based weather station
  - Re-branded example: [Maplin N25FR](http://www.maplin.co.uk/p/wireless-weather-station-n25fr)
- An RTL based SDR reciever (see [http://www.rtl-sdr.com/about-rtl-sdr/](http://www.rtl-sdr.com/about-rtl-sdr/) for examples)
- [rtl_433](https://github.com/merbanan/rtl_433) installed on system PATH
- Weather station registered on Weather Underground's [Personal Weather Station Network](https://www.wunderground.com/personal-weather-station/signup.asp)
- Python packages installed via `pip install -r requirements.txt`

## Usage

1. Ensure requirements above are satisfied
1. Run `python wsbridge.py [STATION ID] [STATION KEY]`
1. Wait for a report from the station to be recieved by the SDR (~40 seconds) and check PWS on Weather Underground
