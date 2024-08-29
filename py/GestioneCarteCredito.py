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

        def aggiungi_carta(self):
            numero_carta = self.numero_carta_entry.get()
            nome_carta = self.nome_carta_entry.get()
            data_scadenza = self.data_scadenza_entry.get()
            cvc = self.cvc_entry.get()
            saldo = self.saldo_entry.get()
            if numero_carta and nome_carta and data_scadenza and cvc and saldo:
                carta = {
                    "numero": numero_carta,
                    "nome": nome_carta,
                    "scadenza": data_scadenza,
                    "cvc": cvc,
                    "saldo": float(saldo),
                    "transazioni": []
                }
                self.carte_data.append(carta)
                self.carte_listbox.insert(tk.END, f"{nome_carta} - {numero_carta[-4:]}")
                self.numero_carta_entry.delete(0, tk.END)
                self.nome_carta_entry.delete(0, tk.END)
                self.data_scadenza_entry.delete(0, tk.END)
                self.cvc_entry.delete(0, tk.END)
                self.saldo_entry.delete(0, tk.END)

        def rimuovi_carta(self):
            selezione = self.carte_listbox.curselection()
            if selezione:
                indice = selezione[0]
                self.carte_listbox.delete(indice)
                del self.carte_data[indice]

        def visualizza_transazioni(self):
            selezione = self.carte_listbox.curselection()
            if selezione:
                indice = selezione[0]
                carta = self.carte_data[indice]
                transazioni_finestra = tk.Toplevel(self.root)
                transazioni_finestra.title(f"Transazioni per {carta['nome']}")

                transazioni_listbox = tk.Listbox(transazioni_finestra)
                transazioni_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                for transazione in carta["transazioni"]:
                    transazioni_listbox.insert(tk.END,
                                               f"{transazione['data']} - {transazione['descrizione']} - {transazione['importo']} €")

                chiudi_btn = tk.Button(transazioni_finestra, text="Chiudi", command=transazioni_finestra.destroy)
                chiudi_btn.pack(pady=10)

        def aggiungi_transazione(self):
            selezione = self.carte_listbox.curselection()
            if selezione:
                indice = selezione[0]
                carta = self.carte_data[indice]
                transazione_finestra = tk.Toplevel(self.root)
                transazione_finestra.title(f"Aggiungi Transazione a {carta['nome']}")

                descrizione_label = tk.Label(transazione_finestra, text="Descrizione:")
                descrizione_label.pack(pady=5)
                descrizione_entry = tk.Entry(transazione_finestra)
                descrizione_entry.pack(pady=5)

                importo_label = tk.Label(transazione_finestra, text="Importo:")
                importo_label.pack(pady=5)
                importo_entry = tk.Entry(transazione_finestra)
                importo_entry.pack(pady=5)

                def salva_transazione():
                    descrizione = descrizione_entry.get()
                    importo = importo_entry.get()
                    if descrizione and importo:
                        transazione = {
                            "descrizione": descrizione,
                            "importo": float(importo),
                            "data": datetime.date.today().strftime("%Y-%m-%d")
                        }
                        carta["transazioni"].append(transazione)
                        carta["saldo"] -= float(importo)
                        transazione_finestra.destroy()

                salva_btn = tk.Button(transazione_finestra, text="Salva", command=salva_transazione)
                salva_btn.pack(pady=10)

        def visualizza_saldo_carte(self):
            saldo_finestra = tk.Toplevel(self.root)
            saldo_finestra.title("Saldo delle Carte")

            saldo_listbox = tk.Listbox(saldo_finestra)
            saldo_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            for carta in self.carte_data:
                saldo_listbox.insert(tk.END, f"{carta['nome']} - Saldo: {carta['saldo']} €")

            chiudi_btn = tk.Button(saldo_finestra, text="Chiudi", command=saldo_finestra.destroy)
            chiudi_btn.pack(pady=10)

            def carica_carte_da_file(self, file_path):
                with open(file_path, "r") as file:
                    for linea in file:
                        numero, nome, scadenza, cvc, saldo = linea.strip().split(",")
                        carta = {
                            "numero": numero,
                            "nome": nome,
                            "scadenza": scadenza,
                            "cvc": cvc,
                            "saldo": float(saldo),
                            "transazioni": []
                        }
                        self.carte_data.append(carta)
                        self.carte_listbox.insert(tk.END, f"{nome} - {numero[-4:]}")

            def salva_carte_su_file(self, file_path):
                with open(file_path, "w") as file:
                    for carta in self.carte_data:
                        file.write(
                            f"{carta['numero']},{carta['nome']},{carta['scadenza']},{carta['cvc']},{carta['saldo']}\n")

            def aggiorna_dati_carta(self, indice, numero, nome, scadenza, cvc, saldo):
                carta = self.carte_data[indice]
                carta["numero"] = numero
                carta["nome"] = nome
                carta["scadenza"] = scadenza
                carta["cvc"] = cvc
                carta["saldo"] = saldo
                self.carte_listbox.delete(indice)
                self.carte_listbox.insert(indice, f"{nome} - {numero[-4:]}")

            def modifica_carta(self):
                selezione = self.carte_listbox.curselection()
                if selezione:
                    indice = selezione[0]
                    carta = self.carte_data[indice]

                    modifica_finestra = tk.Toplevel(self.root)
                    modifica_finestra.title(f"Modifica Carta {carta['nome']}")

                    numero_carta_label = tk.Label(modifica_finestra, text="Numero Carta:")
                    numero_carta_label.pack(pady=5)
                    numero_carta_entry = tk.Entry(modifica_finestra)
                    numero_carta_entry.insert(0, carta["numero"])
                    numero_carta_entry.pack(pady=5)

                    nome_carta_label = tk.Label(modifica_finestra, text="Nome:")
                    nome_carta_label.pack(pady=5)
                    nome_carta_entry = tk.Entry(modifica_finestra)
                    nome_carta_entry.insert(0, carta["nome"])
                    nome_carta_entry.pack(pady=5)

                    data_scadenza_label = tk.Label(modifica_finestra, text="Data Scadenza:")
                    data_scadenza_label.pack(pady=5)
                    data_scadenza_entry = tk.Entry(modifica_finestra)
                    data_scadenza_entry.insert(0, carta["scadenza"])
                    data_scadenza_entry.pack(pady=5)

                    cvc_label = tk.Label(modifica_finestra, text="CVC:")
                    cvc_label.pack(pady=5)
                    cvc_entry = tk.Entry(modifica_finestra)
                    cvc_entry.insert(0, carta["cvc"])
                    cvc_entry.pack(pady=5)

                    saldo_label = tk.Label(modifica_finestra, text="Saldo:")
                    saldo_label.pack(pady=5)
                    saldo_entry = tk.Entry(modifica_finestra)
                    saldo_entry.insert(0, carta["saldo"])
                    saldo_entry.pack(pady=5)

                    def salva_modifiche():
                        numero_carta = numero_carta_entry.get()
                        nome_carta = nome_carta_entry.get()
                        data_scadenza = data_scadenza_entry.get()
                        cvc = cvc_entry.get()
                        saldo = saldo_entry.get()
                        if numero_carta and nome_carta and data_scadenza and cvc and saldo:
                            self.aggiorna_dati_carta(indice, numero_carta, nome_carta, data_scadenza, cvc, float(saldo))
                            modifica_finestra.destroy()

                    salva_btn = tk.Button(modifica_finestra, text="Salva", command=salva_modifiche)
                    salva_btn.pack(pady=10)