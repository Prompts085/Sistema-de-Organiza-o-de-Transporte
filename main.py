rotas_vagas = {
    "centro": 45,
    "cidades-vizinhas": 50,
    "zona-rural": 30
}

turnos = [ "matutino", "vespetino" ]
alunos = []

def dados_alunos(listaRotas, turnoLista):
    nome = input("Diga seu nome: ")
    
    #Validando turno:
    while True:
        turno = input(f"Qual o turno {turnoLista}:").lower()
        if turno == "matutino" or turno == "vespertino":
            break
        print("turno inválido, deve ser matutino ou vespertino (desse jeito)")
    
    #Mostrando as rotas disponiveis
    print("\nRotas disponíveis:")
    print(f"{listaRotas}")

    #Validando rota:
    while True:
        rota = input(f"Qual é a rota:").lower()
        if rota in listaRotas:
            break
        print("Rota inválida, reveja as opções de rotas acima amigo(a)")
    
    return {"nome": nome, "turno": turno, "rota": rota}

novo_estudante = dados_alunos(rotas_vagas, turnos)
alunos.append(novo_estudante) #aqui vamos guardar o aluno na variavel dele

print(f"\nPronto, {novo_estudante['nome']}! você foi pré-cadastrado.")

