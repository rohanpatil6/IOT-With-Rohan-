import RPi.GPIO as GPIO
import time
# Setup GPIO
GPIO.setwarnings(False)
TRIG = 11
ECHO = 8
servoPIN = 18
GPIO.setmode(GPIO.BCM)
# Ultrasonic sensor pin initialization
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN) # Corrected line: Set ECHO pin as input
# Servo motor pin initialization
GPIO.setup(servoPIN, GPIO.OUT)
servo = GPIO.PWM(servoPIN, 50)
servo.start(2.5)

try:
    while True:
        GPIO.output(TRIG, False)
        time.sleep(0.000002)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        startTime = time.time()
        stopTime = time.time()
        
        while GPIO.input(ECHO) == 0:
            startTime = time.time()
        while GPIO.input(ECHO) == 1:
            stopTime = time.time()
        GPIO.output(TRIG, True)
        timeElapsed = stopTime - startTime
        distance = (timeElapsed * 34300) /2
        distance = int(distance)
        print("Distance: {} cm".format(distance))
        
        if distance <= 30:
            duty_cycle = 12.5 # Adjust this value for desired servo position
            
            servo.ChangeDutyCycle(duty_cycle)
            print("Motor Rotated")
            time.sleep(0.1)
        else:
            duty_cycle = 2.5 # Adjust this value for desired servo position
            
            servo.ChangeDutyCycle(duty_cycle)
            print("Motor is at orignal position")
            time.sleep(0.1)
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()


