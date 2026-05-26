# Interface gráfica com TKINTER

# componentes principais (Widgets)
# tk: janela principal
# label: texto ou rotulo
# button: um botaõ cliclavel
# entry: um campo de entrada de texto

import tkinter as tk
from tkinter import messagebox

# 1. Criar a janela principal
janela = tk.Tk()
janela.title("Minha primeira janela GUI")
janela.geometry("400x200") #largura por altura

# 2. criar a função que o botão irá executar
def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Você cliclou no botão s2")

# 3. Criar componentes
lbl_titulo_pagina = tk.Label(janela, text="Bem vindo a aula de interface grafica", font=("Arial", 14, "bold"))
btn_clique_pagina = tk.Button(janela, text="Clique aqui", font=("Arial", 14), bg="#ac1111", fg="White", command=mostrar_mensagem )
btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Italico", 14), bg="#e74c3c", fg="white", command=janela.destroy )
# 4. Posicionar os componentes na janela 
lbl_titulo_pagina.pack(pady=20) #pady adiciona um espaçamento vertical
btn_clique_pagina.pack(pady=10)



# 5. rodar o loop da interface 
janela.mainloop()
