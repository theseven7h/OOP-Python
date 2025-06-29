class Bike:
    def __init__(self):
        self.is_on = False
        self.speed = 0
        self.gear = 1

    def toggle_power(self):
        self.is_on = not self.is_on

    def check_bike_is_on(self):
        return self.is_on

    def get_current_speed(self):
        return self.speed

    def accelerate(self, gear):
        self.speed += gear

    def decelerate(self, gear):
        self.speed -= gear

    def get_current_gear(self):
        speed_exceeds_40 = self.speed > 40
        speed_exceeds_30 = self.speed > 30
        speed_exceeds_20 = self.speed > 20

        if speed_exceeds_40: self.gear = 4
        elif speed_exceeds_30: self.gear = 3
        elif speed_exceeds_20: self.gear = 2
        else: self.gear = 1

        return self.gear