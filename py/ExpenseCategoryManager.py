import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ExpenseCategoryManager(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.categories = {}
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Gestione Categorie Spese", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self, text="Aggiungi Categoria:", font=("Helvetica", 14)).pack(anchor="w", padx=20)
        self.category_entry = tk.Entry(self)
        self.category_entry.pack(anchor="w", padx=40, pady=5)
        self.add_category_button = tk.Button(self, text="Aggiungi", command=self.add_category)
        self.add_category_button.pack(anchor="w", padx=40)

        tk.Label(self, text="Aggiungi Spesa per Categoria:", font=("Helvetica", 14)).pack(anchor="w", padx=20, pady=(20, 0))
        self.category_var = tk.StringVar(value="Seleziona Categoria")
        self.category_combobox = ttk.Combobox(self, values=list(self.categories.keys()), textvariable=self.category_var)
        self.category_combobox.pack(anchor="w", padx=40, pady=5)

        tk.Label(self, text="Importo:", font=("Helvetica", 14)).pack(anchor="w", padx=20)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(anchor="w", padx=40, pady=5)
        self.add_expense_button = tk.Button(self, text="Aggiungi Spesa", command=self.add_expense)
        self.add_expense_button.pack(anchor="w", padx=40, pady=5)

        tk.Label(self, text="Riepilogo Spese per Categoria:", font=("Helvetica", 14)).pack(anchor="w", padx=20, pady=(20, 0))
        self.summary_button = tk.Button(self, text="Mostra Riepilogo", command=self.show_summary)
        self.summary_button.pack(anchor="w", padx=40, pady=10)

        tk.Label(self, text="Gestione Categorie Esistenti:", font=("Helvetica", 14)).pack(anchor="w", padx=20, pady=(20, 0))
        self.category_listbox = tk.Listbox(self)
        self.category_listbox.pack(anchor="w", padx=40, pady=10)
        self.delete_category_button = tk.Button(self, text="Elimina Categoria", command=self.delete_category)
        self.delete_category_button.pack(anchor="w", padx=40, pady=5)

    def add_category(self):
        category_name = self.category_entry.get().strip()
        if category_name and category_name not in self.categories:
            self.categories[category_name] = 0.0
            self.update_category_combobox()
            self.category_listbox.insert(tk.END, category_name)
            messagebox.showinfo("Categoria Aggiunta", f"La categoria '{category_name}' è stata aggiunta con successo.")
        elif category_name in self.categories:
            messagebox.showwarning("Errore", "Questa categoria esiste già!")
        else:
            messagebox.showwarning("Errore", "Il nome della categoria non può essere vuoto!")