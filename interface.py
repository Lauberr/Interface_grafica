import tkinter as tk
from tkinter import *

class Table:
    def __init__(self, root):
        # Inserindo cabeçalhos na primeira linha da tabela
        for j in range(headerlen):
            self.e = Entry(root, width=12, fg='blue', font=('Arial', 16, 'bold'))
            self.e.grid(row=0, column=j)
            self.e.insert(END, headers[j])
        
        # Inserindo dados
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=12, fg='black', font=('Arial', 16))
                self.e.grid(row=i+1, column=j)
                self.e.insert(END, lst[i][j])

def abrir_nova_janela():
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Nova Janela")
    label = tk.Label(nova_janela, text="Esta é uma nova janela!")
    label.pack(padx=20, pady=20)

# Dados da tabela
lst = [
    (1, 'Subrede', 'Qtd. de end', 'Intervalo', '1 end valido', 'Ult. end valido', 'Mascara'),
    (2, 'Subrede', 'Qtd. de end', 'Intervalo', '1 end valido', 'Ult. end valido', 'Mascara'),
    (3, 'Subrede', 'Qtd. de end', 'Intervalo', '1 end valido', 'Ult. end valido', 'Mascara'),
    (4, 'Subrede', 'Qtd. de end', 'Intervalo', '1 end valido', 'Ult. end valido', 'Mascara'),
    (5, 'Subrede', 'Qtd. de end', 'Intervalo', '1 end valido', 'Ult. end valido', 'Mascara')
]

headers = ['ID' ,'Subrede', 'Qtd. Estações', 'End. subrede', 
                   '1° endereço', 'Broadcast', 'Máscara']

# Número total de linhas e colunas na lista
total_rows = len(lst)
total_columns = len(lst[0])
headerlen = len(headers)

# Criando a janela principal
root = Tk()

# Botão para abrir a nova janela
botao = Button(root, text="Clica aqui", width=15, height=1, command=abrir_nova_janela)
botao.grid(column=3, row=total_rows + 2)

# Instanciando a tabela
t = Table(root)

# Loop principal da aplicação Tkinter
root.mainloop()
