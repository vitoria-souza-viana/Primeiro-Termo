# 1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
# jogador [nick] está no nível [nível] e pronto para a partida!"
print("Bem vindo!")
pergunta1= input("Digite o seu nick:")
pergunta2=input("Digite o seu nível atual:")
print("O jogador : " , pergunta1, "está no nível:", pergunta2, "e pronto para a partida!") 

# 2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e
# multiplique por 4 para mostrar quanto ele terá no final do mês.
pergunta1= int(input("Digite a variavel:"))
total= pergunta1 * 4 
print("No final do mês você terá:", total)

# 3. Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para
# Megabytes (MB) (multiplique por 1024).
pergunta1= int(input("Digite o valor em GB:"))
total= pergunta1 * 1024
print("O resultado é:", total)

# 4. Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a
# média final.
pergunta1= int(input("Digite a sua nota de Matemática:"))
pergunta2= int(input("Digite a sua nota de Português:"))
total1= pergunta1 + pergunta2
total= total1/2
print("A sua média é:", total)

# 5. Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores
# o aluno ganhou hoje. Exiba o total atualizado.
pergunta1=int(input("Quantos seguidores você tem?"))
pergunta2=int(input("Quantos seguidores você ganhou hoje?"))
total= pergunta1+pergunta2
print("Agora você tem:", total, "seguidores")

# 6. Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias
# ele já viveu (idade * 365).
pergunta1=int(input("Quantos anos você tem?"))
total=pergunta1*365
print("Você ja viveu:", total, "dias. Ta ficando velho hein!")

# 7. Consumo de Lanche: Peça o preço do salgado e o preço do suco. Exiba o valor
# total da conta.
salgado= int(input("Qual é o valor do sagado?"))
suco= int(input("Qual é o valor do suco?"))
total=salgado+suco
print("Você vai pagar:", total, "reais")

# 8. Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano
# em que ele nasceu.
pergunta1=int(input("Digite o ano atual"))
pergunta2=int(input("Quantos anos você tem?"))
total=pergunta1-pergunta2
print("Você nasceu em:", total)

# 9. Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
# "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
# # mais, "Acesso liberado".
idade=int(input("Digite a sua idade"))
if idade < 13:
    print("Acesso restrito")
if  13 < idade < 18:
    print("Acesso Moderado")
else:
    print("Acesso liberado")

# 10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
# repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
# chegar em 10 e exibe: "Por favor, conecte o carregador!".

# 11. Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
# foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
# esse número, printando: "Curtida numero [i] recebida!".
pergunta1=int(input("Defina um limite de curtidadas começando do 0:"))
for curtidas in range (pergunta1):
    print(f"Curtida n° {curtidas} recebida!")

# 12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o
# aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre
# quantas vezes ele adiciona itens ao carrinho (use um contador).
