import tkinter as tk
from tkinter import *

def abrir_nova_janela():
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Nova Janela")
    label = tk.Label(nova_janela, text="Esta é uma nova janela!")
    label.pack(padx=20, pady=20)


def show_selected_option():
    selected_option = selected_var.get()
    label.config(text=f"Você selecionou: {selected_option}")
# Criando a janela principal
root = tk.Tk()
root.geometry("200x300")

message_label = tk.Label(root, text="Endereço IP")
message_label.grid(column=0, row=0)

entry = tk.Entry(root, width=30)
entry.grid(column=0, row=1, padx=10, pady=10)


message_label = tk.Label(root, text="Máscara")
message_label.grid(column=0, row=2, padx=10, pady=10)


options = []
for i in range(1,33):
    options.append(i)

# Variável para armazenar a opção selecionada
selected_var = tk.StringVar()
selected_var.set(options[0])  # Define a opção padrão

# Cria o OptionMenu
option_menu = tk.OptionMenu(root, selected_var, *options)
option_menu.grid(column=0, row=3, padx=10, pady=10)


# Label para exibir a opção selecionada
label = tk.Label(root, text="")
label.grid(column=2, row=3, padx=10, pady=10)

message_label = tk.Label(root, text="Qntd. de hosts")
message_label.grid(column=0, row=4, padx=10, pady=10)

entry = tk.Entry(root, width=30)
entry.grid(column=0, row=5, padx=10, pady=10)

# Botão para abrir a nova janela
botao = Button(root, text="Let's Go!", width=15, height=1, command=abrir_nova_janela)
botao.grid(column=0, row=6, padx=10, pady=10)

# Loop principal da aplicação Tkinter
root.mainloop()