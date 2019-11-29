#importar bibliotecas
import RPi.GPIO as GPIO
from time import sleep

#led inicia apagado
#o botão da porta 24 aumenta a intensidade luminosa do LED
#o botão da porta 25 diminui a intensidade luminosa do LED
x=0
GPIO.setmode(GPIO.BCM)
#porta 21:led verde
GPIO.setup(21,GPIO.OUT) 
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_UP) 
sleep (0.1)

print("GPIO%d = %d" % (24, GPIO.input(24)))

p = GPIO.PWM(21,100)
p.start(0)
while x>=90 & x>=0:
    p.ChangeDutyCycle(x)
    print("x ",x)
    if GPIO.input(24) == GPIO.HIGH:
            x=x+1
            sleep(0.5)
    if GPIO.input (25) == GPIO.LOW:
         x=x-1
         sleep(0.5)
    

GPIO.cleanup()