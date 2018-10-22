import numpy as np
import matplotlib.pylab as plot
import math as m
import sys

num = int(input('How many projectile you want to create? >> '))+1 # Create how many graph

for i in range(1,num):
    
    v = int(input('Enter the no {} initial velocity (m/s) >> '.format(i))) # Input vector
    g = 9.8
    angle = m.radians(int(input('Enter the no {} angle of projection (degrees) >> '.format(i)))) # Input degree

    t = ((2*v)*np.sin(angle))/g   # Formula to find time
    ts = t*np.linspace(0,1)  # Time vector

    x = (v*ts)*np.cos(angle)  # Formula to find the x position
    y = (v*ts)*np.sin(angle) - (g/2)*(ts**2)  # Formula to find y position

    plot.plot(x,y,label='Projectile no {}'.format(i)) # Create line graph with label

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

##### References #####
# https://newcontent.binus.ac.id/data_content/lecturer_shared_materials/main_material/IS1/201810150749390860002405_Data%20Visualization.pdf
# projectile motion formula
# and also pasha for finding the formula
