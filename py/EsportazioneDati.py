import tkinter as tk
from tkinter import filedialog
import csv
import json

class EsportazioneDati:
    def __init__(self, root, dati_spese, dati_carte, dati_obiettivi):
        self.root = root
        self.dati_spese = dati_spese
        self.dati_carte = dati_carte
        self.dati_obiettivi = dati_obiettivi

        self.export_frame = tk.Frame(root)
        self.export_frame.pack(pady=20)

        self.label = tk.Label(self.export_frame, text="Esporta i tuoi dati")
        self.label.pack(pady=10)

        self.esporta_csv_btn = tk.Button(self.export_frame, text="Esporta in CSV", command=self.esporta_csv)
        self.esporta_csv_btn.pack(pady=5)

        self.esporta_json_btn = tk.Button(self.export_frame, text="Esporta in JSON", command=self.esporta_json)
        self.esporta_json_btn.pack(pady=5)

        self.esporta_carte_btn = tk.Button(self.export_frame, text="Esporta Carte in CSV", command=self.esporta_carte_csv)
        self.esporta_carte_btn.pack(pady=5)

    def esporta_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Data", "Descrizione", "Importo", "Categoria"])
                for spesa in self.dati_spese:
                    writer.writerow([spesa["data"], spesa["descrizione"], spesa["importo"], spesa["categoria"]])

    def esporta_json(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, mode='w') as file:
                json.dump(self.dati_spese, file)

    def esporta_carte_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Numero Carta", "Nome", "Scadenza", "Saldo"])
                for carta in self.dati_carte:
                    writer.writerow([carta["numero"], carta["nome"], carta["scadenza"], carta["saldo"]])

    def esporta_obiettivi_json(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, mode='w') as file:
                json.dump(self.dati_obiettivi, file)

    def esporta_spese_e_obiettivi(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            dati_totali = {
                "spese": self.dati_spese,
                "obiettivi": self.dati_obiettivi
            }
            with open(file_path, mode='w') as file:
                json.dump(dati_totali, file)

    def esporta_carte_e_spese_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Numero Carta", "Nome", "Scadenza", "Saldo"])
                for carta in self.dati_carte:
                    writer.writerow([carta["numero"], carta["nome"], carta["scadenza"], carta["saldo"]])

                writer.writerow([])
                writer.writerow(["Data", "Descrizione", "Importo", "Categoria"])
                for spesa in self.dati_spese:
                    writer.writerow([spesa["data"], spesa["descrizione"], spesa["importo"], spesa["categoria"]])