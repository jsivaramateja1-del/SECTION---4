from matplotlib import pyplot as plt
import numpy as np

n = int(input("Enter the number of iterations : "))

x = np.random.uniform(-1,1,n)
y = np.random.uniform(-1,1,n)
in_circle = x**2 + y**2 <= 1
cummulative_sum = np.cumsum(in_circle)
# print(cummulative_sum)
# print(in_circle)
total_number_points = np.arange(1,n+1)
pi_value = (4*cummulative_sum)/ total_number_points
fig,ax = plt.subplots(1,3,figsize = (12,6),layout = 'constrained') # 1,3 represents 3 subplots in a row
ax[0].plot(total_number_points,pi_value,label = "pi value")
ax[0].grid()
ax[0].axhline(np.pi,color = 'red')
ax[0].set_xlabel("Number of iterations")
ax[0].set_ylabel("pi values")
ax[0].legend()
ax[1].scatter(x[in_circle],y[in_circle],label = "points inside the circle",s = 0.1)
ax[1].scatter(x[~in_circle],y[~in_circle],label = "points outside the circle",s = 0.1)
circle = plt.Circle((0,0),1,fill = False)
ax[1].add_patch(circle)
print("approx.  value",pi_value[-1])
plt.show()
# print(pi_value)