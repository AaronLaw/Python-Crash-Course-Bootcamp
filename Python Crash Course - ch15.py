# ch 15

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

# Load a numpy record array from yahoo csv data with fields date, open, close,
# volume, adj_close from the mpl-data/example directory. The record array
# stores the date as an np.datetime64 with a day unit ('D') in the date column.
with cbook.get_sample_data('goog.npz') as datafile:
    price_data = np.load(datafile)['price_data'].view(np.recarray)
price_data = price_data[-250:]  # get the most recent 250 trading days

delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# Marker size in units of points^2
volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2
close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]

fig, ax = plt.subplots()
ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volume and percent change')

ax.grid(True)
fig.tight_layout()

plt.show()

# 15.2.1　修改标签文字和线条粗细
# mpl_squares.py
import matplotlib.pyplot as plt

input_values = [1,2,3,4,5] # To correct the x axis
squares = [1,4,9,16,25]
plt.plot(input_values, squares, linewidth=5)

# Set chart title, and label the axis
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.show()
# 15.2.3　使用 scatter() 绘制散点图并设置其样式
# scatter_squares.py
import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)

# Set the title of graph and label it
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the size of marker
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

# 15.2.4　使用 scatter() 绘制一系列点
import matplotlib.pyplot as plt

# x_values = [x for x in range(1, 6)]
x_values = list(range(1, 1001))
# y_values = [x * x for x in range(1, 6)]
y_values = [x * x for x in x_values]

plt.scatter(x_values, y_values, s=100)

# Set the title of graph and label it
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=24)

# Set the size of marker
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()


# random_walk.py
from random import choice

class RandomWalk():
    """A class that generate random walk."""

    def __init__(self, num_points=5000):
        """Initial properties of random walk."""
        self.num_points = num_points

        # Every random walk starts at point (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points for random walk."""

        # Randomly walks until reach the defined length.
        while len(self.x_values) < self.num_points:

            # Determent the direction and distance
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject not moving
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values
            next_x = self.x_values[-1] + x_step 
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

# rw_visual.py
import matplotlib.pyplot as plt

# from random_walk import RandomWalk

while True:
    # Create a RandomWalk instance, and draw all the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of window
    plt.figure(figsize=(10, 6))
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, 
            c=point_numbers, cmap=plt.cm.Blues, 
            edgecolor='none', s=1)
    # Emphases start point and end point.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    

    # Hide the axis
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break


# Exercise 15-3
# rw_visual.py
# 分子运动：修改 rw_visual.py，将其中的plt.scatter()替换为plt.plot()。为模拟花粉在水滴表面的运动路径
import matplotlib.pyplot as plt

# from random_walk import RandomWalk

while True:
    # Create a RandomWalk instance, and draw all the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of window
    plt.figure(figsize=(10, 6))
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, 
            c=point_numbers, cmap=plt.cm.Blues, 
            edgecolor='none', s=1)
    # Emphases start point and end point.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    

    # Hide the axis
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break



# Exercise 15-5
# random_walk.py
# Here we refactor fill_walk()
from random import choice

class RandomWalk():
    """A class that generate random walk."""

    def __init__(self, num_points=5000):
        """Initial properties of random walk."""
        self.num_points = num_points

        # Every random walk starts at point (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points for random walk."""

        # Randomly walks until reach the defined length.
        while len(self.x_values) < self.num_points:

            # Determent the direction and distance
            distance_range = 8
            x_step = self.get_step(distance_range=8)
            y_step = self.get_step(distance_range=8)
            # x_step = self.get_step()
            # y_step = self.get_step()

            # Reject not moving
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values
            (next_x, next_y) = self.get_next_step(x_step, y_step)
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self, distance_range: int=4):
        """Determent the direction and distance.
        Return a positive / negative integer within distance_range."""
        direction = choice([1, -1])
        distance = choice([x for x in range(1, distance_range)])
        step = direction * distance
        return step

    def get_next_step(self, x_step, y_step):
        """Calculate the next x and y values.
        Return a tuple represents (next_x, next_y)."""
        next_x = self.x_values[-1] + x_step 
        next_y = self.y_values[-1] + y_step
        return (next_x, next_y)


# 15.4　使用 Pygal 模拟掷骰子
# Exercise 9-14
# I borrow the Die class from Exercise 9-14
from random import randint

class Die():
    """A simulation of a dice."""
    def __init__(self, side=6):
        """Initial a die with sides."""
        self.side = side

    # def roll_die(self) -> int:
    def roll_die(self):
        """Roll a die, and return a result in int."""
        return randint(1, self.side)


# die_visual.py
# from die import Die

# import pygal

# num_rolling = 1000
# # Create a D6
# d6 = Die()

# # Roll the die, and save results in a list.
# results = []
# results = [d6.roll_die() for roll_num in range(num_rolling)]
# # print(results)

# # Analysis the results
# frequencies = [results.count(value) for value in range(1, d6.side+1)]
# print(frequencies)

# # Visualize the results
# hist = pygal.Bar()

# hist.title = f"Results of rolling one D6 {num_rolling} times."
# hist.x_lables = [x for x in range(1, d6.side)]
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"

# hist.add('D6', frequencies)
# hist.render_to_file('results/die_visual.svg')


# 15.4.7　同时掷两个骰子 -> Aaron's Style: more abstract
    # -> buggy
# dice_visual.py
# from die import Die

import pygal

num_rolling = 1000
num_dice = 2
# Create D6
dice = [Die() for die in range(num_dice)] # We create Die objects according num_dice.

# Roll the die, and save results in a list.
# results = [d6.roll_die() for roll_num in range(num_rolling)] # For ...
results = [die.roll_die() for i in range(num_rolling) for die in dice]
print(results)

# Analysis the results
# frequencies = [results.count(value) for value in range(1, d6.side+1)] # For old old 1 dice case.
min_value = 1 * num_dice
max_value = sum([die.side for die in dice]) # Sum up the most large side in each die.
frequencies = [results.count(value) for value in range(min_value, max_value+2)]
print(frequencies)

# Visualize the results
hist = pygal.Bar()

hist.title = f"Results of rolling one D6 {num_rolling} times."
hist.x_lables = [x for x in range(1, dice[0].side)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('results/dice_visual.svg')

# 15.4.8
# differen_dice.py
# from die import Die

import pygal

# from die import Die

num_rolling = 500000
# 创建一个 D6 和一个 D10
die_1 = Die()
die_2 = Die(10)

# 掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(num_rolling):
    result = die_1.roll_die() + die_2.roll_die()
    results.append(result)
print(results)

# 分析结果
frequencies = []
max_result = die_1.side + die_2.side
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 可视化结果
hist = pygal.Bar()

hist.title = f"Results of rolling D6 and D10 dice {num_rolling} times."
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_labels = [side for side in range(2, (die_1.side + die_2.side)+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('results/dice_visual.svg')

