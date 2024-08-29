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

        if item_values:
            cost_entry.insert(0, item_values[1])
        tk.Label(popup, text="Priorità:").grid(row=2, column=0, padx=10, pady=10)
        priority_entry = tk.Entry(popup)
        priority_entry.grid(row=2, column=1, padx=10, pady=10)
        if item_values:
            priority_entry.insert(0, item_values[2])

        tk.Button(popup, text=action, command=lambda: self.process_wishlist_entry(popup, callback, name_entry.get(), cost_entry.get(), priority_entry.get())).grid(row=3, column=0, columnspan=2, pady=20)


    def process_wishlist_entry(self, popup, callback, name, cost, priority):
        if not name or not cost or not priority:
            messagebox.showwarning("Errore", "Compila tutti i campi.")
        else:
            try:
                cost = float(cost)
                callback(name, cost, priority)
                popup.destroy()
            except ValueError:
                messagebox.showerror("Errore", "Il costo stimato deve essere un numero valido.")

    def add_wishlist_to_list(self, name, cost, priority):
        self.wishlist.append((name, cost, priority))
        self.update_wishlist_tree()

    def update_wishlist_item(self, item):
        name = self.popup_name_entry.get()
        cost = self.popup_cost_entry.get()
        priority = self.popup_priority_entry.get()
        self.wishlist_tree.item(item, values=(name, cost, priority))
        # popup.destroy()



    def update_wishlist_tree(self):
        for item in self.wishlist_tree.get_children():
            self.wishlist_tree.delete(item)
        for wishlist_item in self.wishlist:
            self.wishlist_tree.insert("", tk.END, values=wishlist_item)



    def add_goal(self):
        self.create_goal_popup("Aggiungi", self.add_goal_to_list)


    def edit_goal(self):
        selected_item = self.goals_tree.selection()
        if selected_item:
            item_values = self.goals_tree.item(selected_item)["values"]
            self.create_goal_popup("Modifica", lambda: self.update_goal_item(selected_item), item_values)
        else:
            messagebox.showwarning("Errore", "Seleziona un obiettivo da modificare.")



    def delete_goal(self):
        selected_item = self.goals_tree.selection()
        if selected_item:
            self.goals_tree.delete(selected_item)
            self.goals = [goal for goal in self.goals if self.goals_tree.index(goal) != self.goals_tree.index(selected_item)]
            messagebox.showinfo("Obiettivo Eliminato", "L'obiettivo selezionato è stato eliminato.")
        else:
            messagebox.showwarning("Errore", "Seleziona un obiettivo da eliminare.")




    def create_goal_popup(self, action, callback, goal_values=None):
        popup = tk.Toplevel(self)
        popup.title(f"{action} Obiettivo")

        tk.Label(popup, text="Descrizione:").grid(row=0, column=0, padx=10, pady=10)
        description_entry = tk.Entry(popup)
        description_entry.grid(row=0, column=1, padx=10, pady=10)
        if goal_values:
            description_entry.insert(0, goal_values[0])

        tk.Label(popup, text="Importo Target (€):").grid(row=1, column=0, padx=10, pady=10)
        target_entry = tk.Entry(popup)
        target_entry.grid(row=1, column=1, padx=10, pady=10)
        if goal_values:
            target_entry.insert(0, goal_values[1])

        tk.Button(popup, text=action, command=lambda: self.process_goal_entry(popup, callback, description_entry.get(), target_entry.get())).grid(row=2, column=0, columnspan=2, pady=20)



    def process_goal_entry(self, popup, callback, description, target):
        if not description or not target:
            messagebox.showwarning("Errore", "Compila tutti i campi.")
        else:
            try:
                target = float(target)
                callback(description, target)
                popup.destroy()
            except ValueError:
                messagebox.showerror("Errore", "L'importo target deve essere un numero valido.")



    def add_goal_to_list(self, description, target):
        self.goals.append((description, target))
        self.update_goals_tree()

        def update_goal_item(self, item):
            description = self.popup_description_entry.get()
            target = self.popup_target_entry.get()
            self.goals_tree.item(item, values=(description, target))
            #  popup.destroy()

        def update_goals_tree(self):
            for item in self.goals_tree.get_children():
                self.goals_tree.delete(item)
            for goal in self.goals:
                self.goals_tree.insert("", tk.END, values=goal)

    class ExpenseTrackerApp(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Gestione Spese")
            self.geometry("1000x600")

            self.tabs = ttk.Notebook(self)

            self.main_menu = MainMenu(self.tabs, self)
            self.settings_frame = SettingsMenu(self.tabs, self)
            self.category_manager_frame = ExpenseCategoryManager(self.tabs, self)
            self.expense_history_frame = ExpenseHistoryViewer(self.tabs, self)
            self.wishlist_goals_frame = WishlistAndGoalsManager(self.tabs, self)

            self.tabs.add(self.main_menu, text="Menu")
            self.tabs.add(self.settings_frame, text="Impostazioni")
            self.tabs.add(self.category_manager_frame, text="Categorie Spese")
            self.tabs.add(self.expense_history_frame, text="Storico Spese")
            self.tabs.add(self.wishlist_goals_frame, text="Wishlist e Obiettivi")

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
