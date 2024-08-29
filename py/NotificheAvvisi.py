import tkinter as tk
from tkinter import messagebox
import datetime


class NotificheAvvisi:
    def __init__(self, root, spese_data):
        self.root = root
        self.spese_data = spese_data
        self.avvisi_impostati = []
        self.avvisi_ricevuti = []
        self.notifica_frame = tk.Frame(root)
        self.notifica_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.notifica_frame, text="Notifiche e Avvisi", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.avviso_lista_frame = tk.Frame(self.notifica_frame)
        self.avviso_lista_frame.pack(fill=tk.BOTH, expand=True)

        self.avvisi_listbox = tk.Listbox(self.avviso_lista_frame)
        self.avvisi_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.avviso_lista_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.avvisi_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.avvisi_listbox.yview)

        self.avviso_entry_frame = tk.Frame(self.notifica_frame)
        self.avviso_entry_frame.pack(fill=tk.X)

        self.importo_label = tk.Label(self.avviso_entry_frame, text="Importo:")
        self.importo_label.grid(row=0, column=0, padx=10, pady=5)

        self.importo_entry = tk.Entry(self.avviso_entry_frame)
        self.importo_entry.grid(row=0, column=1, padx=10, pady=5)

        self.data_label = tk.Label(self.avviso_entry_frame, text="Data:")
        self.data_label.grid(row=1, column=0, padx=10, pady=5)

        self.data_entry = tk.Entry(self.avviso_entry_frame)
        self.data_entry.grid(row=1, column=1, padx=10, pady=5)

        self.aggiungi_avviso_btn = tk.Button(self.avviso_entry_frame, text="Aggiungi Avviso",
                                             command=self.aggiungi_avviso)
        self.aggiungi_avviso_btn.grid(row=2, column=0, columnspan=2, pady=10)

        self.rimuovi_avviso_btn = tk.Button(self.notifica_frame, text="Rimuovi Avviso", command=self.rimuovi_avviso)
        self.rimuovi_avviso_btn.pack(pady=10)

        self.controlla_avvisi_btn = tk.Button(self.notifica_frame, text="Controlla Avvisi",
                                              command=self.controlla_avvisi)
        self.controlla_avvisi_btn.pack(pady=10)

    def aggiungi_avviso(self):
        importo = self.importo_entry.get()
        data = self.data_entry.get()
        if importo and data:
            avviso = {"importo": float(importo), "data": data}
            self.avvisi_impostati.append(avviso)
            self.avvisi_listbox.insert(tk.END, f"Avviso per importo: {importo} € entro {data}")
            self.importo_entry.delete(0, tk.END)
            self.data_entry.delete(0, tk.END)

    def rimuovi_avviso(self):
        selezione = self.avvisi_listbox.curselection()
        if selezione:
            indice = selezione[0]
            self.avvisi_listbox.delete(indice)
            del self.avvisi_impostati[indice]

    def controlla_avvisi(self):
        data_corrente = datetime.date.today()
        for avviso in self.avvisi_impostati:
            data_avviso = datetime.datetime.strptime(avviso["data"], "%Y-%m-%d").date()
            if data_corrente >= data_avviso:
                importo_totale = sum(spesa["importo"] for spesa in self.spese_data if spesa["data"] <= avviso["data"])
                if importo_totale >= avviso["importo"]:
                    if avviso not in self.avvisi_ricevuti:
                        messagebox.showinfo("Avviso",
                                            f"Hai superato l'importo di {avviso['importo']} € entro la data {avviso['data']}")
                        self.avvisi_ricevuti.append(avviso)

    def visualizza_notifiche(self):
        notifiche_finestra = tk.Toplevel(self.root)
        notifiche_finestra.title("Notifiche Ricevute")

        notifiche_listbox = tk.Listbox(notifiche_finestra)
        notifiche_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for avviso in self.avvisi_ricevuti:
            notifiche_listbox.insert(tk.END, f"Superato importo: {avviso['importo']} € entro {avviso['data']}")

        chiudi_btn = tk.Button(notifiche_finestra, text="Chiudi", command=notifiche_finestra.destroy)
        chiudi_btn.pack(pady=10)

    def resetta_avvisi(self):
        self.avvisi_impostati.clear()
        self.avvisi_listbox.delete(0, tk.END)
        self.avvisi_ricevuti.clear()

    def carica_avvisi_da_file(self, file_path):
        with open(file_path, "r") as file:
            for linea in file:
                importo, data = linea.strip().split(",")
                avviso = {"importo": float(importo), "data": data}
                self.avvisi_impostati.append(avviso)
                self.avvisi_listbox.insert(tk.END, f"Avviso per importo: {importo} € entro {data}")

    def salva_avvisi_su_file(self, file_path):
        with open(file_path, "w") as file:
            for avviso in self.avvisi_impostati:
                file.write(f"{avviso['importo']},{avviso['data']}\n")

    def avviso_periodico(self, intervallo):
        importo_periodico = float(self.importo_entry.get())
        data_corrente = datetime.date.today()
        data_periodica = data_corrente + datetime.timedelta(days=intervallo)
        avviso = {"importo": importo_periodico, "data": data_periodica.strftime("%Y-%m-%d")}
        self.avvisi_impostati.append(avviso)
        self.avvisi_listbox.insert(tk.END, f"Avviso periodico: {importo_periodico} € entro {data_periodica}")
        self.importo_entry.delete(0, tk.END)
        self.data_entry.delete(0, tk.END)

    def avvisi_per_categoria(self, categoria):
        spese_categoria = [spesa for spesa in self.spese_data if spesa["categoria"] == categoria]
        importo_totale = sum(spesa["importo"] for spesa in spese_categoria)
        avviso = {"importo": importo_totale, "data": datetime.date.today().strftime("%Y-%m-%d")}
        self.avvisi_impostati.append(avviso)
        self.avvisi_listbox.insert(tk.END, f"Avviso per categoria {categoria}: {importo_totale} €")

    def visualizza_avvisi_categoria(self, categoria):
        avvisi_categoria_finestra = tk.Toplevel(self.root)
        avvisi_categoria_finestra.title(f"Avvisi per Categoria: {categoria}")

        avvisi_listbox = tk.Listbox(avvisi_categoria_finestra)
        avvisi_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for avviso in self.avvisi_impostati:
            spese_categoria = [spesa for spesa in self.spese_data if spesa["categoria"] == categoria]
            importo_totale = sum(spesa["importo"] for spesa in spese_categoria)
            avvisi_listbox.insert(tk.END, f"{categoria}: {importo_totale} € entro {avviso['data']}")

        chiudi_btn = tk.Button(avvisi_categoria_finestra, text="Chiudi", command=avvisi_categoria_finestra.destroy)
        chiudi_btn.pack(pady=10)
