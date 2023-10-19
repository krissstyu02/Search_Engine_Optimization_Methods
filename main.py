import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import numdifftools as nd
from tkinter import scrolledtext
from LR1 import GradientDescentAlgorithm
from LR2 import Simplex_method
from scipy.optimize import minimize


# Создание окна приложения
root = tk.Tk()
root.title("Методы поисковой оптимизации")

notebook = ttk.Notebook(root)
notebook.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Инициализация графика при запуске программы
fig = plt.figure(figsize=(8, 9))  # Установка размеров фигуры (ширина, высота)
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.RIGHT, padx=20)

# Вкладка для лр1
param_frame = ttk.Frame(notebook,padding=(15, 0))
notebook.add(param_frame, text="ЛР1")

GradientDescentAlgorithm(param_frame,root,ax,canvas)

param_frame2 = ttk.Frame(notebook)
notebook.add(param_frame2, text="ЛР2")

Simplex_method(param_frame2,root,ax,canvas)

param_frame3 = ttk.Frame(notebook)
notebook.add(param_frame3, text="ЛР3")

param_frame4 = ttk.Frame(notebook)
notebook.add(param_frame4, text="ЛР4")

param_frame5 = ttk.Frame(notebook)
notebook.add(param_frame5, text="ЛР5")

param_frame6 = ttk.Frame(notebook)
notebook.add(param_frame6, text="ЛР6")

param_frame7 = ttk.Frame(notebook)
notebook.add(param_frame7, text="ЛР7")

param_frame8 = ttk.Frame(notebook)
notebook.add(param_frame8, text="ЛР8")

root.mainloop()
