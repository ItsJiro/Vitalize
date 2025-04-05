import tkinter as tk
from config.constants import SIZE_PRESETS
from core.processor import ImageProcessor
from ui.main_window import MainWindow

class VitaLizeApp:
    def __init__(self, root: tk.Tk):
        self.processor = ImageProcessor(SIZE_PRESETS)
        self.main_window = MainWindow(root, self.processor, SIZE_PRESETS)

def main():
    root = tk.Tk()
    root.iconbitmap('vitalize.ico')
    app = VitaLizeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()