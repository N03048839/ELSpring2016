# This is a simple raspberry pi program, that
# causes an external LED to blink rapidly, alternating 
# between three and four times.
  
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

TIME_STEP_LONG = 3;
TIME_STEP_SHORT = 0.1;
LED_PIN = 17;

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def q():
   print("done!");
   GPIO.cleanup();

def blink():
   count = 0;
   while (True):
      for i in range (3, 4): 
         for j in range (0, i):
            count = count + 1; 
            print "blink #" + str(count);
            GPIO.output(LED_PIN, True);
            time.sleep(TIME_STEP_SHORT);
            GPIO.output(LED_PIN, False);
            time.sleep(TIME_STEP_SHORT);
         time.sleep(TIME_STEP_LONG); 

blink();
