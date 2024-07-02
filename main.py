import tkinter as tk
from tkinter import *
import math
import ipaddress



def calcular_subredes(ip, quantidade_subredes):
    bits_subrede = math.ceil(math.log2(quantidade_subredes)) # Nessa linha o ".ceil" arredonda o valor enquanto o ".log2" é uma função que calucla o log2 da quantidade de subredes.
    nova_prefix = ip.prefixlen + bits_subrede # O ".prefixlen" retorna o tamanho do endereço IP, e o nova_prefix é o endereço IP com o numero adicional de bits para as subredes.
    
    if nova_prefix > 32:
        raise ValueError("Número de sub-redes é muito grande para o endereço IP fornecido.")
    
    subredes = list(ip.subnets(new_prefix=nova_prefix)) # gera uma lista de sub-redes a partir do endereço IP fornecido.
    return subredes


def gerar_enderecos_subredes(subredes):
    enderecos = []
    for subrede in subredes:
        primeiro_endereco = subrede.network_address # Retorna o primeiro endereço IP da sub-rede.
        ultimo_endereco = subrede.broadcast_address # Retorna o ultimo endereço IP da sub-rede.
        mascara = subrede.netmask # Retorna a mascara de endereço da sub-rede.
        enderecos.append((primeiro_endereco, ultimo_endereco, mascara))
    return enderecos


class Table: # Classe para geração da tabela da segunda página.
    def __init__(self, root, headers, data):
        headerlen = len(headers)
        total_rows = len(data)
        total_columns = len(headers) # Essas três linhas geram a tabela com cabeçalho e a quantidade de linhas e colunas.
        

        # Criando um frame para a tabela dentro da pagina.
        self.canvas = tk.Canvas(root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        

        # Adicionando uma barra de rolagem vertical.
        self.scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        

        # Conectando a barra de rolagem ao canvas.
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        

        # Frame que conterá a tabela.
        self.table_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.table_frame, anchor=tk.NW)
        

        # Inserindo cabeçalhos na primeira linha da tabela.
        for j in range(headerlen):
            self.e = Entry(self.table_frame, width=16, fg='blue', font=('Arial', 10, 'bold'))
            self.e.grid(row=0, column=j)
            self.e.insert(END, headers[j])
        

        # Inserindo dados.
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(self.table_frame, width=16, fg='black', font=('Arial', 10))
                self.e.grid(row=i+1, column=j)
                self.e.insert(END, data[i][j])


def abrir_nova_janela(): # Função para gerar uma nova pagina na ação do clique de um botão.
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Resultados das Sub-redes")
    
    ip_address = ip_entry.get()
    mask = selected_var.get()
    quantidade_subredes = int(hosts_entry.get()) # Essas três linhas armazenam os valores digitados nos entrys e selects de IP, máscara e Qntd. de hosts.
    
    try:
        ip = ipaddress.ip_network(f"{ip_address}/{mask}", strict=False) # Cria um objeto de rede IP usando o endereço IP ip_address e a máscara mask.
        subredes = calcular_subredes(ip, quantidade_subredes) # Chama a função calcular_subredes para calcular as sub-redes pelo objeto de rede ip e pela na quantidade desejada de sub-redes quantidade_subredes.
        enderecos = gerar_enderecos_subredes(subredes) # Chama a função gerar_enderecos_subredes para criar uma lista de cada sub-rede calculada.
        
        lst = []
        for i, (primeiro, ultimo, mascara) in enumerate(enderecos, start=1):
            lst.append([i, str(ip), quantidade_subredes, str(primeiro), str(primeiro + 1), str(ultimo), str(mascara)]) # Insere os dados da subrede na tabela para que sejam inseridos posteriormente na tabela.
        
        headers = ['ID', 'Subrede', 'Qtd. Estações', 'End. subrede', 
                   '1° endereço', 'Broadcast', 'Máscara']

        Table(nova_janela, headers, lst) # Gera efetivamente a tabela

        nova_janela.update_idletasks()
        nova_janela.geometry(f"822x200") 

    except ValueError as e:
        tk.Label(nova_janela, text=f"Erro: {str(e)}").pack(padx=20, pady=10)
    except Exception as e:
        tk.Label(nova_janela, text=f"Erro: Endereço IP inválido ou outro erro.").pack(padx=20, pady=10)


def validate_integer(P):
    if P.isdigit() or P == "": # Valida se o valor digitado é ou não um inteiro
        return True
    else:
        return False


root = tk.Tk()
root.geometry("210x300")

vcmd = (root.register(validate_integer), '%P')

message_label = tk.Label(root, text="Endereço IP")
message_label.grid(column=0, row=0)

ip_entry = tk.Entry(root, width=30)
ip_entry.grid(column=0, row=1, padx=10, pady=10)

message_label = tk.Label(root, text="Máscara")
message_label.grid(column=0, row=2, padx=10, pady=10)

options = list(range(1, 33))

selected_var = tk.StringVar()
selected_var.set(options[0])

option_menu = tk.OptionMenu(root, selected_var, *options)
option_menu.grid(column=0, row=3, padx=10, pady=10)

message_label = tk.Label(root, text="Qntd. de sub-redes")
message_label.grid(column=0, row=4, padx=10, pady=10)

hosts_entry = tk.Entry(root, width=30, validate="key", validatecommand=vcmd)
hosts_entry.grid(column=0, row=5, padx=10, pady=10)

botao = Button(root, text="Let's Go!", width=15, height=1, command=abrir_nova_janela)
botao.grid(column=0, row=6, padx=10, pady=10)

root.mainloop() # Essas ultimas linhas, geram o layout da pagina de entrada de dados.
