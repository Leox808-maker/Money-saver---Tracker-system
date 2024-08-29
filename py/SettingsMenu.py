import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class SettingsMenu(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Menu Impostazioni", font=("Helvetica", 16)).pack(pady=20)

        tk.Label(self, text="Tema:", font=("Helvetica", 14)).pack(anchor="w", padx=20)
        self.theme_var = tk.StringVar(value="Chiaro")
        self.light_theme_radiobutton = tk.Radiobutton(self, text="Chiaro", variable=self.theme_var, value="Chiaro", command=self.change_theme)
        self.dark_theme_radiobutton = tk.Radiobutton(self, text="Scuro", variable=self.theme_var, value="Scuro", command=self.change_theme)
        self.light_theme_radiobutton.pack(anchor="w", padx=40)
        self.dark_theme_radiobutton.pack(anchor="w", padx=40)

        tk.Label(self, text="Valuta:", font=("Helvetica", 14)).pack(anchor="w", padx=20, pady=(10, 0))
        self.currency_var = tk.StringVar(value="€")
        self.currency_combobox = ttk.Combobox(self, values=["€", "$", "£", "¥"], textvariable=self.currency_var)
        self.currency_combobox.pack(anchor="w", padx=40)
        self.currency_combobox.bind("<<ComboboxSelected>>", self.change_currency)

        # Notifiche
        tk.Label(self, text="Notifiche:", font=("Helvetica", 14)).pack(anchor="w", padx=20, pady=(20, 0))
        self.notifications_var = tk.BooleanVar(value=True)
        self.notifications_checkbox = tk.Checkbutton(self, text="Abilita notifiche di spesa", variable=self.notifications_var, command=self.toggle_notifications)
        self.notifications_checkbox.pack(anchor="w", padx=40)

        tk.Label(self, text="Limite Spesa Mensile:", font=("Helvetica", 14)).pack(anchor="w", padx=20, pady=(20, 0))
        self.limit_var = tk.DoubleVar(value=1000)
        self.limit_spinbox = tk.Spinbox(self, from_=0, to=10000, increment=50, textvariable=self.limit_var)
        self.limit_spinbox.pack(anchor="w", padx=40)

        self.save_button = tk.Button(self, text="Salva Impostazioni", command=self.save_settings)
        self.save_button.pack(pady=20)

        self.reset_button = tk.Button(self, text="Ripristina Impostazioni", command=self.reset_settings)
        self.reset_button.pack()

    def change_theme(self):
        theme = self.theme_var.get()
        if theme == "Chiaro":
            self.app.set_light_theme()
        elif theme == "Scuro":
            self.app.set_dark_theme()
        messagebox.showinfo("Tema cambiato", f"Il tema è stato cambiato a {theme}")

    def change_currency(self, event=None):
        currency = self.currency_var.get()
        messagebox.showinfo("Valuta cambiata", f"La valuta è stata cambiata a {currency}")

    def toggle_notifications(self):
        if self.notifications_var.get():
            messagebox.showinfo("Notifiche", "Le notifiche sono abilitate")
        else:
            messagebox.showinfo("Notifiche", "Le notifiche sono disabilitate")

    def save_settings(self):
        theme = self.theme_var.get()
        currency = self.currency_var.get()
        notifications = self.notifications_var.get()
        limit = self.limit_var.get()

        settings = {
            "theme": theme,
            "currency": currency,
            "notifications": notifications,
            "limit": limit,
        }
        self.app.save_user_settings(settings)
        messagebox.showinfo("Impostazioni Salvate", "Le impostazioni sono state salvate con successo")

    def reset_settings(self):
        self.theme_var.set("Chiaro")
        self.currency_var.set("€")
        self.notifications_var.set(True)
        self.limit_var.set(1000)

        messagebox.showinfo("Impostazioni Ripristinate", "Le impostazioni sono state ripristinate ai valori di default")
        self.change_theme()