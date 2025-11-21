

import tkinter as tk

# Globals
root = tk.Tk()
canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

started = False
polyline: list[int] = []
polylines: list[list[int]] = []
line_ids: list[int] = []

def left_click(e):
    global started
    started = True
    
    polyline.extend([e.x, e.y])
    line_id = canvas.create_line(e.x, e.y, e.x, e.y)
    line_ids.append(line_id)

def right_click(e):
    global started
    started = False 

    polyline.extend([e.x, e.y])
    polylines.append(list(polyline))
    polyline.clear()
    line_ids.clear()

    print(polylines)

def on_mouse_move(event):
    if started:
        print(f"Mouse moved to: x={event.x}, y={event.y}")
 
        # Change the coordinates of the last created line to the new coordinates
        canvas.coords(line_ids[-1], polyline[-2], polyline[-1], event.x, event.y)
        
def on_undo(event):
    global started
    
    if len(line_ids) > 0:
        canvas.delete(line_ids.pop())
        polyline.pop()
        polyline.pop()
        if len(line_ids) == 0:
            started=False

canvas.bind("<ButtonPress-1>", left_click)
canvas.bind("<ButtonPress-3>", right_click)
canvas.bind("<Motion>", on_mouse_move)
root.bind("u", on_undo) 

root.mainloop()
