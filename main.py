from tkinter import *
from jogador import Jogador
from desafios import obter_desafio

jogador = Jogador()
desafio_atual = None
categoria_atual = None


# ---------------- lógica ---------------- #

def descobrir_categoria(casa):

    if casa < 100:
        return "matematica"
    elif casa < 200:
        return "logica"
    else:
        return "sequencia"


def cor_categoria(cat):

    if cat == "matematica":
        return "#4CAF50"
    elif cat == "logica":
        return "#2196F3"
    else:
        return "#FF9800"


def buscar_pergunta():

    global desafio_atual, categoria_atual

    casa = int(entry_casa.get())

    categoria_atual = descobrir_categoria(casa)

    nivel = jogador.nivel[categoria_atual]

    desafio_atual = obter_desafio(categoria_atual, nivel)

    jogador.iniciar_tempo()

    pergunta_label.config(
        text=desafio_atual["pergunta"],
        fg=cor_categoria(categoria_atual)
    )

    status_categoria.config(
        text=f"Categoria: {categoria_atual.upper()} | Nível {nivel}"
    )

    atualizar_status()


def verificar():

    resposta = entry_resposta.get().strip().lower()
    correta = desafio_atual["resposta"].strip().lower()

    if resposta == correta:

        jogador.acertou(categoria_atual)
        feedback_label.config(text="🔥 ACERTOU! Evolução desbloqueada!")

    else:

        jogador.errou(categoria_atual)
        feedback_label.config(text=f"❌ Errado! Resposta: {correta}")

    atualizar_status()
    entry_resposta.delete(0, END)


def atualizar_status():

    mat = jogador.pontos["matematica"]
    log = jogador.pontos["logica"]
    seq = jogador.pontos["sequencia"]

    texto = f"""
🧠 STATUS DO JOGADOR

🟩 Matemática: Nível {jogador.nivel['matematica']} | Pontos {mat}
🟦 Lógica: Nível {jogador.nivel['logica']} | Pontos {log}
🟨 Sequência: Nível {jogador.nivel['sequencia']} | Pontos {seq}

✔ Acertos: {jogador.acertos}
❌ Erros: {jogador.erros}
"""

    status_label.config(text=texto)


# ---------------- interface ---------------- #

janela = Tk()
janela.title("Logic Quest")
janela.geometry("650x700")
janela.config(bg="#121212")


# TÍTULO
titulo = Label(
    janela,
    text="LOGIC QUEST",
    font=("Arial", 26, "bold"),
    fg="white",
    bg="#121212"
)
titulo.pack(pady=10)


# CARD CASA
frame_casa = Frame(janela, bg="#1e1e1e", padx=10, pady=10)
frame_casa.pack(pady=10)

Label(frame_casa, text="🏠 Número da Casa", fg="white", bg="#1e1e1e").pack()

entry_casa = Entry(frame_casa, font=("Arial", 14), width=10, justify="center")
entry_casa.pack(pady=5)

Button(
    frame_casa,
    text="🎲 Buscar Desafio",
    command=buscar_pergunta,
    bg="#03DAC5",
    fg="black",
    font=("Arial", 12, "bold"),
    padx=10
).pack()


# STATUS CATEGORIA
status_categoria = Label(
    janela,
    text="",
    font=("Arial", 14, "bold"),
    fg="#03DAC5",
    bg="#121212"
)
status_categoria.pack(pady=10)


# CARD PERGUNTA
frame_pergunta = Frame(janela, bg="#1e1e1e", padx=15, pady=15)
frame_pergunta.pack(pady=10)

pergunta_label = Label(
    frame_pergunta,
    text="",
    font=("Arial", 16),
    fg="white",
    bg="#1e1e1e",
    wraplength=500,
    justify="center"
)
pergunta_label.pack()


# RESPOSTA
entry_resposta = Entry(janela, font=("Arial", 14), justify="center")
entry_resposta.pack(pady=10)


Button(
    janela,
    text="🚀 ENVIAR RESPOSTA",
    command=verificar,
    bg="#BB86FC",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=10
).pack(pady=5)


# FEEDBACK
feedback_label = Label(
    janela,
    text="",
    font=("Arial", 14, "bold"),
    fg="#FFD54F",
    bg="#121212"
)
feedback_label.pack(pady=10)


# STATUS
status_label = Label(
    janela,
    text="",
    font=("Consolas", 11),
    fg="white",
    bg="#121212",
    justify=LEFT
)
status_label.pack(pady=10)


atualizar_status()

janela.mainloop()