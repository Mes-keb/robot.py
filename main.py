
from tkinter import Tk
from gui import RobotGUI


def main():
    window = Tk()
    app = RobotGUI(window)
    window.mainloop()


    if __name__ == "__main__":
        main()