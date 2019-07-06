# ch 9
# # Class
# 9.1
# class Dog():
#     """A simple test on creation of dog."""
#     def __init__(self, name, age):
#         """Initial name and age."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate sitting of dog."""
#         print(self.name.title() + " is now sitting.")

#     def roll_over(self):
#         """Simulate roll over of dog."""
#         print(self.name.title() + " rolled over!")

# if __name__ == "__main__":
#     my_dog = Dog('willie', 6)
#     your_dog = Dog('lucy', 3)

#     print(f"My dog's name is {my_dog.name.title()}.")
#     print(f"My dog is {my_dog.age} year old.")
#     my_dog.sit()
#     my_dog.roll_over()

#     print(f"Your dog's name is {your_dog.name.title()}.")
#     print(f"Your dog is {your_dog.age} year old.")
#     your_dog.sit()

"""9-1 餐馆：创建一个名为Restaurant的类，其方法__init__()设置两个属性：restaurant_name和cuisine_type。创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。

9-2 三家餐馆：根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant()。

9-3 用户：创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性。在类User中定义一个名为describe_user()的方法，它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。"""

# Exercise 9-1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Initial of a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} has {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now opening.")

if __name__ == "__main__":
    restaurant = Restaurant('Bar Bar Restuarant', 'menu')
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    # Exercise 9-2
    mac = Restaurant('Macdonla', 'burger')
    kfc = Restaurant('KFC', 'chicken')
    mac.describe_restaurant()
    kfc.describe_restaurant()

# Exercise 9-3
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Greeting! {self.first_name} {self.last_name}")

if __name__ == "__main__":
    ann = User('Ann', 'Lee')
    ann.describe_user()
    ann.greet_user()

# 9.2
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


if __name__ == "__main__":
    my_new_car = Car('audi', 'a4', 2016)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()

# 可以以三种不同的方式修改属性的值：直接通过实例进行修改；通过方法进行设置；通过方法进行递增（增加特定的值）。下面依次介绍这些方法。
    # 直接通过实例进行修改
    my_new_car.odometer_reading = 233
    my_new_car.read_odometer()

    # 通过方法进行设置；
    my_new_car.update_odometer(235)
    my_new_car.update_odometer(32)
    my_new_car.read_odometer()

    # 通过方法进行递增（增加特定的值）
    my_new_car.increment_odometer(200)
    my_new_car.increment_odometer(200)
    my_new_car.increment_odometer(-50)
    my_new_car.read_odometer()


"""9-4 就餐人数：在为完成练习9-1而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。

添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。

添加一个名为increment_number_served()的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

9-5 尝试登录次数：在为完成练习9-3而编写的User类中，添加一个名为login_attempts 的属性。编写一个名为increment_login_attempts()的方法，它将属性login_attempts的值加1。再编写一个名为reset_login_attempts()的方法，它将属性login_attempts的值重置为0。

根据User类创建一个实例，再调用方法increment_login_attempts()多次。打印属性login_attempts的值，确认它被正确地递增；然后，调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重置为0。"""

# Exercise 9-4
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Init of a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} has {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now opening.")

if __name__ == "__main__":
    restaurant = Restaurant('Bar Bar Restuarant', 'menu')
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    # Exercise 9-2
    mac = Restaurant('Macdonla', 'burger')
    kfc = Restaurant('KFC', 'chicken')
    mac.describe_restaurant()
    kfc.describe_restaurant()

# Exercise 9-5
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Greeting! {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset user's login_attempts to 0."""
        self.login_attempts = 0

if __name__ == "__main__":
    ann = User('Ann', 'Lee')
    ann.describe_user()
    ann.greet_user()
    ann.increment_login_attempts()
    ann.increment_login_attempts()
    ann.increment_login_attempts()
    print(f"{ann.first_name} has logged in {ann.login_attempts} times.")
    ann.reset_login_attempts()
    print(f"{ann.first_name} has logged in {ann.login_attempts} times.")



# 9.3　继承
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

if __name__ == "__main__":
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()
    # print(type(my_tesla))
    # print(dir(my_tesla))
    # help(my_tesla)
    my_tesla.fill_gas_tank()
    my_tesla.get_range()

"""9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它继承你为完成练习9-1或练习9-4而编写的Restaurant类。这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。添加一个名为flavors的属性，用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个IceCreamStand实例，并调用这个方法。

9-7 管理员：管理员是一种特殊的用户。编写一个名为Admin的类，让它继承你为完成练习9-3或练习9-5而编写的User类。添加一个名为privileges的属性，用于存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin实例，并调用这个方法。

9-8 权限：编写一个名为Privileges的类，它只有一个属性——privileges，其中存储了练习9-7所说的字符串列表。将方法show_privileges()移到这个类中。在Admin类中，将一个Privileges实例用作其属性。创建一个Admin实例，并使用方法show_privileges()来显示其权限。

9-9 电瓶升级：在本节最后一个 electric_car.py 版本中，给Battery类添加一个名为upgrade_battery()的方法。这个方法检查电瓶容量，如果它不是85，就将它设置为85。创建一辆电瓶容量为默认值的电动汽车，调用方法get_range()，然后对电瓶进行升级，并再次调用get_range()。你会看到这辆汽车的续航里程增加了。"""

# Exercise 9-6
class IceCreamStand(Restaurant):
    """IceCreamStand is a type of Restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initial of IceCreamStand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Chocolate', 'Vanilla', 'Mango', 'Strawberry']
    
    def show_flavors(self):
        """Display falvors the ice-cream shop offer."""
        return self.flavors

if __name__ == "__main__":
    ice_cream_shop = IceCreamStand('Ice for you', 'menu')
    show_ice = ice_cream_shop.show_flavors() # Here Python's function is an object, so we can store it in a variable
    print(f"{show_ice}")

# Exercise 9-7
class Admin(User):
    """Admin is a super user."""
    def __init__(self, first_name, last_name):
        """Initial of an admin."""
        super().__init__(first_name, last_name)
        # self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges()

    # Codes below moved to Exercise 9-8.
    # def show_privileges(self):
    #     """Show privileges of an admin."""
    #     print(f"Privileges of {self.first_name} {self.last_name}: ")
    #     for right in self.privileges:
    #         print(f" - {right}")

# if __name__ == "__main__":
#     admin = Admin("John", "Wick")
#     admin.show_privileges()

# Exercise 9-8
class Privileges():
    """A class that holds privileges."""
    def __init__(self):
        """Initial of Privileges."""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Show privileges of an admin."""
        print(f"Privileges of mine: ")
        for right in self.privileges:
            print(f" - {right}")

if __name__ == "__main__":
    admin = Admin("John", "Wick")
    admin.privileges.show_privileges()

# Exercise 9-9
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

if __name__ == "__main__":
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()
    # print(type(my_tesla))
    # print(dir(my_tesla))
    # help(my_tesla)
    my_tesla.fill_gas_tank()
    my_tesla.get_range()
    my_tesla.battery.upgrade_battery()
    my_tesla.get_range()

# Exercise 9-13

# Exercise 9-14
# from random import randint
# class Die():
#     """A simulation of a dice."""
#     def __init__(self, side=6):
#         """Initial a die with sides."""
#         self.side = side

#     def roll_die(self) -> int:
#         """Roll a die, and return a result in int."""
#         return randint(1, self.side)

# if __name__ == "__main__":
#     # Testing Die class
#     die1 = Die() # a die with 6 sides.
#     print(f"Test of die: {die1.roll_die()}")

#     # As we are going to roll a die 10 times, let's create a function to do it!
#     def roll_10_times(die) -> list:
#         """Given a die and return 10 times results in list."""
#         results = []
#         for i in range(10):
#             result = die.roll_die()
#             results.append(result)
#         return results

#     # Create Dies in different sides.
#     die6 = Die(6)
#     die10 = Die(10)
#     die20 = Die(20)

#     # Roll the Dies!
#     ## Test client
#     result_6 = roll_10_times(die6)
#     print(f"The result of a {die6.side} side die: {result_6}")
#     ## Roll the Dice!
#     dice = [die6, die10, die20] # put dice in a list in order to for loop
#     for die in dice:
#         rolling_result = roll_10_times(die)
#         print(f"The result of a {die.side} side die: {rolling_result}")

