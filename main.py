
rotas_vagas = {
    "centro": {"matutino": 45, "vespertino": 35},
    "localidade": {"matutino": 30, "vespertino": 20},
    "zona-rural": {"matutino": 35, "vespertino": 40}
}

alunos = []

def dados_alunos(listaRotas):
    nome = input("Diga seu nome: ")
    
    while True:
        turno = input(f"Qual o turno (matutino ou vespertino): ").lower()
        if turno == "matutino" or turno == "vespertino":
            break
        print("Turno inválido, deve ser matutino ou vespertino (desse jeito)")
    
    print("\nRotas disponíveis:")
    print(f"{listaRotas}")

    while True:
        rota = input("\nQual é a rota: ").lower()
        if rota in listaRotas:
            break
        print("Rota inválida, reveja as opções de rotas acima amigo(a)")
    
    return {"nome": nome, "turno": turno, "rota": rota}

def organizar_vagas(aluno, vagas):
    rota = aluno['rota']
    turno = aluno['turno']

    if vagas[rota][turno] > 0:
        vagas[rota][turno] -= 1
        return True
    else:
        return False

while True:
    novo_aluno = dados_alunos(rotas_vagas)
    
    if organizar_vagas(novo_aluno, rotas_vagas):
        alunos.append(novo_aluno)
        print(f"{novo_aluno['nome']}! Você foi cadastrado na rota: {novo_aluno['rota']}.")
    else:
        print(f"{novo_aluno['nome']}. Não há vagas para a rota: {novo_aluno['rota']}.")

    print(f"Vagas restantes: {rotas_vagas}")

    continuar = input("\nDeseja cadastrar outro aluno(a): (s ou n)").lower()
    if continuar == "s":
        continue
    else:
        break