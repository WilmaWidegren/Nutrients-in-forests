import functions as f
import numpy as np
import matplotlib.pyplot as plt

# x, y = f.get_tree_positions(100, 10)
# x = np.random.randint(1, 40)
# x = 23
factor = np.random.uniform(0.01, 0.05)
rate_parameter = -0.015
forest_size = f.grow_initial_forest(10, 40) 
forest_new_plot1 = [] 
forest_new_plot2 = [] 
forest_new_plot3 = [] 
forest_new_plot4 = [] 
time = 0
    # print('Initial:', forest)
carbon = f.initial_carbon_matrix(forest_size)
print(carbon)
while time < 10:
    if time == 0:
        pass
    else:
        for i in range(len(forest_size)):
        
            size = f.calculate_tree_growth(forest_size[i], 40, 0.01, rate_parameter, 1.2, carbon[i])
            forest_size[i] += size
    
    
    time += 0.1
    carbon = f.calculate_max_carbon(forest_size, factor)

print('After growth', forest_size)
# print(forest_new_plot)

plt.plot(forest_new_plot1, label = 'färg')
plt.plot(forest_new_plot2, label = 'färg')
plt.plot(forest_new_plot3, label = 'färg')
plt.plot(forest_new_plot4, label = 'färg')
plt.xlim([0,100])
plt.legend()
plt.show()