
import tkinter as tk
from tkinter import ttk

from robot import Robot


class RobotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RoboMove - Student Robotics")
        self.root.geometry("760x650")
        self.root.minimize(620, 580)

        self.robot = Robot(grid_size=9)
        self.cell_size = 48
        self.padding = 20

        self.status = tk.StringVar()
        self.message = tk.StringVar(valyue="Robot is ready!")

        self.build_interface()
        self.draw_grid()

    def buil_interface(self):
        title = ttk.Label(
            self.root,
            text="RoboMove Simulator",
            font=("Arial", 20, "bold")
        ) 
        title.pack(pady=10)

        self.canvas = tk.Canvas(
            self.root,
            width=self.cell_size * 9,
            height=self.cell_size * 9,
            bg="white",
            highlightthickness=1,
            highlightthickness="#a0bfe5eb"
        )   
        self.canvas.pack(padx=10, pady=5)

        controls = ttk.Frame(self.root)
        controls.pack(pady=10)

        ttk.Button