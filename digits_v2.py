
import tensorflow as tf
import tkinter as tk
import numpy as np
import PIL
import io
import matplotlib.pyplot as plt
from skimage.transform import resize


model = tf.keras.models.load_model('digit_recognizer_model')


class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.canvas_width = 500
        self.canvas_height = 500
        self.brush_size = 20
        self.color = "black"

        
        # Create canvas
        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.update_predict_header)
        
        # Create clear button
        clear_button = tk.Button(self.master, text="Clear Canvas", command=self.clear_canvas)
        clear_button.pack()
        
        # Create Prediction 
        self.prediction_header = tk.Label(self.master, text="Predicted: ", font=("Arial", 16))
        self.prediction_header.pack()
        
    def draw(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def clear_canvas(self):
        self.canvas.delete("all")
    
    def update_predict_header(self, event):
        ps = self.canvas.postscript(colormode="color")
        img = PIL.Image.open(io.BytesIO(ps.encode("utf-8")))
        img = PIL.ImageOps.invert(img)
        arr_resized = resize(np.asarray(img), (28, 28)).mean(axis=2).reshape(-1,28,28,1)
        num = np.argmax(model.predict(arr_resized, verbose=0)[0])
        self.prediction_header.configure(text=f"Predicted: {num}")
        
    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    app.run()
