# Pi Zero display client
import cv2
import tkinter as tk
from PIL import Image, ImageTk

class TruckDisplay:
    def __init__(self, side):
        self.side = side
        self.root = tk.Tk()
        self.root.title(f"{side} View")
        self.label = tk.Label(self.root)
        self.label.pack()
        self.update_frame()
        
    def get_stream_url(self):
        # Portenta H7 IP
        if self.side == "LEFT":
            return "http://192.168.1.10/left_stream"
        elif self.side == "RIGHT":
            return "http://192.168.1.10/right_stream"
        else:
            return "http://192.168.1.10/rear_stream"
    
    def update_frame(self):
        cap = cv2.VideoCapture(self.get_stream_url())
        ret, frame = cap.read()
        if ret:
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)
        self.root.after(50, self.update_frame)  # ~20 FPS

if __name__ == "__main__":
    import sys
    app = TruckDisplay(sys.argv[1])  # "LEFT" or "RIGHT"
    app.root.mainloop()
