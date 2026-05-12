# 1. O laço "for" (Repetições Determinadas)
# Use o "for" quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou  uma lista de peças).
#Exemplo: relatório de produção diaria 
# imagine que você tem uma meta de produção de 5 lotes e quer numerar cada um

#Exemplo
for lote in range(1,6):
    print(f"Processando lote número (lote)...")
    print("Qualidade verificada. [OK]")
    print("Produção do dia finalizada!")

    #Exemplo 2
    for b in range (10):
        print(f"Quantidade total {b} foi...")

    #Exemplo 3 
    #imagine o seguinte cenario, iremos produzir 20 discos de vinil.
    for discos in range (1 ,21):
        print(f"Quantidade total {discos} foi...")
            
    #Exemplo 4
    pecas = ["Engrenagem" , "Eixo" , "Rolamento" , "Parafuso" , "Martelo"]
    itempecas= ["cilindricas", "eixo conico" "Radiais", "Madeira"]

    for item in pecas: 
        print(f"Item em estoque: {item} e {itempecas}")
        for item2 in itempecas: 
            print(f"Item de peças em estoque: {itempecas}")

#Exemplo 5
# Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir da seleção ele listar os produtos 
print("Loja vsv")
print("Opção 1- peças")
print("Opção 2- item peças")
menu= int(input("Escolha uma opção"))

pecas=["Engrenagens","Eixo", "Rolamento","Parafuso","Martelo","Chave de fenda"]
itempecas= ["cilindricas", "eixo conico" "Radiais", "Madeira"]
if menu==1:
        print(f"Sua lista de peças {pecas} são...")
elif menu==2:
    print(f"Sua lista de peças {itempecas} são...")
else: 
    print("Opção invalida: Encerrando o sistema")

# #Exercicio 1 
# #1. Contador de produção (for)
# #Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e para cada numero imprima: "peça numero x processada com sucesso".
#No final exiba ciclo de produção concluida 

for ciclo in range (1,11):
     print(f"Peça numero {ciclo} processada com sucesso..:)")
print("Ciclo de produção concluido...:)")

#Exercicio 2 
# Imagine a produção  d e frutas em uma feira. Desejo apresentar as frutas banana,  manga, melancia, abacaxi.
# Com uma quantidade de 10 bananas, 5 mangas, 10 melancias e 10 abacaxi

for banana in range (10):
     print(f" A quantidade de {banana} foi...:)")
for mangas in range (5):
     print(f" A quantidade de {mangas} foi...:)")
for melancias in range (10):
     print(f" A quantidade de {melancias} foi...:)")
for abacaxi in range (10):
     print(f" A quantidade de {abacaxi} foi...:)")

#Exercicio 3
# montar uma tabuada inicialmente pode ser usada por um valor fixo e depois usar a pergunta 
int(input("Qual tabuada você deseja fazer?")) 










