from ast import main
import sys
import time
import RPi.GPIO as GPIO


class motorDriver:

    'controls a L298n motor controller'

    def __init__(self, enA, enB, in1, in2, in3, in4):

        'sets up pin assignment'
        GPIO.setmode(GPIO.BOARD)
        self.enA = enA
        self.enB = enB
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4

        'sets all pins to output and to zero'
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.enA,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)

        GPIO.setup(self.in3,GPIO.OUT)
        GPIO.setup(self.in4,GPIO.OUT)
        GPIO.setup(self.enB,GPIO.OUT)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)

        'set enA and enB to pwm'
        self.pA = GPIO.PWM(self.enA,1000)
        self.pB = GPIO.PWM(self.enB,1000)
        self.pA.start(25)
        self.pB.start(25)
        
    
        
    def forward(self, velSpeed):
        'goes foreward and given speed'

        speed = velSpeed*100

        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)

        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)

        self.pA.ChangeDutyCycle(speed)
        self.pB.ChangeDutyCycle(speed)
	
	time.sleep(.5)

    def backward(self, velSpeed):
        'goes backwards at given speed'

        speed = velSpeed*100

        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)

        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)

        self.pA.ChangeDutyCycle(speed)
        self.pB.ChangeDutyCycle(speed)

	time.sleep(.5)

    def right(self, velSpeed):
        'goes right at given speed'

        speed = velSpeed*100

        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)

        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)

        self.pA.ChangeDutyCycle(speed)
        self.pB.ChangeDutyCycle(speed)

	time.sleep(.5)

    def left(self, velSpeed):
        'goes left at given speed'

        speed = velSpeed*100

        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)

        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)

        self.pA.ChangeDutyCycle(speed)
        self.pB.ChangeDutyCycle(speed)

	time.sleep(.5)

def main():
    'test that motors are funtioncal with hard coded pin assignment'
    test = motorDriver(22, 7, 16, 18, 13, 11)

    test.forward(.75)
    time.sleep(3)
    test.backward(.75)
    time.sleep(3)
    test.left(.75)
    time.sleep(3)
    test.right(.75)
    time.sleep(3)


if __name__ == "__main__":
    main()

