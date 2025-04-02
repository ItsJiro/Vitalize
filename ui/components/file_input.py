import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from typing import Set

class FileInput:
    def __init__(self, parent):
        self.added_files: Set[str] = set()
        
        self.frame = ttk.LabelFrame(parent, text=" Input Images ", padding="10")
        self.frame.pack(fill=tk.X, pady=(0, 10))
        
        self.input_listbox = tk.Listbox(
            self.frame,
            height=6,
            selectmode=tk.EXTENDED,
            background='white',
            font=('TkDefaultFont', 9)
        )
        self.input_listbox.pack(fill=tk.X, pady=(0, 10))
        
        btn_frame = ttk.Frame(self.frame)
        btn_frame.pack(fill=tk.X)
        
        ttk.Button(
            btn_frame,
            text="Add Files",
            command=self.add_files
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Button(
            btn_frame,
            text="Clear All",
            command=self.clear_files
        ).pack(side=tk.LEFT)
    
    def add_files(self):
        """Add files to the input list, preventing duplicates"""
        file_paths = filedialog.askopenfilenames(
            title="Select Image Files",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        
        if file_paths:
            for path in file_paths:
                if path not in self.added_files:
                    self.input_listbox.insert(tk.END, path)
                    self.added_files.add(path)
                else:
                    messagebox.showwarning(
                        "Duplicate File",
                        f"'{os.path.basename(path)}' is already in the list!"
                    )
    
    def clear_files(self):
        """Clear all files from the input list"""
        self.input_listbox.delete(0, tk.END)
        self.added_files.clear()
    
    def get_files(self):
        return self.input_listbox.get(0, tk.END)