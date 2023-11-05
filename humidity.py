#importing required pacakages
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import sys
import urllib.request as urllib2

myAPI = 'XNXF3SOUKNN3R7KG' #Enter Your Write Api Key
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 
GPIO.setmode(GPIO.BCM)
sensor = Adafruit_DHT.DHT11
pin = 23
while True:
    
 #Reading Data From Sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is None and temperature is None:
        print("Failed")
        time.sleep(0.5)
    else:
        print(f"Temperature: {temperature} , Humidity: {humidity}")
 #Type casting Variables To send Towards Api
        humidity = '%.2f' %humidity
        temperature = '%.2f' %temperature
 
 # Establishing Connection With Api
        conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s' % (temperature, humidity))
 
        print(conn.read()) #checking that connection is establoished
 
        conn.close() #Closing Connection After Sending Data
 
        time.sleep(0.5)
        