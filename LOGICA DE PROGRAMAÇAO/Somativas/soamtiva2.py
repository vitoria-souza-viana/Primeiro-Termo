# Somativa 2 09/06/26


#1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox

# def janela_info():
#     nome = nome_operador.get()
#     turno = turno_operador.get()

#     if nome == "":
#         messagebox.showwarning("Aviso" , "Digite seu nome")

#     else:
#         messagebox.showinfo("Bem vindo", f"Operador {nome} ,Registrado no Turno {turno}, Boa jornada!")

#     if turno == "":
#         messagebox.showwarning("Digite turno A; B ou C")

#     else:
#        messagebox.showwarning("Bem-Vindo(A)")


# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("300x300")
# janela.configure(bg="red")


# lbl_Entre = tk.Label(janela, text="Digite seu nome ")
# lbl_Entre.grid(row=0, column=0, pady=60, padx=10)

# nome_operador= tk.Entry(janela, font=("Arial", 12))
# nome_operador.grid(row=0, column=1, pady=10, padx=10)

# btn_Entre= tk.Button(janela, text="Entre" , command= janela_info)
# btn_Entre.grid(row=3, column=0, pady=10, padx=10)

# turno_operador = tk.Entry(janela, font=("Arial", 12))
# turno_operador.grid(row=1, column=1, pady=10, padx=10)

# lbl_operador = tk.Label(janela, text="Digite seu turno")
# lbl_operador.grid(row=1, column=0, pady=10, padx=10)


# janela.mainloop()


# Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.


import tkinter as tk
from tkinter import messagebox

def janela_info():
   peças = pecas_hora.get()

   if peças == "":
    messagebox.showwarning("Aviso" , "Digite quantas peças são produzidas por hora")
   else:
     total = total * 8
     messagebox.showinfo(f"em 8 horas {total} , peças são produzidas ")


janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("300x300")
janela.configure(bg="red")


lbl_peças= tk.Label(janela, text="Digite quantas peças são produzidas por hora: ")
lbl_peças.grid(row=0, column=0, pady=60, padx=10) 

pecas_hora= tk.Entry(janela, font=("Arial", 12))
pecas_hora.grid(row=1, column=0, pady=10, padx=10)
# btn_Entre= tk.Button(janela, text="Entre" , command= janela_info)
# btn_Entre.grid(row=3, column=0, pady=10, padx=10)

turno_operador = tk.Entry(janela, font=("Arial", 12))
turno_operador.grid(row=1, column=1, pady=10, padx=10)

lbl_operador = tk.Label(janela, text="Digite seu turno")
lbl_operador.grid(row=1, column=0, pady=10, padx=10)

janela.mainloop()
