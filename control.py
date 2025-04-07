import time

import RPi.GPIO as GPIO

class Control:
    IN1 = 10
    IN2 = 9
    ENA = 25  # Motor enable pin

    @staticmethod
    def setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(Control.IN1, GPIO.OUT)
        GPIO.setup(Control.IN2, GPIO.OUT)
        GPIO.setup(Control.ENA, GPIO.OUT)

    @staticmethod
    def close():
        GPIO.output(Control.ENA, GPIO.HIGH)
        GPIO.output(Control.IN1, GPIO.HIGH)
        GPIO.output(Control.IN2, GPIO.LOW)

    @staticmethod
    def open():
        GPIO.output(Control.ENA, GPIO.HIGH)
        GPIO.output(Control.IN1, GPIO.LOW)
        GPIO.output(Control.IN2, GPIO.HIGH)

if __name__ == "__main__":
    Control.setup()
    print("setup complete")
    time.sleep(3)

    print("opening...")
    Control.open()
    time.sleep(15)
    print("closing...")
    Control.close()
    time.sleep(15)