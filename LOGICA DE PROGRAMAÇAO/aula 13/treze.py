import tkinter as tk
from tkinter import messagebox

def janela_bemvvindo():   #serve para buscar informação na caixa de texto.
    nome= nome_usuario.get()
    idade= idade_usuario.get()


    if nome == "":
        messagebox.showwarning("Aviso" , "Digite seu nome :)")
    else:
        messagebox.showinfo("bem vindo" , f"Olá usuario, {nome} - seja bem-vindo a nosso sistema")

    if idade == "":
        messagebox.showwarning("Digite sua idade")
   
    else:
        messagebox.showinfo("Bem vindo")

#janela
janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("300x300")
janela.configure(bg="pink")

# componentes
lbl_mensagem = tk.Label(janela, text="Digite seu nome :)")
lbl_mensagem.grid(row=0, column=0, pady=60, padx=10)

nome_usuario = tk.Entry(janela, font=("Arial", 12))
nome_usuario.grid(row=0, column=1, pady=10, padx=10)

btn_mensagem = tk.Button(janela, text="Mensagem" , command= janela_bemvvindo)
btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

idade_usuario= tk.Entry(janela, font=("Arial", 12))
idade_usuario.grid(row=3, column=1, pady=10, padx=10)

lbl_idade = tk.Label(janela, text="Digite sua idade:)")
lbl_idade.grid(row=3, column=0, pady=60, padx=10)

# Rodar interface
janela.mainloop()
