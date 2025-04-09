import RPi.GPIO as GPIO
import time

from api.website.views import verify_door_opened


class Control:

    IN1 = 10
    IN2 = 9
    ENA = 25
    BTN = 11
    LED = 26

    battery_supply = 100

    # Setup GPIO
    @staticmethod
    def setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Control.IN1, GPIO.OUT)
        GPIO.setup(Control.IN2, GPIO.OUT)
        GPIO.setup(Control.ENA, GPIO.OUT)
        GPIO.setup(Control.LED, GPIO.OUT)
        GPIO.setup(Control.BTN, GPIO.IN)

        if Control.verified_open():
            print("it was already open")
            GPIO.output(Control.LED, GPIO.HIGH)

    @staticmethod
    def close():
        GPIO.output(Control.LED, GPIO.LOW)

        GPIO.output(Control.ENA, GPIO.HIGH)
        GPIO.output(Control.IN1, GPIO.HIGH)
        GPIO.output(Control.IN2, GPIO.LOW)

    @staticmethod
    def open():
        GPIO.output(Control.ENA, GPIO.HIGH)
        GPIO.output(Control.IN1, GPIO.LOW)
        GPIO.output(Control.IN2, GPIO.HIGH)

        if Control.verified_open():
            GPIO.output(Control.LED, GPIO.HIGH)

    @staticmethod
    def verified_open():
        return GPIO.input(Control.BTN) == GPIO.HIGH

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
    if Control.verified_open():
        print("the door is indeed open")
    time.sleep(15)

    print("closing door...")
    Control.close()
    print("door closed")