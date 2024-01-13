class Battery:
    def __init__(self):
        self.charge = 100

    def use(self,amount):
        if self.charge - amount < 0:
            self.charge = 0
        else:
            self.charge -= amount

    def get_charge(self):
        return self.charge