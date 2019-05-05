from mycroft import MycroftSkill, intent_file_handler


class RosGpioPins(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pins.gpio.ros.intent')
    def handle_pins_gpio_ros(self, message):
        self.speak_dialog('pins.gpio.ros')


def create_skill():
    return RosGpioPins()

