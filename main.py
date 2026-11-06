"""Relógio digital personalizado do Maurício."""

from datetime import datetime
import tkinter as tk

NOME_USUARIO = "Maurício"

DIAS = (
    "segunda-feira", "terça-feira", "quarta-feira",
    "quinta-feira", "sexta-feira", "sábado", "domingo",
)

MESES = (
    "janeiro", "fevereiro", "março", "abril",
    "maio", "junho", "julho", "agosto",
    "setembro", "outubro", "novembro", "dezembro",
)

TEMAS = {
    "escuro": {
        "fundo": "#211C20",
        "principal": "#9627E8",
        "secundario": "#8A3AC0",
        "icone": "#F4CB50",
    },
    "claro": {
        "fundo": "#F8F5FB",
        "principal": "#7118C7",
        "secundario": "#6F4D85",
        "icone": "#E2A700",
    },
}


def formatar_data(agora: datetime) -> str:
    dia = DIAS[agora.weekday()]
    mes = MESES[agora.month - 1]
    return f"{dia}, {agora.day} de {mes} de {agora.year}"


def formatar_hora(agora: datetime) -> str:
    return agora.strftime("%H:%M:%S")


class RelogioApp:
    def __init__(self, janela: tk.Tk) -> None:
        self.janela = janela
        self.tema_atual = "escuro"

        janela.title(f"Relógio de {NOME_USUARIO}")
        janela.geometry("600x320")
        janela.minsize(550, 320)

        self.conteudo = tk.Frame(janela)
        self.conteudo.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
        )

        self.botao_tema = tk.Button(
            self.conteudo,
            command=self.alternar_tema,
            font=("Segoe UI Symbol", 27),
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2",
            padx=12,
        )
        self.botao_tema.pack(pady=(0, 14))

        self.saudacao = tk.Label(
            self.conteudo,
            text=f"Olá, {NOME_USUARIO}!",
            font=("Segoe UI", 16),
        )
        self.saudacao.pack(pady=(0, 8))

        self.data = tk.Label(
            self.conteudo,
            font=("Segoe UI", 12),
        )
        self.data.pack(pady=(0, 12))

        self.hora = tk.Label(
            self.conteudo,
            font=("Segoe UI", 62, "bold"),
        )
        self.hora.pack()

        self.aplicar_tema()
        self.atualizar_relogio()

    def aplicar_tema(self) -> None:
        cores = TEMAS[self.tema_atual]

        self.janela.configure(bg=cores["fundo"])
        self.conteudo.configure(bg=cores["fundo"])

        for etiqueta in (self.saudacao, self.data):
            etiqueta.configure(
                bg=cores["fundo"],
                fg=cores["secundario"],
            )

        self.hora.configure(
            bg=cores["fundo"],
            fg=cores["principal"],
        )

        self.botao_tema.configure(
            text="☾" if self.tema_atual == "escuro" else "☀",
            bg=cores["fundo"],
            fg=cores["icone"],
            activebackground=cores["fundo"],
            activeforeground=cores["principal"],
        )

    def alternar_tema(self) -> None:
        if self.tema_atual == "escuro":
            self.tema_atual = "claro"
        else:
            self.tema_atual = "escuro"

        self.aplicar_tema()

    def atualizar_relogio(self) -> None:
        agora = datetime.now()

        self.data.configure(
            text=formatar_data(agora)
        )
        self.hora.configure(
            text=formatar_hora(agora)
        )

        # Sincroniza a atualização com a virada do segundo.
        intervalo = 1000 - agora.microsecond // 1000

        self.janela.after(
            intervalo,
            self.atualizar_relogio,
        )


def main() -> None:
    janela = tk.Tk()
    RelogioApp(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()