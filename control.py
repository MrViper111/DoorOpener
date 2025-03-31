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
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(RLED, GPIO.OUT)
    GPIO.setup(GLED, GPIO.OUT)
    GPIO.setup(BLED, GPIO.OUT)

    # Initialize PWM for LED pins (frequency set to 1000Hz)
    pwm_R = GPIO.PWM(RLED, 1000)
    pwm_G = GPIO.PWM(GLED, 1000)
    pwm_B = GPIO.PWM(BLED, 1000)
    pwm_R.start(0)
    pwm_G.start(0)
    pwm_B.start(0)

    @staticmethod
    def setRGB(RV, GV, BV):
        """
        Set the RGB LED color.
        RV, GV, BV range from 0 to 255.
        """
        duty_R = RV / 255 * 100
        duty_G = GV / 255 * 100
        duty_B = BV / 255 * 100
        pwm_R.ChangeDutyCycle(duty_R)
        pwm_G.ChangeDutyCycle(duty_G)
        pwm_B.ChangeDutyCycle(duty_B)

    @staticmethod
    def close():
        """
        Close operation:
        - Enable motor (set to full power).
        - Set IN1 HIGH and IN2 LOW.
        - Display blue color (0,0,255) for "working but not open".
        - Delay for 10 seconds.
        """
        GPIO.output(ENA, GPIO.HIGH)
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
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
        GPIO.output(ENA, GPIO.HIGH)
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        time.sleep(1)
        Control.setRGB(0, 255, 0)
        time.sleep(10)

    try:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        pwm_R.stop()
        pwm_G.stop()
        pwm_B.stop()
        GPIO.cleanup()

while True:
    Control.open()
    time.sleep(5)
    Control.close()
