import tkinter as tk

from ui.app import ImageProcessingApp


def main():

    root = tk.Tk()

    ImageProcessingApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()