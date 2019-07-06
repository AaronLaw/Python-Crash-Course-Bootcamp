import random
scores = []
max_value = 65
length = 36
for i in range(length):
    scores.append(random.randint(0, max_value))

print(scores)

    至数百万个元素的列表。

# 4.1　遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    # print(f"{magician.title()} , that was a great trick!")
    print("{}, that was a great trick".format(magician.title()))


# Margherita. Tomato sauce, mozzarella, and oregano.
# Marinara. Tomato sauce, garlic and basil.
# Quattro Stagioni. Tomato sauce, mozzarella, mushrooms, ham, artichokes, olives, and oregano.

# Exercise 4-1
pizzas = ['Margherita', 'Marinara', 'Quattro Stagioni']
for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("I really like pizza!")

# Exercise 4-2
pets = ['dog', 'cat', 'rabbit']
for pet in pets:
    print(f"A {pet} would make a great pet")
print("Any of these animals woul make a great pet!")

# Exercise extra
pizzas = {'Margherita': ['Tomato sauce', 'mozzarella', 'oregano'],
        'Marinara': ['Tomato sauce', 'garlic','basil'],
        'Quattro Stagioni': ['Tomato sauce', 'mozzarella', 'mushrooms', 'ham', 'artichokes', 'olives', 'oregano']}

for k, v in pizzas.items():
    print(k, v)

for k, v in pizzas.items():
    print(f"Pizza {k} is made of:")
    # for item in v:
    #     print(f"\t {item}")
    for i, v_ in enumerate(v):
        # print(i, v_)
        print(f"\t {i}. {v_}")

# 4.3　创建数值列表
squares = []
for value in range(1, 111):
    squares.append(value ** 2)
print(squares)
len(squares)

squares = [value ** 2 for value in range(1, 111)]
print(squares)

# Exercise
"""4-3 数到20：使用一个for循环打印数字1~20（含）。

4-4 一百万：创建一个列表，其中包含数字1~1000000，再使用一个for循环将这些数字打印出来（如果输出的时间太长，按 Ctrl+C 停止输出，或关闭输出窗口）。

4-5 计算1~1000000的总和：创建一个列表，其中包含数字1~1000000，再使用min()和max()核实该列表确实是从1开始，到1000000结束的。另外，对这个列表调用函数sum()，看看 Python 将一百万个数字相加需要多长时间。

4-6 奇数：通过给函数range()指定第三个参数来创建一个列表，其中包含1~20的奇数；再使用一个for循环将这些数字都打印出来。

4-7 3的倍数：创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for循环将这个列表中的数字都打印出来。

4-8 立方：将同一个数字乘三次称为立方。例如，在 Python 中，2的立方用2**3表示。请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for循环将这些立方数都打印出来。

4-9 立方解析：使用列表解析生成一个列表，其中包含前10个整数的立方。"""

# Exercise 4-3
for i in range(1, 21):
    print(i)
# Exercise 4-4
# digits = range(1, 1000000)
# [sum(digits) for i in range(1, 1000000)]

# Exercise 4-6
odd_numbers = list(range(1,21,2))
print(odd_numbers)

# Exercise 4-7
tri_numbers = list(range(3, 31, 3))
for num in tri_numbers:
    # Use divide operator 
    if num % 3 != 0:
        print(f"{num} cannot be divided by 3!")
    else:
        print(num)
    # Or use try...except block to handle
    try:
        if num % 3 == 0:
            print(num)
        else:
            raise ValueError
    except ValueError as e:
        print(f"Error: {num} cannot be divided by 3!")

# Exercise 4-8
cubes = [(x**3) for x in range(1, 11)]
print(cubes)

# Slice, same object or not?
a = [1, 2]
print(f"ID of a: {id(a)}")
a.reverse()
print(f"ID of a: {id(a)}")
b = a
print(f"ID of b: {id(b)}")
c = a[::]
print(f"ID of c: {id(c)}")
print(c) # Why c has a new address in each run?

# 找出從 1 到 30 內能被 3 和 整除之數
result = [x for x in range(30) if (x % 3 == 0) and (x % 2 == 0)]

for x in range(30):
    if x%3 == 0 and x%2 == 0:
        result.append(x)
print(result)

print(id(squares))
print(id(squares[:]))
a = squares[:]
a.append('het')
print(id(a))
print(id(squares))
print(squares)

"""4-13 自助餐：有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。
* 使用一个for循环将该餐馆提供的五种食品都打印出来。
* 尝试修改其中的一个元素，核实 Python 确实会拒绝你这样做。
* 餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块：给元组变量赋值，并使用一个for循环将新元组的每个元素都打印出来。
"""
# Exercise 4-13:
foods = ('Margherita', 'Marinara', 'Quattro Stagioni', 'Burgen', 'Rice')
print(f"We have these foods in menu:")
for food in foods:
    print(f"\t{food}")

try:
    foods[1] = 'rice'
except TypeError as e:
    print(f"An exception occurs: {e}, and you cannot change any element in a tuple.")
    print(f"And so, our menu is immutable.")

foods = ('Margherita', 'Marinara', 'Salmon soup', 'Burgen', 'Chocolate pie')
print(f"We have these foods in a menu renewed:")
for food in foods:
    print(f"\t{food}")