#Method2
import random

lower ="abcdefghijklmnopqrstuvwxxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Number = "0123456789"
symbol ="!@#$%^&*()."


Pass_gen= lower + upper + Number + symbol
length = 12
Password = "".join(random.sample(Pass_gen, length ))

print("Your random Password is : ", Password)