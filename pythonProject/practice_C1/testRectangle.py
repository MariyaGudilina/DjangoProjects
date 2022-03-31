
from rectangle import Rectangle
r1 = Rectangle(10, 5)

print("r1.width =", r1.width)
print("r1.height =", r1.height)
print("r1.get_width =", r1.get_width())
print("r1.get_height =", r1.get_height())
print("r1.get_area =", r1.get_area())

r1 = Rectangle(2, 4)

from rectangle import Cat
cat_1 = Cat("Baron", "boy", 2)
cat_2 = Cat("Sam", "boy", 2)

print(cat_1.get_name(), cat_1.get_gender(), cat_1.get_age())
print(cat_2.get_name(), cat_2.get_gender(), cat_2.get_age())

from rectangle import Dog

dog_1=Dog("Felix", "boy", 2)
print(dog_1.get_pet())
