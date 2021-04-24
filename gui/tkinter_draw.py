import random
import tkinter as tk
# from PIL import Image, ImageTk


class ExampleApp(tk.Tk):
    colors = ('red', 'green', 'blue', 'black', 'yellow')
    corner_diff = 5
    line_diff = 5

    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.canvas = tk.Canvas(self, width=512, height=512, cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self._draw_image()
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

        self.rects = {}
        self.rect = None
        self.rect_coords = None
        self.prev_x, self.prev_y = None, None
        self.moving = False
        self.resizing = False

    @classmethod
    def in_rectangle(cls, rec_coords, x, y):
        return rec_coords[0] <= x <= rec_coords[2] and rec_coords[1] <= y <= rec_coords[3]

    @classmethod
    def choose_color(cls):
        return random.choice(cls.colors)

    def _draw_image(self):
        pass
        # self.im = Image.open('./resource/image.jpg')
        # self.tk_im = ImageTk.PhotoImage(self.im)
        # self.canvas.create_image(0,0,anchor="nw",image=self.tk_im)

    def on_button_press(self, event):
        print('click press', event.x, event.y)

        if self.rects:
            self.rect = self.canvas.find_closest(event.x, event.y)
            self.rect_coords = self.canvas.coords(self.rect[0])
            if not self.in_rectangle(self.rect_coords, event.x, event.y):
                self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, fill=self.choose_color())
                self.start_x = event.x
                self.start_y = event.y
                self.moving = False
            else:
                self.start_x, self.start_y, self.end_x, self.end_y = self.rect_coords
                self.start_x = self.start_x - event.x
                self.start_y = self.start_y - event.y
                self.end_x = self.end_x - event.x
                self.end_y = self.end_y - event.y
                self.moving = True
        else:
            self.rect = self.canvas.create_rectangle(event.x, event.y, 1, 1, fill=self.choose_color())
            self.rects[1] = self.rect
            self.start_x = event.x
            self.start_y = event.y
            self.moving = False

    def on_move_press(self, event):
        if self.resizing:
            print('move', event.x, event.y)
            self.canvas.coords(self.rect,
                               self.start_x,
                               self.start_y,
                               self.end_x + event.x,
                               self.end_y + event.y)
        elif self.moving:
            print('move', event.x, event.y)
            self.canvas.coords(self.rect,
                               self.start_x + event.x,
                               self.start_y + event.y,
                               self.end_x + event.x,
                               self.end_y + event.y)
        else:
            self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_button_release(self, event):
        # print('release', event.x, event.y)
        self.rect = None


if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
