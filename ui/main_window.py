import tkinter as tk
from tkinter import ttk, messagebox
from .components.header import Header
from .components.file_input import FileInput
from .components.settings_panel import SettingsPanel

class MainWindow:
    def __init__(self, root, processor, size_presets):
        self.root = root
        self.processor = processor
        self.root.title("Vitalize")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        self.setup_ui(size_presets)
    
    def setup_ui(self, size_presets):
        """Setup the main application interface"""
        main_container = ttk.Frame(self.root, padding="10")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Add components
        Header(main_container)
        self.file_input = FileInput(main_container)
        self.settings_panel = SettingsPanel(main_container, size_presets)
        
        # Process button
        process_frame = ttk.Frame(main_container)
        process_frame.pack(fill=tk.X, pady=(0, 0))
        
        center_frame = ttk.Frame(process_frame)
        center_frame.pack(expand=True)
        
        ttk.Button(
            center_frame,
            text="Process Images",
            command=self.process_images,
            width=15
        ).pack(pady=5)
    
    def process_images(self):
        """Handle image processing"""
        input_paths = self.file_input.get_files()
        
        if not input_paths:
            messagebox.showwarning("No Files", "Please add some image files first!")
            return
        
        settings = self.settings_panel.get_settings()
        
        if settings['output_folder'] is None:
            output_folder = os.path.dirname(input_paths[0])
        else:
            output_folder = settings['output_folder']
            if not output_folder:
                messagebox.showwarning("No Folder", "Please select an output folder!")
                return
        
        # Create progress window
        progress_window = tk.Toplevel(self.root)
        progress_window.title("Processing Images")
        progress_window.resizable(False, False)
        progress_window.grab_set()
        
        progress_label = ttk.Label(
            progress_window,
            text=f"Processing 1 of {len(input_paths)}...",
            font=('TkDefaultFont', 9)
        )
        progress_label.pack(pady=(15, 5), padx=20)
        
        progress_bar = ttk.Progressbar(
            progress_window,
            maximum=len(input_paths),
            length=400
        )
        progress_bar.pack(pady=(0, 15), padx=20)
        
        def update_progress(current, total, filename):
            progress_label.config(text=f"Processing {current} of {total}\n{filename}")
            progress_bar['value'] = current
            progress_window.update()
        
        # Process images
        success_count = self.processor.process_images(
            input_paths,
            settings['size'],
            output_folder,
            update_progress
        )
        
        progress_window.destroy()
        
        # Show results
        result_message = (
            f"Processing complete!\n\n"
            f"Successfully processed: {success_count} of {len(input_paths)} files\n"
            f"Output folder: {output_folder}\n"
            f"Target size: {settings['size'][0]}×{settings['size'][1]}\n"
            f"Color depth: 256 colors (8-bit)"
        )
        
        messagebox.showinfo("Processing Complete", result_message)