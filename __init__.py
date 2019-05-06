from mycroft import MycroftSkill, intent_file_handler
import RPi.GPIO as GPIO
import time


class RosGpioPins(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pins.gpio.ros.intent')
    def handle_pins_gpio_ros(self, message):
        self.speak_dialog('pins.gpio.ros')
        GPIO.setmode(GPIO.BOARD)
        green=11
        GPIO.setup(green,GPIO.OUT)
        GPIO.output(green,True)
        time.sleep(1)
        GPIO.output(green,False)
        time.sleep(1)
        GPIO.output(green,True)
        time.sleep(1)
        GPIO.output(green,False)
        GPIO.cleanup()


def create_skill():
    return RosGpioPins()

