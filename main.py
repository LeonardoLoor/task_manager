import tkinter as tk
from app.interfaz import Interfaz

def main():
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()

if __name__ == "__main__":
    main()