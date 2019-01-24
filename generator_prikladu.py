import operator
import random
​
x = random.randint(1, 10)
y = random.randint(1, 10)
​
operace = random.choice([{"znak": "-", "funkce": operator.sub}, 
                         {"znak": "+", "funkce": operator.add}])
​
if operace["znak"] == "-" and y > x:
    x, y = y, x
​
zadani = f"{x} {operace['znak']} {y} = "
reseni = operace["funkce"](x, y)