import tkinter as tk
from _tkinter import messagebox

def janela_Bemvindo():
    alunos= aluno_usuario.get() 
    comunidade_geral= comunidade_geral_usuario.get()
    nome= nome_usuario.get()

    if nome == "":
        messagebox.showwaring("Digite seu nome")
    else:
        messagebox.showinf("Bem-Vindo (A) {nome}")
       

lbl_escolha= tk.Label("Digite 1 para Alunos ou 2 para Comunidade Geral.")
lbl_escolha.grid(row=0, column=0, pady=10, padx=10)
if lbl_escolha == 1:            
    lbl_categoria=tk.Label("Digite 1 para livros Raros e 2 para livros Normais")
    lbl_categoria.grid(row=1, column=0, pady=10, padx=10)

def janela_dias():
    






janela.mainloop()