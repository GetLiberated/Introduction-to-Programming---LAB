import numpy as np
import matplotlib.pylab as plot
import math as m
import sys

v = [0]
angle = [0]
t = [0]
ts = [0]
x = [0]
y = [0]

num = int(input('How many projectile you want to create? >> '))+1 # Create how many graph

for i in range(1,num):
    
    vi = int(input('Enter the no {} initial velocity (m/s) >> '.format(i))) # Input vector
    v.append(vi)
    g = 9.8
    anglei = m.radians(int(input('Enter the no {} angle of projection (degrees) >> '.format(i)))) # Input degree
    angle.append(anglei)

    ti = ((2*v[i])*np.sin(angle[i]))/g   # Formula to find time
    t.append(ti)
    tsi = t[i]*np.linspace(0,1)  # Time vector
    ts.append(tsi)

    xi = (v[i]*ts[i])*np.cos(angle[i])  # Formula to find the x position
    yi = (v[i]*ts[i])*np.sin(angle[i]) - (g/2)*(ts[i]**2)  # Formula to find y position
    x.append(xi)
    y.append(yi)

    plot.plot(x[i],y[i],label='Projectile no {}'.format(i)) # Create line graph with label

plot.title('Projection motion of a ball') # Graph title
plot.xlabel('x-coordinate') # Graph x label title
plot.ylabel('y-coordinate') # Graph y label title
plot.legend() # Print legend

ask = input('Do you want to save your graph? [Y/N] >> ').upper()
if ask == 'Y':
    plot.savefig('graph.png', bbox_inches='tight') # Save graph
    print('done.')
elif ask == 'N':
    m.pi

plot.show() # Print graph
sys.exit()
