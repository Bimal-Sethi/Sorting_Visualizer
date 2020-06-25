from tkinter import *
from tkinter import ttk
import random
from bubble_sort import bubble_sort

### Making a window for the app ###
root = Tk()
root.title("Sorting Algorithm Visualisation")
root.maxsize(height=540, width=810)
root.config(bg='black')

### Partioning the window in UI and Canvas ###
UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=5, pady=5)

canvas_width = 796
canvas_height = 380
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.grid(row=1, column=0, padx=5, pady=5)

### varibales and functions ###
selected_algo = StringVar()
data = []

def draw(data, color):
    canvas.delete("all")
    spacing = 10
    offset = 20
    c_width = canvas_width - 2*offset
    c_height = canvas_height - 2*offset

    x_width = (c_width - (len(data)-1)*spacing)/len(data)
    modified = [i + 0.5 - min(data) for i in data]
    normalized_data = [i / max(modified) for i in modified]

    for i, j in enumerate(normalized_data):
        x0 = offset + i*(x_width+spacing)
        y0 = 0
        x1 = offset + i*(x_width+spacing) + x_width
        y1 = j*c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
        canvas.create_text(x0+1, y1+2, anchor=NW, text=str(data[i]))

    root.update_idletasks()

def Generate():
    global data
    Min = int(minScale.get())
    Max = int(maxScale.get())
    Size = int(sizeScale.get())
    if(Min > Max): Min, Max = Max, Min
    data = []
    for _ in range (Size) :
        data.append(random.randrange(Min, Max+1))
    draw(data, ['orange' for i in range(len(data))])

def startAlgo():
    global data
    bubble_sort(data, draw, 0.25/speedScale.get())

### User Interface Area ###
Label(UI_frame, text="Sort Using :", bg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_algo, values=['Bubble Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=1, to=20, length=200, label="Select Speed", orient=HORIZONTAL, resolution=1)
speedScale.grid(row=0, column=2, padx=5, pady=5)
speedScale.set(20)

Button(UI_frame, text="Generate", command=Generate, bg='cyan').grid(row=0, column=3, padx=5, pady=5)
Button(UI_frame, text="Click here to Start Sorting!", command=startAlgo, bg='pink', width=38).grid(row=0, column=4, padx=5, pady=5)

sizeScale = Scale(UI_frame, from_=1, to=35, resolution=1, label="Select Size", orient=HORIZONTAL, length=212)
sizeScale.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

minScale = Scale(UI_frame, from_=-99, to=99, resolution=1, label="Min Value", orient=HORIZONTAL, length=268)
minScale.grid(row=1, column=2, padx=5, pady=5, columnspan=2)

maxScale = Scale(UI_frame, from_=-99, to=99, resolution=1, label="Max Value", orient=HORIZONTAL, length=268)
maxScale.grid(row=1, column=4, padx=5, pady=5, columnspan=1)

root.mainloop()
