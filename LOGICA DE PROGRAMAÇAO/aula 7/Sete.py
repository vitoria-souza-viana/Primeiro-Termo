# projeto cancela automatica 
# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

print("Bem-vindo ao shopping Pátio!")
print("Escolha uma das opções")
print("1- Ticket \n 2- TAG \n 3- Interfone")
metodoentrada= input("Ticket / Tag / Interfone")

if metodoentrada == "Ticket": 
    print("Bem-Vindo ao shopping")
horaentrada= int(input("Digite a hora de entrada"))
valorestacionamento= float(input("Digite o valor a cobrar"))
horasaida= float(input("Digite a hora da saida"))
totalpermanencia= horasaida - horaentrada
print(f"Seu tempo de permanencia {totalpermanencia} em horas")
totalestacionamento= totalpermanencia * valorestacionamento
print(f"O valor total a ser cobrado foi de R${totalestacionamento:.2f }")
print("Devolver o ticket")

if metodoentrada=="Tag": 
    print("Bem vindo ao shopping")
    print("Sua parmanencia no shopping será cobrado na sua fatura")
    print("obrigado pela visita!")

elif metodoentrada == "Interfone":
    print("Bem-vindo ao shopping")
    print("Liberando acesso pelo interfone")
    print("Sua saída deverá ser feita também pelo interfone")

else: 
    print("Obrigada pela visita!")
