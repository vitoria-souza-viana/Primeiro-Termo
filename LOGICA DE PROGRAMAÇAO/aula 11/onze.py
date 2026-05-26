# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar



andaratual=0
while True:
    try: 
        destino = int(input("Digite o andar de destino(0-10): "))
        if destino < 0 or destino > 10:
            raise ValueError ("Andar invalido, por favor, digite um numero entre 0 e 10 ")
            
        print(f("Elevador se movendo do andar {andaratual} para o andar {destino}..."))
        andaratual = destino
        print(f"Chegamos ao andar {andaratual}")

        if input("Deseja escolher outro andar? (s/n): ").lower()!= 's':
            print("Obrigada por usar o elevador python! Até a próxima!")
            break
        for listagem in range(10):
            print(f"Andar {listagem} - {'[X]' if listagem == andaratual else '[ ]'}")
    except ValueError as erro:
        print(f"Erro: {erro}. tente novamente")
        print("Programa encerrado")
        break