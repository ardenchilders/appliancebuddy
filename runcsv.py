import requests
import time
import csv

url_switch_on  = 'http://172.20.10.3/on'
url_switch_off = "http://172.20.10.3/off"
sonoff_url     = "NOT_INIT"

def main():
        with open('newcarbon.csv', 'r') as csvfile:
          csvreader = csv.reader(csvfile, delimiter = ',')
          for row in csvreader:
            if( int(float(row[1])) > 5100):
              sonoff_url = url_switch_off
              print('- OFF -', 'Carbon Emission: ', int(float(row[1])))
              requests.post(sonoff_url)
            else:
              sonoff_url = url_switch_on
              print('- ON -', 'Carbon Emission: ', int(float(row[1])))
              requests.post(sonoff_url)
          time.sleep(1)
main()
