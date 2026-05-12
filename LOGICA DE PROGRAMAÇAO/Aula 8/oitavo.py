# Exercícios de Programação Python: "O Caça-Erros"
# 1. O problema da idade
#Erro 
# idade = input("Digite sua idade:")
# if idade >= 18:
#     print("Você é maior de idade")
   # Corrigido 
# idade = int(input("Digite sua idade"))
# if idade >= 18:
#     print("Você é maior de idade")
# else: 
#     print("Você é menor de idade")

# 2. A Escrita Fiel
# nome = "Mariana"
# print("Seja bem-vinda, nome!")
 #Corrigido
# nome= input("Digite seu nome")
# print("Seja bem-vindo (a):", nome ,"!")

# 3. Falta de Espaço
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

#Corrigido
# numero= 10
# if numero >5:
#     print("O Numero é maior que cinco")

    #Melhorado
#     numero= int(input("Digite o Numero"))
# if numero >5:
#     print("O Numero é maior que 5")
# else:
#     print("O numero é menor ou igual a cinco")

# 4. Esquecimento Fatal
# usuario="aluno123"
# if usuario == "aluno123"
# print("login realizado com sucesso.")
#Corrigido
# usuario= "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso")
#melhorado
# usuario= input("Digite seu usuario")
# if usuario == "aluno123":
#       print("Login realizado com sucesso")
# else:
#       print("Acesso negado.")

# 5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")

#Corrigido
# clima = input(" ensolarado \ chuvoso ")
# if clima == "chuvoso":
#     print("Leve um guarda chuva!")

# #Melhorado
# clima = input(" ensolarado \ chuvoso ")
# if clima == "chuvoso":
#     print("Leve um guarda chuva!")
# else:
#     print("Tenha um bom dia!")


# 6. Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")

# pontos= 50 
# print("Parabens! Você Fez:",pontos, "pontos")

# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")
#Corrigido
# nota = float(input("Digite a sua nota"))
# if nota >=7:
#     print("Aprovado")
# if nota >=9:
#     print("Exelente!")   
#Melhorado 
# nota = float(input("Digite a sua nota"))
# if nota >=7:
#     print("Aprovado")
# if nota >=9:
#     print("Exelente!")   
# elif nota <7:
#     print("Reprovado, KKKKK")

# 8. O Contador de 1 a 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
# print(i)

#CORRIGIDO
# for i in range (1,5):
#     print(i)

# 9. O Loop Eterno
# tentativas = 1
# while tentativas <= 3:
# print("Tentando conectar...")
# O código deveria parar após 3 tentativas
#Corrigido
# tentativas= 1
# while tentativas <= 3:
#     print("Tentando conectar ...")
#     tentativas += 1

# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"
# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!") 
#Corrigido
# senha = input("Digite a senha secreta")
# while senha == "python123":
#     break
# print("Acesso concedido!")
