import RPi.GPIO as GPIO
import time

class Control:

    IN1 = 11
    IN2 = 8
    ENA = 25  # Motor enable pin

    # Setup GPIO
    @staticmethod
    def setup():
        GPIO.setmode(GPIO.BCM)
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

    @staticmethod
    def clean():
        GPIO.cleanup()

if __name__ == "__main__":
    Control.setup()
    print("setup complete")
    time.sleep(3)

    print("opening door...")
    Control.open()
    print("door opened")
    time.sleep(15)

    print("closing door...")
    Control.close()
    print("door closed")