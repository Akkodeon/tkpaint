# -*- coding: utf-8 -*-

__all__ = ["TkPaint"]

import tkinter as tk

from tkpaint.gui import Window


class TkPaint(tk.Tk):
    def __init__(self):
        super(TkPaint, self).__init__()
        self.window = Window(app=self)


if __name__ == "__main__":
    app = TkPaint()
    app.mainloop()
