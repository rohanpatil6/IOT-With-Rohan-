from gpiozero import LED
import time
R=LED(16)
Y=LED(17)
G=LED(18)
while(1) :
 R.on()
 time.sleep(1)
 R.off()
 Y.on()
 time.sleep(2)
 Y.off()
 G.on()
 time.sleep(3)
 G.off()
 