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


#2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.


# import tkinter as tk
# from tkinter import messagebox

# def janela_info():
#    peças =int(pecas_hora.get())

#    if peças == "":
#     messagebox.showwarning("Aviso" , "Digite quantas peças são produzidas por hora")
#    else:
#      total = peças * 8
#      messagebox.showinfo("Calculado" ,  f"em 8 horas {total} , peças são produzidas ")


# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("300x300")
# janela.configure(bg="red")


# lbl_peças= tk.Label(janela, text="Digite quantas peças são produzidas por hora: ")
# lbl_peças.grid(row=0, column=0, pady=60, padx=10) 

# pecas_hora= tk.Entry(janela, font=("Arial", 12))
# pecas_hora.grid(row=1, column=0, pady=10, padx=10)

# btn_Entre= tk.Button(janela, text="calcular" , command= janela_info)
# btn_Entre.grid(row=3, column=0, pady=10, padx=10)

# janela.mainloop()

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.


import tkinter as tk
from tkinter import messagebox

def janela_info():
   pressaobar =int(pressao_bar.get())

   if pressaobar == "":
    messagebox.showwarning("Aviso" ,"Digite a pressao em Bar")
   else:
     total = pressaobar * 14.5
     messagebox.showinfo("Calculado" ,  f"em 8 horas {total} , peças são produzidas ")


janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("300x300")
janela.configure(bg="red")


lbl_peças= tk.Label(janela, text="Digite quantas peças são produzidas por hora: ")
lbl_peças.grid(row=0, column=0, pady=60, padx=10) 

pecas_hora= tk.Entry(janela, font=("Arial", 12))
pecas_hora.grid(row=1, column=0, pady=10, padx=10)

btn_Entre= tk.Button(janela, text="calcular" , command= janela_info)
btn_Entre.grid(row=3, column=0, pady=10, padx=10)

janela.mainloop()
































# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
#aritmética simples delas.

# import tkinter as tk
# from tkinter import messagebox

# def janela_notas():
#    peça1 = int(peca_um.get())
#    peça2 = int(peca_dois.get())
#    peça3 = int(peca_tres.get())

#    if peça1 == "" and peça2 == "" and peça3 == "":
#       messagebox.showwarning("Digite uma nota para cada peça")
#    else:
#       soma = peça1 + peça2 + peça3
#       total = soma / 3 
#       messagebox.showinfo("Calculado" ,  f"A média das peças é de: {total}  ")
      

# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("600x600")
# janela.configure(bg="green")


# lbl_peça_um = tk.Label(janela, text="Dê uma nota de 0 a 10 para primeira peça")
# lbl_peça_um.grid(row=0, column=0, pady=60, padx=10)

# peca_um = tk.Entry(janela, font=("Arial", 12))
# peca_um.grid(row=0, column=1, pady=10, padx=10)

# lbl_peca_dois = tk.Label(janela, text="Dê uma nota de 0 a 10  para segunda peça")
# lbl_peca_dois.grid(row=1, column=0, pady=10, padx=10)

# peca_dois = tk.Entry(janela, font=("Arial", 12))
# peca_dois.grid(row=1, column=1, pady=10, padx=10)

# lbl_peca_tres = tk.Label(janela, text="Dê uma nota de 0 a 10 para terceira peça")
# lbl_peca_tres.grid(row=2, column=0, pady=10, padx=10)

# peca_tres= tk.Entry(janela, font=("Arial", 12))
# peca_tres.grid(row=2, column=1, pady=10, padx=10)


# btn_Entre= tk.Button(janela, text="Entre" , command= janela_notas)
# btn_Entre.grid(row=4, column=0, pady=10, padx=10)

# janela.mainloop()
