
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class ExpenseHistoryViewer(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.expense_history = []
        self.create_widgets()

    def create_widgets(self):
        # Titolo della schermata
        tk.Label(self, text="Storico Spese", font=("Helvetica", 16)).pack(pady=20)

        self.history_tree = ttk.Treeview(self, columns=("Categoria", "Importo", "Data"), show="headings")
        self.history_tree.heading("Categoria", text="Categoria")
        self.history_tree.heading("Importo", text="Importo (€)")
        self.history_tree.heading("Data", text="Data")
        self.history_tree.column("Categoria", width=200)
        self.history_tree.column("Importo", width=100)
        self.history_tree.column("Data", width=150)
        self.history_tree.pack(fill="both", expand=True, padx=20, pady=10)

        self.delete_button = tk.Button(self, text="Elimina Spesa Selezionata", command=self.delete_selected_expense)
        self.delete_button.pack(pady=10)

        self.update_button = tk.Button(self, text="Aggiorna", command=self.update_history)
        self.update_button.pack(pady=10)

    def add_expense(self, category, amount):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.expense_history.append((category, amount, date))
        self.update_history()

    def update_history(self):
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)

        for expense in self.expense_history:
            self.history_tree.insert("", tk.END, values=expense)

    def delete_selected_expense(self):
        selected_item = self.history_tree.selection()
        if selected_item:
            expense_values = self.history_tree.item(selected_item)["values"]
            self.history_tree.delete(selected_item)
            self.expense_history = [exp for exp in self.expense_history if exp != tuple(expense_values)]
            messagebox.showinfo("Spesa Eliminata", "La spesa selezionata è stata eliminata.")
        else:
            messagebox.showwarning("Errore", "Seleziona una spesa da eliminare.")

class ExpenseTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestione Spese")
        self.geometry("800x600")

        self.tabs = ttk.Notebook(self)

        self.main_menu = MainMenu(self.tabs, self)
        self.settings_frame = SettingsMenu(self.tabs, self)
        self.category_manager_frame = ExpenseCategoryManager(self.tabs, self)
        self.expense_history_frame = ExpenseHistoryViewer(self.tabs, self)

        self.tabs.add(self.main_menu, text="Menu")
        self.tabs.add(self.settings_frame, text="Impostazioni")
        self.tabs.add(self.category_manager_frame, text="Categorie Spese")
        self.tabs.add(self.expense_history_frame, text="Storico Spese")

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

