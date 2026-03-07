
rotas_vagas = {
    "centro": 45,
    "localidade": 50, #no primeiro commit tava cidade-vizinha
    "zona-rural": 30
}

turnos = ["matutino", "vespertino"]
alunos = []

def dados_alunos(listaRotas, turnoLista):
    nome = input("Diga seu nome: ")
    
    while True:
        turno = input(f"Qual o turno {turnoLista}: ").lower()
        if turno == "matutino" or turno == "vespertino":
            break
        print("Turno inválido, deve ser matutino ou vespertino (desse jeito)")
    
    print("\nRotas disponíveis:")
    print(f"{listaRotas}")

    while True:
        rota = input("Qual é a rota: ").lower()
        if rota in listaRotas:
            break
        print("Rota inválida, reveja as opções de rotas acima amigo(a)")
    
    return {"nome": nome, "turno": turno, "rota": rota}

def organizar_vagas(aluno, vagas):
    rota_escolhida = aluno['rota']
    if vagas[rota_escolhida] > 0:
        vagas[rota_escolhida] -= 1
        return True
    else:
        return False

while True:
    novo_aluno = dados_alunos(rotas_vagas, turnos)
    
    if organizar_vagas(novo_aluno, rotas_vagas):
        alunos.append(novo_aluno)
        print(f"{novo_aluno['nome']}! Você foi cadastrado na rota: {novo_aluno['rota']}.")
    else:
        print(f"{novo_aluno['nome']}. Não há vagas para a rota: {novo_aluno['rota']}.")

    print(f"Vagas restantes: {rotas_vagas}")
