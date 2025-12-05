import tkinter as tk
from PIL import Image, ImageTk
import os

def wheel1_callback(color):
    print("Wheel 1:", color)
    os.system("python3 -m liquidctl --match \"NZXT RGB Controller F-Series\" set led3 color fixed {}".format(color[1:]))
    

def wheel2_callback(color):
    print("Wheel 2:", color)
    os.system("python3 -m liquidctl --match \"NZXT RGB Controller Kraken\" set led2 color fixed {}".format(color[1:]))

def wheel3_callback(color):
    print("Wheel 3:", color)
    os.system("python3 -m liquidctl --match \"NZXT RGB Controller Kraken\" set led1 color fixed {}".format(color[1:]))

def wheel4_callback(color):
    print("Wheel 4:", color)
    os.system("python3 -m liquidctl --match \"NZXT RGB Controller F-Series\" set led2 color fixed {}".format(color[1:]))

def wheel5_callback(color):
    print("Wheel 5:", color)
    os.system("python3 -m liquidctl --match \"NZXT RGB Controller F-Series\" set led1 color fixed {}".format(color[1:]))

def wheel6_callback(color):
    print("Wheel 6:", color)
    os.system("python3 -m liquidctl --match \"NZXT RGB Controller F-Series\" set led3 color fixed {}".format(color[1:]))
    os.system("python3 -m liquidctl --match \"NZXT RGB Controller Kraken\" set led2 color fixed {}".format(color[1:]))
    os.system("python3 -m liquidctl --match \"NZXT RGB Controller Kraken\" set led1 color fixed {}".format(color[1:]))
    os.system("python3 -m liquidctl --match \"NZXT RGB Controller F-Series\" set led2 color fixed {}".format(color[1:]))
    os.system("python3 -m liquidctl --match \"NZXT RGB Controller F-Series\" set led1 color fixed {}".format(color[1:]))

# ----------------------------
class ColorWheel:
    def __init__(self, master, image_path, callback, name):
        self.callback = callback
        self.selected_color = tk.StringVar()

        self.image = Image.open(image_path).convert("RGBA")
        self.width, self.height = self.image.size
        self.tk_image = ImageTk.PhotoImage(self.image)

        self.canvas = tk.Canvas(master, width=self.width, height=self.height)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        self.canvas.pack(padx=5, pady=5)
        self.canvas.bind("<Button-1>", self.pick_color)

        self.preview = tk.Label(master, text="Vorschau", bg="white", width=10, height=1)
        self.preview.pack(pady=(0,10))
        self.fan_name = tk.Label(master, text=name, bg="white", width=20, height=1)
        self.fan_name.pack()

    def pick_color(self, event):
        x, y = event.x, event.y
        if 0 <= x < self.width and 0 <= y < self.height:
            r, g, b, a = self.image.getpixel((x, y))
            if a > 0:
                hex_color = f"#{r:02x}{g:02x}{b:02x}"
                self.selected_color.set(hex_color)
                self.preview.config(bg=hex_color, text=hex_color)
                self.callback(hex_color)

root = tk.Tk()
root.title("6 Color Wheels - 3x3 Raster")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

images = ["colorwheel.png","colorwheel.png","colorwheel.png",
          "colorwheel.png","colorwheel.png","colorwheel.png"]

callbacks = [wheel1_callback, wheel2_callback, wheel3_callback,
             wheel4_callback, wheel5_callback, wheel6_callback]

names = ["Fan back top", "Fan top back", "Fan top front",
         "Fan front top", "Fan front bottom", "All"]

row, col = 0, 0
for i in range(6):
    cell_frame = tk.Frame(frame)
    cell_frame.grid(row=row, column=col, padx=10, pady=10)
    ColorWheel(cell_frame, images[i], callbacks[i], names[i])

    col += 1
    if col >= 3:
        col = 0
        row += 1

root.mainloop()
