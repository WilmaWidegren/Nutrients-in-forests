import time
from tkinter import *
import numpy as np
from numpy import random


tree_positions_x = random.rand(100)
tree_positions_y = random.rand(100)
tree_size = []
for i in range(100):
    tree_size.append(random.randint(0,100))

print(tree_size)

N_skip = 1  # Visualize status every N_skip steps. 
ra = 0.01  # Radius of the circle representing the agents.

window_size = 600

tk = Tk()
tk.geometry(f'{window_size + 20}x{window_size + 20}')
tk.configure(background='#000000')

canvas = Canvas(tk, background='#ECECEC')  # Generate animation window.
tk.attributes('-topmost', 0)
canvas.place(x=10, y=10, height=window_size, width=window_size)


step = 0

def stop_loop(event):
    global running
    running = False
tk.bind("<Escape>", stop_loop)  # Bind the Escape key to stop the loop.
running = True  # Flag to control the loop.
while running:


    for i in range(len(tree_size)):
        tree_size[i] += 1
    
    # Update animation frame.
    if step % N_skip == 0:   
        canvas.delete('all')
        agents = []


        for j in range(len(tree_positions_y)):
            center_x = tree_positions_x[j] * window_size
            center_y = tree_positions_y[j] * window_size
            current_radius = tree_size[j]
            
            # 2. NY LOGIK: Välj färg baserat på storlek
            if current_radius < 80:
                agent_color = '#ffd700'  # Guld (Liten)
            elif current_radius < 150:
                agent_color = '#ff8c00'  # Mörk Orange (Mellanstor)
            else:
                agent_color = '#cc0000'  # Röd (Stor)
            agents.append(
                canvas.create_oval(
                    (tree_positions_x[j]-ra) * window_size,
                    (tree_positions_y[j]-ra)   * window_size,
                    (tree_positions_x[j]+ra)  * window_size,
                    (tree_positions_y[j]+ra)  * window_size,
                    outline='', 
                    fill=agent_color,
                )
            )
        
        tk.title(f'Iteration {step}')
        tk.update_idletasks()
        tk.update()
        time.sleep(0.1)  # Increase to slow down the simulation.

    step += 1
    

tk.update_idletasks()
tk.update()
tk.mainloop()  # Release animation handle (close window to finish).
