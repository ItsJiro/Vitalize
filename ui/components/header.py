import tkinter as tk
from tkinter import ttk

class Header:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(
            self.frame,
            text="Vitalize",
            font=('Courier', 24, 'bold')
        ).pack()
        
        ttk.Label(
            self.frame,
            text="PS Vita Theme Image Converter",
            font=('TkDefaultFont', 10)
        ).pack(pady=(0, 10))