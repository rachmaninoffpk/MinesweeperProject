import tkinter as tk 

root = tk.Tk()

frame = tk.LabelFrame(root)
frame.pack(padx=50, pady=50)

canvas = tk.Canvas(frame, height=400, width=400)
canvas.pack()


#Figure out how to access location of mouse
'''
mouse = tk.Event()
print(mouse.x, mouse.y)
'''

colors = ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']

for i in range(20):
    for j in range(20):
        text = '{},{}'.format(i,j)
        canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill=colors[(i+j)%len(colors)])

root.mainloop()