#Tratamento de erros 
##Organizar de forma adequada o código é essencial para evitar erros e garantir que o pragrama funcione  O tratamento de erros é uma prática importante para lidar com situações inesperadas que podem ocorrer durante a execução do programa.
# try e except são estruturas usadas para capturar e lidar com erros de forma controlada. O código dentro do bloco try é executado normalmente, mas se ocorrer um erro, o programa pula para o bloco except, onde você pode definir como lidar com o erro.


# Erros comuns:
# - ZeroDivisionError: divisão por zero
# - ValueError: conversão de tipo inválida
# - IndexError: acesso a índice fora do limite
# - KeyError: acesso a chave inexistente em dicionário



# While true : 
# try:
#  # Código que pode gerar um erro 
#  numero = int(input("Digite um número: "))
#  resultado = 10 / numero 
#  print(f"O resultado é: {resultado}")


# except ValueError:
#   print("Erro: Você deve digitar um numero valido.")
#   break

# except ZeroDivisionError:
#   print("Erro: Não é possivel dividir por zero")
#   break

# except Exception as erro:
#   print(f"Ocorreu um erro inesperado: {erro}")
#   break

# print("Programa encerrado.")


# Exercicio 1:
# Crie um algoritmo para calcular a média e trate o erro ao inserir valores errados.
while True:
    try:
        nota1 = float(input("Digite seu primeiro numero: "))
        nota2= float(input("Digite seu segundo numero: "))
        conta1 = nota1 + nota2 
        media = conta1 / 2
        print(f"Sua média é: {media}")
    
    except ValueError:
        print("Digite um numero valido")
        break

    
    except ZeroDivisionError:
        print("Não é possivel dividir por zero")
        break 
    print("Programa encerrado")


#  Exercicio 2 
# Escreva um programa que solicite ao usuário um número inteiro e calcule a media de uma lista de números. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja um número inteiro.
# - ZeroDivisionError: se a lista de números estiver vazia.
# len: Retorna o número de itens de um objeto. Pode ser usado para obter o comprimento de uma string, lista, dicionário, etc.
# append: Adiciona um item ao final de uma lista.
while True: 
 try:
    print("Calculadora de Média em lista")
    lista = []
    numero = int(input("Digite um numero inteiro para definir o tamanho da lista: "))
    for listagem in range (numero):
     numero_lista = float(input(f"Digite o numero {listagem + 1}:"))
    lista.append(numero_lista)

    media = sum(lista)/ len(lista)
    print(f"A média dos numeros é:{media}")
    break 
 except ValueError:
    print("Erro: Você deve digitar um numero inteiro valido tente novamente.")
    break
 except ZeroDivisionError:
    print("Erro: A lista de núumeros está vazia. não é possivel calcular a média.")
    break 
print("Programa encerrado.")


# Exercicio 3:
# Escreva um programa que solicite ao usuário uma lista de palavras e conte quantas vezes cada palavra aparece na lista. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja uma string.

try: 
   palavras = input("Digite uma lista de palavras separadas por espaço").split()
   contagem = {}
   for lista in palavras:
      if palavras in contagem:
         contagem [palavras] += 1
      else:
         contagem[palavras] = 1 
         print("Contagem de palavras")
         for palavras, contagem in contagem.items():
            print(f"{palavras}:{contagem}")
except ValueError:
   print("Erro: Entrada invalida: Digite uma lista separada por espaços.")
         




