import tkinter as tk
from tkinter import ttk, StringVar, filedialog

class SettingsPanel:
    def __init__(self, parent, size_presets):
        self.size_presets = size_presets
        
        self.frame = ttk.LabelFrame(parent, text=" Conversion Settings ", padding="3")
        self.frame.pack(fill=tk.X, pady=(0, 3))
        
        # Size selection
        ttk.Label(self.frame, text="Target Size:").pack(anchor=tk.W)
        
        self.size_var = StringVar(value=list(self.size_presets.keys())[0])
        
        for size_name, size_info in self.size_presets.items():
            ttk.Radiobutton(
                self.frame,
                text=f"{size_name} - {size_info['description']}",
                variable=self.size_var,
                value=size_name
            ).pack(anchor=tk.W, pady=2)
        
        # Output options
        ttk.Label(self.frame, text="\nOutput Location:").pack(anchor=tk.W)
        
        self.output_var = StringVar(value="same_folder")
        
        ttk.Radiobutton(
            self.frame,
            text="Same folder as originals",
            variable=self.output_var,
            value="same_folder",
            command=self.toggle_output_widgets
        ).pack(anchor=tk.W)
        
        custom_frame = ttk.Frame(self.frame)
        custom_frame.pack(fill=tk.X, pady=2)
        
        ttk.Radiobutton(
            custom_frame,
            text="Custom folder:",
            variable=self.output_var,
            value="custom_folder",
            command=self.toggle_output_widgets
        ).pack(side=tk.LEFT)
        
        # Custom folder entry frame
        entry_btn_frame = ttk.Frame(custom_frame)
        entry_btn_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
        
        self.custom_folder_path = StringVar()
        self.folder_entry = ttk.Entry(
            entry_btn_frame,
            textvariable=self.custom_folder_path,
            state='disabled'
        )
        self.folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.browse_btn = ttk.Button(
            entry_btn_frame,
            text="Browse...",
            command=self.select_custom_folder,
            width=8,
            state='disabled'
        )
        self.browse_btn.pack(side=tk.LEFT, padx=(5, 0))
    
    def toggle_output_widgets(self):
        """Enable/disable custom folder widgets based on selection"""
        if self.output_var.get() == "custom_folder":
            self.folder_entry.config(state='normal')
            self.browse_btn.config(state='normal')
        else:
            self.folder_entry.config(state='disabled')
            self.browse_btn.config(state='disabled')
            self.custom_folder_path.set('')
    
    def select_custom_folder(self):
        """Select custom output folder"""
        folder_path = filedialog.askdirectory(title="Select Output Folder")
        if folder_path:
            self.custom_folder_path.set(folder_path)
    
    def get_settings(self):
        """Return current settings"""
        size_name = self.size_var.get()
        return {
            'size': self.size_presets[size_name]["size"],
            'output_folder': self.custom_folder_path.get() if self.output_var.get() == "custom_folder" else None
        }