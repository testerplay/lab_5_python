import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Функція для обчислення периметра і площі прямокутника
def RectPS(x1, y1, x2, y2):
    # Обчислюємо довжину і ширину прямокутника
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    perimeter = 2 * (width + height)
    area = width * height
    return perimeter, area

class MainWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=1)

        # Розміщення елементів GUI
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.lb1 = tk.Label(self, text="Enter x1, y1, x2, y2 coordinates:")
        self.lb1.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)

        self.x1_entry = tk.Entry(self)
        self.y1_entry = tk.Entry(self)
        self.x2_entry = tk.Entry(self)
        self.y2_entry = tk.Entry(self)

        self.x1_entry.grid(row=1, column=0, sticky=tk.NSEW)
        self.y1_entry.grid(row=1, column=1, sticky=tk.NSEW)
        self.x2_entry.grid(row=1, column=2, sticky=tk.NSEW)
        self.y2_entry.grid(row=1, column=3, sticky=tk.NSEW)

        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=2, column=0, columnspan=4, sticky=tk.NSEW)

        self.result_label = tk.Label(self, text="Results will be shown here.")
        self.result_label.grid(row=3, column=0, columnspan=4, sticky=tk.NSEW)

        self.plot_button = tk.Button(self, text="Show Plot", command=self.show_plot)
        self.plot_button.grid(row=4, column=0, columnspan=4, sticky=tk.NSEW)

        self.data = []  # Для зберігання результатів периметрів і площ

    def calculate(self):
        try:
            # Читання координат з полів введення
            x1 = float(self.x1_entry.get())
            y1 = float(self.y1_entry.get())
            x2 = float(self.x2_entry.get())
            y2 = float(self.y2_entry.get())

            # Обчислення периметра і площі
            perimeter, area = RectPS(x1, y1, x2, y2)

            # Виведення результату на екран
            result_text = f"Perimeter: {perimeter}\nArea: {area}"
            self.result_label.config(text=result_text)

            # Додавання результату до списку даних
            self.data.append((x1, y1, x2, y2, perimeter, area))

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

    def show_plot(self):
        if not self.data:
            messagebox.showerror("No Data", "Please calculate first.")
            return

        # Підготовка даних для графіка
        x1_values = [d[0] for d in self.data]
        y1_values = [d[1] for d in self.data]
        x2_values = [d[2] for d in self.data]
        y2_values = [d[3] for d in self.data]
        perimeter_values = [d[4] for d in self.data]
        area_values = [d[5] for d in self.data]

        # Створення графіку
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)

        # Побудова графіка периметрів і площ
        ax.plot(range(1, len(self.data) + 1), perimeter_values, label="Perimeter", color="blue", marker="o")
        ax.plot(range(1, len(self.data) + 1), area_values, label="Area", color="red", marker="x")

        ax.set_title("Perimeter and Area of Rectangles")
        ax.set_xlabel("Rectangle Number")
        ax.set_ylabel("Value")
        ax.legend()
        ax.grid(True)

        # Відображення графіка в Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid(row=5, column=0, columnspan=4, sticky=tk.NSEW)
        canvas.draw()

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Rectangle Perimeter and Area Calculator")
    window = MainWindow(app)
    app.mainloop()
