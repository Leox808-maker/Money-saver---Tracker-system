import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime


class GestioneCarteCredito:
    def __init__(self, root):
        self.root = root
        self.carte_data = []
        self.transazioni = []
        self.carte_frame = tk.Frame(root)
        self.carte_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.title_label = tk.Label(self.carte_frame, text="Gestione Carte di Credito", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        self.carte_list_frame = tk.Frame(self.carte_frame)
        self.carte_list_frame.pack(fill=tk.BOTH, expand=True)
        self.carte_listbox = tk.Listbox(self.carte_list_frame)
        self.carte_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar = tk.Scrollbar(self.carte_list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.carte_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.carte_listbox.yview)
        self.carta_entry_frame = tk.Frame(self.carte_frame)
        self.carta_entry_frame.pack(fill=tk.X)

        self.numero_carta_label = tk.Label(self.carta_entry_frame, text="Numero Carta:")
        self.numero_carta_label.grid(row=0, column=0, padx=10, pady=5)
        self.numero_carta_entry = tk.Entry(self.carta_entry_frame)
        self.numero_carta_entry.grid(row=0, column=1, padx=10, pady=5)
        self.nome_carta_label = tk.Label(self.carta_entry_frame, text="Nome:")
        self.nome_carta_label.grid(row=1, column=0, padx=10, pady=5)
        self.nome_carta_entry = tk.Entry(self.carta_entry_frame)
        self.nome_carta_entry.grid(row=1, column=1, padx=10, pady=5)
        self.data_scadenza_label = tk.Label(self.carta_entry_frame, text="Data Scadenza (MM/YY):")
        self.data_scadenza_label.grid(row=2, column=0, padx=10, pady=5)
        self.data_scadenza_entry = tk.Entry(self.carta_entry_frame)
        self.data_scadenza_entry.grid(row=2, column=1, padx=10, pady=5)
        self.cvc_label = tk.Label(self.carta_entry_frame, text="CVC:")
        self.cvc_label.grid(row=3, column=0, padx=10, pady=5)

        self.cvc_entry = tk.Entry(self.carta_entry_frame)
        self.cvc_entry.grid(row=3, column=1, padx=10, pady=5)
        self.saldo_label = tk.Label(self.carta_entry_frame, text="Saldo Iniziale:")
        self.saldo_label.grid(row=4, column=0, padx=10, pady=5)
        self.saldo_entry = tk.Entry(self.carta_entry_frame)
        self.saldo_entry.grid(row=4, column=1, padx=10, pady=5)
        self.aggiungi_carta_btn = tk.Button(self.carta_entry_frame, text="Aggiungi Carta", command=self.aggiungi_carta)
        self.aggiungi_carta_btn.grid(row=5, column=0, columnspan=2, pady=10)
        self.rimuovi_carta_btn = tk.Button(self.carte_frame, text="Rimuovi Carta", command=self.rimuovi_carta)
        self.rimuovi_carta_btn.pack(pady=10)

        self.transazioni_btn = tk.Button(self.carte_frame, text="Visualizza Transazioni",
                                         command=self.visualizza_transazioni)
        self.transazioni_btn.pack(pady=10)
        self.aggiungi_transazione_btn = tk.Button(self.carte_frame, text="Aggiungi Transazione",
                                                  command=self.aggiungi_transazione)
        self.aggiungi_transazione_btn.pack(pady=10)
        self.saldo_carte_btn = tk.Button(self.carte_frame, text="Visualizza Saldo Carte",
                                         command=self.visualizza_saldo_carte)
        self.saldo_carte_btn.pack(pady=10)