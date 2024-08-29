import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class WishlistAndGoalsManager(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.wishlist = []  # names
        self.goals = []  # obb.
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Obiettivi e Wishlist", font=("Helvetica", 16)).pack(pady=20)

        wishlist_frame = tk.Frame(self)
        wishlist_frame.pack(side="left", fill="both", expand=True, padx=20)

        tk.Label(wishlist_frame, text="Wishlist Acquisti", font=("Helvetica", 14)).pack(pady=10)

        self.wishlist_tree = ttk.Treeview(wishlist_frame, columns=("Nome", "Costo Stimato", "Priorità"),
                                          show="headings")
        self.wishlist_tree.heading("Nome", text="Nome")
        self.wishlist_tree.heading("Costo Stimato", text="Costo Stimato (€)")
        self.wishlist_tree.heading("Priorità", text="Priorità")
        self.wishlist_tree.column("Nome", width=200)
        self.wishlist_tree.column("Costo Stimato", width=150)
        self.wishlist_tree.column("Priorità", width=100)
        self.wishlist_tree.pack(fill="both", expand=True, pady=10)

        wishlist_buttons_frame = tk.Frame(wishlist_frame)
        wishlist_buttons_frame.pack(pady=10)

        self.add_wishlist_button = tk.Button(wishlist_buttons_frame, text="Aggiungi Elemento",
                                             command=self.add_wishlist_item)
        self.add_wishlist_button.grid(row=0, column=0, padx=10)
        self.edit_wishlist_button = tk.Button(wishlist_buttons_frame, text="Modifica Elemento",
                                              command=self.edit_wishlist_item)
        self.edit_wishlist_button.grid(row=0, column=1, padx=10)
        self.delete_wishlist_button = tk.Button(wishlist_buttons_frame, text="Elimina Elemento",
                                                command=self.delete_wishlist_item)
        self.delete_wishlist_button.grid(row=0, column=2, padx=10)

        goals_frame = tk.Frame(self)
        goals_frame.pack(side="right", fill="both", expand=True, padx=20)

        tk.Label(goals_frame, text="Obiettivi Finanziari", font=("Helvetica", 14)).pack(pady=10)
        self.goals_tree = ttk.Treeview(goals_frame, columns=("Descrizione", "Importo Target (€)"), show="headings")
        self.goals_tree.heading("Descrizione", text="Descrizione")
        self.goals_tree.heading("Importo Target (€)", text="Importo Target (€)")
        self.goals_tree.column("Descrizione", width=250)
        self.goals_tree.column("Importo Target (€)", width=150)
        self.goals_tree.pack(fill="both", expand=True, pady=10)

        goals_buttons_frame = tk.Frame(goals_frame)
        goals_buttons_frame.pack(pady=10)
        self.add_goal_button = tk.Button(goals_buttons_frame, text="Aggiungi Obiettivo", command=self.add_goal)
        self.add_goal_button.grid(row=0, column=0, padx=10)
        self.edit_goal_button = tk.Button(goals_buttons_frame, text="Modifica Obiettivo", command=self.edit_goal)
        self.edit_goal_button.grid(row=0, column=1, padx=10)
        self.delete_goal_button = tk.Button(goals_buttons_frame, text="Elimina Obiettivo", command=self.delete_goal)
        self.delete_goal_button.grid(row=0, column=2, padx=10)

    def add_wishlist_item(self):
        self.create_wishlist_popup("Aggiungi", self.add_wishlist_to_list)

    def edit_wishlist_item(self):
        selected_item = self.wishlist_tree.selection()
        if selected_item:
            item_values = self.wishlist_tree.item(selected_item)["values"]
            self.create_wishlist_popup("Modifica", lambda: self.update_wishlist_item(selected_item), item_values)
        else:
            messagebox.showwarning("Errore", "Seleziona un elemento dalla wishlist da modificare.")

    def delete_wishlist_item(self):
        selected_item = self.wishlist_tree.selection()
        if selected_item:
            self.wishlist_tree.delete(selected_item)
            self.wishlist = [item for item in self.wishlist if
                             self.wishlist_tree.index(item) != self.wishlist_tree.index(selected_item)]
            messagebox.showinfo("Elemento Eliminato", "L'elemento selezionato è stato eliminato.")
        else:
            messagebox.showwarning("Errore", "Seleziona un elemento dalla wishlist da eliminare.")

    def create_wishlist_popup(self, action, callback, item_values=None):
        popup = tk.Toplevel(self)
        popup.title(f"{action} Elemento Wishlist")

        tk.Label(popup, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(popup)
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        if item_values:
            name_entry.insert(0, item_values[0])

        tk.Label(popup, text="Costo Stimato (€):").grid(row=1, column=0, padx=10, pady=10)
        cost_entry = tk.Entry(popup)
        cost_entry.grid(row=1, column=1, padx=10, pady=10)