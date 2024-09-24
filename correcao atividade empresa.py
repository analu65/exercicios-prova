dic = {}

print("*****"*10)
print("Menu de Opções: ")
print("C - cadastrar")
print("A - alterar")
print("E - excluir")
print("P - pesquisar")
print("S - sair")
print("*****"*10)

while True:
    opcao = input("Digite a opçao que deseja selecionar: ").upper()
    if opcao == "S":
        print("programa encerrado.")
        break
    if opcao == "C":
        numero = int(input("Digite o numero do funcionario: "))
        funcionarios = input("Digite o nome do funcionario: ")
        cargos = input("Digite o cargo do funcionario: ")
        dic[numero] = funcionarios,cargos
        print(dic)
    if opcao == "A":
        alt = input("Digite o que deseja alterar (C - cargo ou F - funcionario): ").upper()

        if alt == "F":
            numfunc = int(input("Digite o numero do funcionario que deseja alterar: "))
            novofunc = input("digite o nome do novo funcionario: ")
            if numfunc not in dic:
                print("funcionario nao cadastrado")
            else:
                dic[numero][0] = novofunc
            if alt == "C":
                numcargo = int(input("Digite o numero do cargo que deseja alterar: "))
                novocargo = input("digite o nome do novo cargo: ")
                if numcargo not in dic:
                    print("cargo nao cadastrado")
                else:
                    dic[numero][1] = novocargo
    if opcao == "E":
        remover = int(input("digite o numero do funcionario que deseja remover: "))
        if remover in dic:
            dic.pop(remover)
        else:
            print("funcionario nao cadastrado")
    if opcao == "P":
        print("lista completa: ",dic)
        print("lista em ordem alfabetica: ",sorted(dic,reverse = False))
        print("total de funcionarios cadastrados: ",len(dic))
        