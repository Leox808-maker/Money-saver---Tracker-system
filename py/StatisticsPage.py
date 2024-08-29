import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random


class StatisticsPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Statistiche delle Spese", font=("Helvetica", 16)).pack(pady=20)
        charts_frame = tk.Frame(self)
        charts_frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.create_pie_chart(charts_frame)
        self.create_bar_chart(charts_frame)

    def create_pie_chart(self, parent_frame):
        categories = ["Spesa", "Intrattenimento", "Salute", "Trasporti", "Altro"]
        amounts = [random.randint(50, 300) for _ in categories]
        figure, ax = plt.subplots(figsize=(5, 5), dpi=100)
        ax.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        ax.set_title("Distribuzione delle Spese per Categoria", fontsize=14)
        pie_canvas = FigureCanvasTkAgg(figure, parent_frame)
        pie_canvas.get_tk_widget().grid(row=0, column=0, padx=20, pady=10)

    def create_bar_chart(self, parent_frame):
        months = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott", "Nov", "Dic"]
        expenses = [random.randint(400, 1500) for _ in months]
        figure, ax = plt.subplots(figsize=(7, 5), dpi=100)
        ax.bar(months, expenses, color=plt.cm.Paired.colors[:len(months)])
        ax.set_xlabel("Mese", fontsize=12)
        ax.set_ylabel("Spese (€)", fontsize=12)
        ax.set_title("Spese Mensili", fontsize=14)
        bar_canvas = FigureCanvasTkAgg(figure, parent_frame)
        bar_canvas.get_tk_widget().grid(row=0, column=1, padx=20, pady=10)

    def refresh_charts(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_widgets()


class ExpenseTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestione Spese")
        self.geometry("1200x800")
        self.tabs = ttk.Notebook(self)
        self.main_menu = MainMenu(self.tabs, self)
        self.settings_frame = SettingsMenu(self.tabs, self)
        self.category_manager_frame = ExpenseCategoryManager(self.tabs, self)
        self.expense_history_frame = ExpenseHistoryViewer(self.tabs, self)
        self.wishlist_goals_frame = WishlistAndGoalsManager(self.tabs, self)
        self.statistics_frame = StatisticsPage(self.tabs, self)
        self.tabs.add(self.main_menu, text="Menu")
        self.tabs.add(self.settings_frame, text="Impostazioni")
        self.tabs.add(self.category_manager_frame, text="Categorie Spese")
        self.tabs.add(self.expense_history_frame, text="Storico Spese")
        self.tabs.add(self.wishlist_goals_frame, text="Wishlist e Obiettivi")
        self.tabs.add(self.statistics_frame, text="Statistiche")
        self.tabs.pack(expand=1, fill="both")

    def set_light_theme(self):
        pass

    def set_dark_theme(self):
        pass

    def save_user_settings(self, settings):
        pass


if __name__ == "__main__":
    app = ExpenseTrackerApp()
    app.mainloop()
