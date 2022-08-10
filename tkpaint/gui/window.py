# -*- coding: utf-8 -*-

__all__ = ["Window"]

import tkinter as tk


class Window(tk.Frame):
    def __init__(
        self,
        app,
        filename: str | None = None,
        size: tuple[int, int] = (640, 480),
        offset: tuple[int, int] = (50, 50),
    ):
        super(Window, self).__init__(master=app)
        self.set_title(filename)
        self.set_geometry(size, offset)

    def set_title(self, filename: str | None = None) -> str:
        if not filename:
            filename = "Untitled"
        self.master.title(f"{filename} - TkPaint")
        return filename

    def set_geometry(
        self,
        size: tuple[int, int] = (640, 480),
        offset: tuple[int, int] = (50, 50),
    ) -> str:
        w, h = size
        w, h = max(w, 640), max(h, 480)
        x, y = offset
        x, y = max(x, 0), max(y, 0)
        geometry = f"{w}x{h}+{x}+{y}"
        self.master.geometry(geometry)
        self.master.resizable(True, True)
        self.master.minsize(w, h)
        return geometry
