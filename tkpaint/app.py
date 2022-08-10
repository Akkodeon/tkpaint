# -*- coding: utf-8 -*-

__all__ = ["TkPaint"]

import tkinter as tk


class TkPaint(tk.Frame):
    def __init__(self, master=None):
        super(TkPaint, self).__init__(master)
        self.master.title("TkPaint")


if __name__ == "__main__":
    app = TkPaint()
    app.mainloop()
