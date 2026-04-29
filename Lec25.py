'''
import numpy as np

# a = np.linspace(0,10,10)
# print(a)

# b = np.arange(0,10,2)
# print(b)

c = np.random.rand(3)
# randomly chooses real numbers between 0 and 1
print(c)

d = np.random.uniform(-1,1,5)
# randomly chooses real numbers between -1 and 1
print(d)

e = np.random.randint(1,9)
# randomly chooses integers between 1 and 9
print(e)
'''

'''
import matplotlib.pyplot as plt

# from matplotlib import pyplot as plt

import numpy as np
# x = np.array([x for x in range(0,6)])
x = np.linspace(0,2,100)
# print(x)
y = x**2
y1 = x**3
y2 = x
# print(y)

fig,ax = plt.subplots(figsize = (10,8),layout = 'constrained')
ax.plot(x,y,label = "y = x ^ 2 ")
ax.plot(x,y1,label = " y = x ^ 3")
ax.plot(x,y2,label = "y = x ")
ax.set_xlabel("x values") # x label
ax.set_ylabel("y values") # y label
ax.set_title("y = x^2 and y = x^3") # adding title to the graph
ax.grid()
ax.legend()
plt.show()
'''

'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,3,5,7,9])
y = np.array([2,5,6,9,1])

fig,ax = plt.subplots(figsize = (5,10) , layout = "constrained")
ax.scatter(x,y,label = "point values")
ax.plot(x,y)
ax.set_xlabel("x values")
ax.set_ylabel("y values")
ax.set_title("scatter diagram")
ax.grid()
ax.legend()
plt.show()
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(-1,1,10)
y = np.random.uniform(-1,1,10)

fig,ax = plt.subplots(figsize = (10,5),layout = "constrained")
ax.scatter(x,y,label = "scatter graph")
ax.plot(x,y)
ax.set_xlabel("x values")
ax.set_ylabel("y values")
ax.set_title("scatter graph of x and y on uniform distribution")
ax.grid()
ax.legend()
plt.show()