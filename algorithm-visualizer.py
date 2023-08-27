# Sorting Algorithms Visualizer in Python
from tkinter import * #importing tkinter
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort 
from mergesort import merge_sort

#tkinter layout
tkinterRoot = Tk()
tkinterRoot.title('Sorting Algorithm Visualisation')
tkinterRoot.maxsize(900, 600)
tkinterRoot.config(bg='black')

#variables
selectedAlgorithm = StringVar()
data = []

#function
def drawData(data, colorArray):
    user_canvas.delete("all")
    canvasHeight = 380
    canvasWidth = 600
    x_width = canvasWidth / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = canvasHeight - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = canvasHeight

        user_canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        user_canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    tkinterRoot.update_idletasks()


def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['red' for x in range(len(data))]) #['red', 'red' ,....]

def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
    
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())
    
    drawData(data, ['green' for x in range(len(data))])


#frame / base lauout
user_frame = Frame(tkinterRoot, width= 600, height=200, bg='grey')
user_frame.grid(row=0, column=0, padx=10, pady=5)

user_canvas = Canvas(tkinterRoot, width=600, height=380, bg='white')
user_canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row[0]
Label(user_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(user_frame, textvariable=selectedAlgorithm, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(user_frame, from_=0.1, to=15.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(user_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(user_frame, from_=3, to=50, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(user_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Minimum Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(user_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Maximum Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(user_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

tkinterRoot.mainloop()