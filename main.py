rotas_vagas = {
    "centro": {"manhã": 45, "tarde": 35, "noite": 10},
    "localidade": {"manhã": 30, "tarde": 20, "noite": 10},
    "zona-rural": {"manhã": 35, "tarde": 40, "noite": 10}
}

alunos = []

def validar_turno(periodo):
    periodo = periodo.lower()
    
    if periodo == "matutino" or periodo == "manhã" or periodo == "manha":
        return "manhã"
    elif periodo == "vespertino" or periodo == "tarde":
        return "tarde"
    elif periodo == "noturno" or periodo == "noite":
        return "noite"
    else:
        return None

def colocar_Aluno(nome, rota, turno, vagas):
    if rota in vagas and turno in vagas[rota]:
        if vagas[rota][turno] > 0:
            vagas[rota][turno] -= 1
            return f"Aluno [{nome}] cadastrado na [{rota}] para o turno da [{turno}]."
    return False

while True:
   
    print("Rotas disponíveis:")
    print(f"{rotas_vagas}")

    nome_aluno = input("Nome do aluno: ")
    rota_desejada = input("Rota (centro/localidade/zona-rural): ").lower()
    entrada = input("Qual o período (Manhã/Tarde/Noite): ")

    turno_validado = validar_turno(entrada)
    resultado = colocar_Aluno(nome_aluno, rota_desejada, turno_validado, rotas_vagas)

    if resultado:
        alunos.append({"nome": nome_aluno, "rota": rota_desejada, "turno": turno_validado})
        print(resultado)
    else:
        print("Erro ao cadastrar. Verifique os dados ou vagas.")
    
    print("Rotas atualizadas:")
    print(f"{rotas_vagas}")

    continuar = input("\nDeseja cadastrar outro aluno(a): (s ou n)").lower()
    
    if continuar == "s":
        continue
    else:
        break

print("\nEncerrando Sistema, Alunos cadastrados:", alunos)
