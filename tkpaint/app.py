# -*- coding: utf-8 -*-

__all__ = ["TkPaint"]

import tkinter as tk


class TkPaint(tk.Tk):
    def __init__(self):
        super(TkPaint, self).__init__()
        self.title("TkPaint")
        self.geometry("640x480+50+50")


if __name__ == "__main__":
    app = TkPaint()
    app.mainloop()
