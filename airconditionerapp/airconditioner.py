
class AirConditioner:
    DEFAULT_TEMPERATURE = 24
    MAX_TEMPERATURE = 30
    MIN_TEMPERATURE = 16

    def __init__(self):
        self.ac_is_on = False
        self.temperature = self.DEFAULT_TEMPERATURE

    def check_ac_is_on(self):
        return self.ac_is_on

    def toggle_power(self):
        self.ac_is_on = not self.ac_is_on

    def get_temperature(self):
        return self.temperature

    def increase_temperature(self, increment):
        if self.temperature + increment < self.MAX_TEMPERATURE:
            self.temperature += increment
        else:
            self.temperature = self.MAX_TEMPERATURE

    def decrease_temperature(self, decrement):
        if self.temperature - decrement > self.MIN_TEMPERATURE:
            self.temperature -= decrement
        else:
            self.temperature = self.MIN_TEMPERATURE

