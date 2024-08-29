import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime


class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestione Spese")
        self.root.geometry("800x600")

        self.create_main_widgets()

    def create_main_widgets(self):
        self.tabs = ttk.Notebook(self.root)

        self.home_frame = HomeFrame(self.tabs)
        self.add_expense_frame = AddExpenseFrame(self.tabs, self)
        self.view_expenses_frame = ViewExpensesFrame(self.tabs, self)
        self.statistics_frame = StatisticsFrame(self.tabs, self)

        self.tabs.add(self.home_frame, text="Home")
        self.tabs.add(self.add_expense_frame, text="Aggiungi Spesa")
        self.tabs.add(self.view_expenses_frame, text="Visualizza Spese")
        self.tabs.add(self.statistics_frame, text="Statistiche")

        self.tabs.pack(expand=1, fill="both")

        self.expenses = []


class HomeFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Benvenuto nell'app di gestione delle spese", font=("Helvetica", 16))
        label.pack(pady=20)


class AddExpenseFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Aggiungi una nuova spesa", font=("Helvetica", 14)).pack(pady=10)

        self.description_label = tk.Label(self, text="Descrizione:")
        self.description_label.pack()

        self.description_entry = tk.Entry(self)
        self.description_entry.pack()

        self.amount_label = tk.Label(self, text="Importo:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()

        self.category_label = tk.Label(self, text="Categoria:")
        self.category_label.pack()

        self.category_combobox = ttk.Combobox(self, values=["Cibo", "Trasporti", "Svago", "Altro"])
        self.category_combobox.pack()

        self.date_label = tk.Label(self, text="Data:")
        self.date_label.pack()

        self.date_entry = tk.Entry(self)
        self.date_entry.pack()
        self.date_entry.insert(0, datetime.date.today().strftime("%Y-%m-%d"))

        self.add_button = tk.Button(self, text="Aggiungi Spesa", command=self.add_expense)
        self.add_button.pack(pady=10)

    def add_expense(self):
        description = self.description_entry.get()
        amount = self.amount_entry.get()
        category = self.category_combobox.get()
        date = self.date_entry.get()

        if not description or not amount or not category or not date:
            messagebox.showwarning("Campi mancanti", "Per favore, riempi tutti i campi")
            return
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showwarning("Errore di input", "L'importo deve essere un numero valido")
            return

        expense = {"description": description, "amount": amount, "category": category, "date": date}
        self.app.expenses.append(expense)
        messagebox.showinfo("Spesa aggiunta", "Spesa aggiunta con successo")

        self.clear_fields()

    def clear_fields(self):
        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_combobox.set("")
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.date.today().strftime("%Y-%m-%d"))

class ViewExpensesFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Visualizza Spese", font=("Helvetica", 14)).pack(pady=10)

        self.expenses_tree = ttk.Treeview(self, columns=("Descrizione", "Importo", "Categoria", "Data"), show="headings")
        self.expenses_tree.heading("Descrizione", text="Descrizione")
        self.expenses_tree.heading("Importo", text="Importo")
        self.expenses_tree.heading("Categoria", text="Categoria")
        self.expenses_tree.heading("Data", text="Data")
        self.expenses_tree.pack(expand=True, fill="both")

        self.refresh_button = tk.Button(self, text="Aggiorna", command=self.refresh_expenses)
        self.refresh_button.pack(pady=10)

    def refresh_expenses(self):
        for row in self.expenses_tree.get_children():
            self.expenses_tree.delete(row)

        for expense in self.app.expenses:
            self.expenses_tree.insert("", tk.END, values=(expense["description"], expense["amount"], expense["category"], expense["date"]))




class StatisticsFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Statistiche Spese", font=("Helvetica", 14)).pack(pady=10)

        self.stats_label = tk.Label(self, text="")
        self.stats_label.pack(pady=20)

        self.refresh_button = tk.Button(self, text="Aggiorna Statistiche", command=self.calculate_statistics)
        self.refresh_button.pack()

    def calculate_statistics(self):
        total_spent = sum(expense["amount"] for expense in self.app.expenses)
        num_expenses = len(self.app.expenses)

        if num_expenses == 0:
            average_spent = 0
        else:
            average_spent = total_spent / num_expenses

        stats_text = f"Totale Spese: {total_spent:.2f} €\nNumero di spese: {num_expenses}\nSpesa media: {average_spent:.2f} €"
        self.stats_label.config(text=stats_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()