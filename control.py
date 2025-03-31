import RPi.GPIO as GPIO
import time

# Define GPIO pins (using BCM numbering)
class Control:

    IN1 = 17
    IN2 = 27
    ENA = 22  # Motor enable pin
    RLED = 5
    GLED = 6
    BLED = 13

    # Setup GPIO
    @staticmethod
    def setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Control.IN1, GPIO.OUT)
        GPIO.setup(Control.IN2, GPIO.OUT)
        GPIO.setup(Control.ENA, GPIO.OUT)
        GPIO.setup(Control.RLED, GPIO.OUT)
        GPIO.setup(Control.GLED, GPIO.OUT)
        GPIO.setup(Control.BLED, GPIO.OUT)

        Control.pwm_R = GPIO.PWM(Control.RLED, 1000)
        Control.pwm_G = GPIO.PWM(Control.GLED, 1000)
        Control.pwm_B = GPIO.PWM(Control.BLED, 1000)

        Control.pwm_R.start(0)
        Control.pwm_G.start(0)
        Control.pwm_B.start(0)

    @staticmethod
    def setRGB(RV, GV, BV):
        """
        Set the RGB LED color.
        RV, GV, BV range from 0 to 255.
        """
        duty_R = RV / 255 * 100
        duty_G = GV / 255 * 100
        duty_B = BV / 255 * 100
        Control.pwm_R.ChangeDutyCycle(duty_R)
        Control.pwm_G.ChangeDutyCycle(duty_G)
        Control.pwm_B.ChangeDutyCycle(duty_B)

    @staticmethod
    def close():
        """
        Close operation:
        - Enable motor (set to full power).
        - Set IN1 HIGH and IN2 LOW.
        - Display blue color (0,0,255) for "working but not open".
        - Delay for 10 seconds.
        """
        GPIO.output(Control.ENA, GPIO.HIGH)
        GPIO.output(Control.IN1, GPIO.HIGH)
        GPIO.output(Control.IN2, GPIO.LOW)
        Control.setRGB(0, 0, 255)
        time.sleep(10)

    @staticmethod
    def open():
        """
        Open operation:
        - Display yellow (255,255,0) while starting.
        - Reverse motor direction: set IN1 LOW and IN2 HIGH.
        - After 1 second, change LED to green (0,255,0) to indicate "open".
        - Delay for 10 seconds.
        """
        Control.setRGB(255, 255, 0)
        GPIO.output(Control.ENA, GPIO.HIGH)
        GPIO.output(Control.IN1, GPIO.LOW)
        GPIO.output(Control.IN2, GPIO.HIGH)
        time.sleep(1)
        Control.setRGB(0, 255, 0)
        time.sleep(10)

def main():
    Control.setup()

    try:
        while True:
            print("hi")
            Control.open()
            time.sleep(5)

            Control.close()
    except KeyboardInterrupt:
        pass
    finally:
        Control.pwm_R.stop()
        Control.pwm_G.stop()
        Control.pwm_B.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    main()
