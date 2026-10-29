import tkinter as tk
from tkinter import ttk, messagebox
from urllib.parse import urlparse
import webbrowser


def normalize_game_url(raw: str) -> str:
    raw = raw.strip()
    if not raw:
        raise ValueError("Cole o link de uma experiência Roblox.")
    if not raw.startswith(("https://", "http://")):
        raw = "https://" + raw
    parsed = urlparse(raw)
    if parsed.netloc.lower() not in {"roblox.com", "www.roblox.com", "web.roblox.com"}:
        raise ValueError("Use um link do domínio roblox.com.")
    if not parsed.path.startswith(("/games/", "/share")):
        raise ValueError("O link deve ser de uma experiência Roblox (/games/...).")
    return raw


class VoidBotApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("VoidBot Roblox")
        root.geometry("640x520")
        root.minsize(560, 470)
        root.configure(bg="#101522")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#101522", foreground="#eef2ff",
                        font=("Segoe UI", 10))
        style.configure("Title.TLabel", background="#101522", foreground="#a5b4fc",
                        font=("Segoe UI", 20, "bold"))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8)
        style.configure("TEntry", padding=7)

        frame = ttk.Frame(root, padding=18)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="VOIDBOT ROBLOX", style="Title.TLabel").pack(anchor="w")
        ttk.Label(frame, text="Menu auxiliar para abrir perfis e experiências").pack(
            anchor="w", pady=(3, 16))

        ttk.Label(frame, text="Nome de usuário Roblox").pack(anchor="w")
        self.username = tk.StringVar()
        ttk.Entry(frame, textvariable=self.username).pack(fill="x", pady=(4, 8))
        ttk.Button(frame, text="Abrir busca de usuário",
                   command=self.open_profile_search).pack(anchor="w", pady=(0, 14))

        ttk.Label(frame, text="Link da experiência Roblox").pack(anchor="w")
        self.game_url = tk.StringVar()
        ttk.Entry(frame, textvariable=self.game_url).pack(fill="x", pady=(4, 8))
        ttk.Button(frame, text="Abrir experiência",
                   command=self.open_game).pack(anchor="w")

        ttk.Label(frame, text="Registro").pack(anchor="w", pady=(16, 5))
        self.log_box = tk.Text(frame, height=8, bg="#080c14", fg="#c7d2fe",
                               insertbackground="white", relief="flat", wrap="word",
                               font=("Consolas", 9))
        self.log_box.pack(fill="both", expand=True)
        self.log("Pronto. Este menu abre páginas e links; não automatiza pedidos de amizade.")
        self.log("O NPC precisa ser instalado em uma experiência que você possa editar.")

    def log(self, text: str):
        self.log_box.insert("end", text + "\n")
        self.log_box.see("end")

    def open_profile_search(self):
        name = self.username.get().strip()
        if not name or any(ch.isspace() for ch in name):
            messagebox.showerror("Nome inválido", "Digite um nome de usuário sem espaços.")
            return
        url = "https://www.roblox.com/search/users?keyword=" + name
        webbrowser.open(url)
        self.log(f"Abrindo busca de usuário: {name}")

    def open_game(self):
        try:
            url = normalize_game_url(self.game_url.get())
        except ValueError as exc:
            messagebox.showerror("Link inválido", str(exc))
            return
        webbrowser.open(url)
        self.log("Abrindo experiência: " + url)
        self.log("Se solicitado, confirme a abertura do aplicativo Roblox.")


if __name__ == "__main__":
    root = tk.Tk()
    VoidBotApp(root)
    root.mainloop()
