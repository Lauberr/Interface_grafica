import pyglet
import random
import tkinter as tk
from tkinter import ttk 


redes = ['192.168.10.0/24'
'10.20.30.0/24'
'172.16.0.0/16'
'192.0.2.0/24'
'198.51.100.0/24'
'10.0.0.0/8'
'172.31.0.0/16'
'192.168.1.0/24'
'203.0.113.0/24'
'172.20.0.0/16']

window = tk.Tk()
window.geometry('1280x960')
print(pyglet.window.Window())
window.title("teste")

table = ttk.Treeview(window, columns= ('Subrede', 'Qtd. de Estações', 'Endereços da sub-rede', 'Primeiro endereço', 'Broadcast', 'Máscara'), show='headings')
table.heading('Subrede', text='Subrede')
table.heading('Qtd. de Estações', text='Qtd. de Estações')
table.heading('Endereços da sub-rede', text='Endereços da sub-rede')
table.heading('Primeiro endereço', text='Primeiro endereço')
table.heading('Máscara', text='Máscara')
table.heading('Broadcast', text='Broadcast')

table.pack(fill='both',expand=True)

for i in range(20):
    table.insert(parent= '', index=0, values=(redes[random.randint(0,9)]))


window.mainloop()