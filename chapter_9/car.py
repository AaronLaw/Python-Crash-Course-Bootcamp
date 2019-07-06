"""A class that represents car."""

class Car():
    """A simple simulation of car."""
    
    def __init__(self, make, model, year):
        """Initial attributes of car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a simplely descriptive info of car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print an info about car's odometer."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Set odometer to mileage."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Increment miles to odometer."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        """Fill the gas tank of car."""
        print(f"The gas tank is filled.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initial of parent class."""
        super().__init__(make, model, year)
        # self.battery_size = 70
        self.battery = Battery()

    def get_battery(self):
        """Return the size of battery."""
        return self.battery.battery_size

    def describe_battery(self):
        """Print an info about battery."""
        # print(f"This car has a {self.battery.battery_size}-kWh battery.")
        self.battery.describe_battery()

    def fill_gas_tank(self):
        """Electric car has no gas tank."""
        print("This car doesn't need a gas tank!")

    def get_range(self):
        """Return the running range from battery."""
        self.battery.get_range()

class Battery():
    """A simulation of battery in car."""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print an info about battery."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a message to show how long it can run."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print(f"This car can go approximately {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery when it's < 85."""
        if self.battery_size < 85:
            self.battery_size = 85