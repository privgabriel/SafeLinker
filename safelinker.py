import tkinter as tk
from tkinter import messagebox
import webbrowser

urls_surface = {
    "who.is": "https://who.is/",
    "registro.br": "https://registro.br/",
    "Hacking Database": "https://www.exploit-db.com/google-hacking-database",
    "Dorks": "https://gbhackers.com/latest-google-dorks-list/",
    "Dorks-Tutorial": "https://www.recordedfuture.com/threat-intelligence-101/threat-analysis-techniques/google-dorks",
    "Shodan": "https://www.shodan.io/",
    "Censys": "https://censys.io/",
}

urls_db_surface = {
    "Dehashed": "https://dehashed.com/",
    "Leaked-DataBase": "https://www.leakedsource.ru/",
    "Pwned": "https://haveibeenpwned.com/",
    "Snusbase": "https://snusbase.com/",
}

urls_onion = {
    "Ahmia": "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/",
    "BreachForums": "http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/",
    "Leaked Password Database": "http://breachdb7r5fusv54wbqgfrmtqcle647ybi7jyi2b2btqyraioox3wid.onion/LeakedPass",
}


def open_url(url):
    webbrowser.open_new(url)


root = tk.Tk()
root.title("URLs Organizator")
root.geometry("400x600")
root.configure(bg="#f7f3f9")

btn_font = ("Helvetica", 10, "bold")
btn_color = "#7b1fa2"  
btn_fg = "white"


def create_buttons(frame, urls):
    for name, url in urls.items():
        button = tk.Button(frame, text=name, font=btn_font, bg=btn_color, fg=btn_fg, relief="flat", command=lambda u=url: open_url(u))
        button.pack(fill="x", pady=2, padx=5)

frame_surface = tk.LabelFrame(root, text="Surface URLs", bg="#f7f3f9", fg=btn_color, font=("Helvetica", 12, "bold"))
frame_surface.pack(fill="both", expand=True, padx=10, pady=5)
create_buttons(frame_surface, urls_surface)

frame_db_surface = tk.LabelFrame(root, text="Database URLs", bg="#f7f3f9", fg=btn_color, font=("Helvetica", 12, "bold"))
frame_db_surface.pack(fill="both", expand=True, padx=10, pady=5)
create_buttons(frame_db_surface, urls_db_surface)

frame_onion = tk.LabelFrame(root, text="Onion URLs", bg="#f7f3f9", fg=btn_color, font=("Helvetica", 12, "bold"))
frame_onion.pack(fill="both", expand=True, padx=10, pady=5)
create_buttons(frame_onion, urls_onion)

footer = tk.Label(root, text="Desenvolvido com ❤ em Python", bg="#f7f3f9", fg="#7b1fa2", font=("Helvetica", 10))
footer.pack(side="bottom", pady=10)

root.mainloop()
