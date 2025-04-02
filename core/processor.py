from PIL import Image
from tkinter import messagebox
import os
from pathlib import Path
from typing import List

class ImageProcessor:
    def __init__(self, size_presets):
        self.SIZE_PRESETS = size_presets
    
    def process_images(self, input_paths: List[str], size: tuple, output_folder: str, progress_callback=None):
        """Process all selected images"""
        success_count = 0
        
        for i, input_path in enumerate(input_paths, 1):
            try:
                if progress_callback:
                    progress_callback(i, len(input_paths), os.path.basename(input_path))
                
                with Image.open(input_path) as img:
                    img_resized = img.resize(size, Image.Resampling.LANCZOS)
                    img_8bit = img_resized.convert('P', palette=Image.Palette.ADAPTIVE, colors=256)
                    
                    original_stem = Path(input_path).stem
                    output_filename = f"{original_stem}_{size[0]}x{size[1]}.png"
                    output_path = os.path.join(output_folder, output_filename)
                    
                    counter = 1
                    while os.path.exists(output_path):
                        output_filename = f"{original_stem}_{size[0]}x{size[1]}_{counter}.png"
                        output_path = os.path.join(output_folder, output_filename)
                        counter += 1
                    
                    img_8bit.save(output_path)
                    success_count += 1
                    
            except Exception as e:
                messagebox.showerror(
                    "Processing Error",
                    f"Failed to process {os.path.basename(input_path)}:\n{str(e)}"
                )
        
        return success_count