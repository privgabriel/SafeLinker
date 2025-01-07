import tkinter as tk
from tkinter import messagebox
import webbrowser

URLS_SURFACE = {
    "who.is": "https://who.is/",
    "registro.br": "https://registro.br/",
    "Hacking Database": "https://www.exploit-db.com/google-hacking-database",
    "Dorks": "https://gbhackers.com/latest-google-dorks-list/",
    "Dorks-Tutorial": "https://www.recordedfuture.com/threat-intelligence-101/threat-analysis-techniques/google-dorks",
    "Shodan": "https://www.shodan.io/",
    "Censys": "https://censys.io/",
    "Wayback Machine": "https://archive.org/web/",
    "crt.sh": "https://crt.sh/",
}

URLS_DB_SURFACE = {
    "Dehashed": "https://dehashed.com/",
    "Leaked-DataBase": "https://www.leakedsource.ru/",
    "Pwned": "https://haveibeenpwned.com/",
    "Snusbase": "https://snusbase.com/",
}

URLS_ONION = {
    "Ahmia": "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/",
    "BreachForums": "http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/",
    "Leaked Password Database": "http://breachdb7r5fusv54wbqgfrmtqcle647ybi7jyi2b2btqyraioox3wid.onion/LeakedPass",
}

def open_url(url: str):
    try:
        webbrowser.open_new(url)
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir a URL. Detalhes: {e}")

def create_buttons(frame, urls):
    for name, url in urls.items():
        button = tk.Button(frame, text=name, font=("Helvetica", 10, "bold"), bg="#7b1fa2", fg="white", relief="flat", command=lambda u=url: open_url(u))
        button.pack(fill="x", pady=2, padx=5)

def setup_ui():
    root = tk.Tk()
    root.title("URL ORGANIZER")
    root.geometry("400x600")
    root.configure(bg="#f7f3f9")

    frame_surface = tk.LabelFrame(root, text="Surface URLs", bg="#f7f3f9", fg="#7b1fa2", font=("Helvetica", 12, "bold"))
    frame_surface.pack(fill="both", expand=True, padx=10, pady=5)
    create_buttons(frame_surface, URLS_SURFACE)

    frame_db_surface = tk.LabelFrame(root, text="Database URLs", bg="#f7f3f9", fg="#7b1fa2", font=("Helvetica", 12, "bold"))
    frame_db_surface.pack(fill="both", expand=True, padx=10, pady=5)
    create_buttons(frame_db_surface, URLS_DB_SURFACE)

    frame_onion = tk.LabelFrame(root, text="Onion URLs", bg="#f7f3f9", fg="#7b1fa2", font=("Helvetica", 12, "bold"))
    frame_onion.pack(fill="both", expand=True, padx=10, pady=5)
    create_buttons(frame_onion, URLS_ONION)

    root.mainloop()

setup_ui()
