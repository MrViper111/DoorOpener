import RPi.GPIO as GPIO

class Control:

    IN1 = 11
    IN2 = 8
    ENA = 25  # Motor enable pin
    RLED = 3
    GLED = 4
    BLED = 14

    pwm_R = None
    pwm_G = None
    pwm_B = None

    battery_supply = 100

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

        # Control.close()

    @staticmethod
    def setRGB(RV, GV, BV):
        duty_R = (255 - RV) / 255 * 100
        duty_G = (255 - GV) / 255 * 100
        duty_B = (255 - BV) / 255 * 100

        Control.pwm_R.ChangeDutyCycle(duty_R)
        Control.pwm_G.ChangeDutyCycle(duty_G)
        Control.pwm_B.ChangeDutyCycle(duty_B)

    @staticmethod
    def close():
        Control.setRGB(255, 0, 0)
        GPIO.output(Control.ENA, GPIO.HIGH)
        GPIO.output(Control.IN1, GPIO.HIGH)
        GPIO.output(Control.IN2, GPIO.LOW)

    @staticmethod
    def open():
        Control.setRGB(0, 255, 0)
        GPIO.output(Control.ENA, GPIO.HIGH)
        GPIO.output(Control.IN1, GPIO.LOW)
        GPIO.output(Control.IN2, GPIO.HIGH)

    @staticmethod
    def clean():
        if Control.pwm_R: Control.pwm_R.stop()
        if Control.pwm_G: Control.pwm_G.stop()
        if Control.pwm_B: Control.pwm_B.stop()

        GPIO.cleanup()
