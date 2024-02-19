from controller import ControllerCadastro, ControllerLogin

while True:
    print('========== MENU ==========')
    decisao = int(input(f'Digite 1 para cadastrar\n'
                        f'Digite 2 para logar\n'
                        f'Digite 3 para sair\n'))
    
    if decisao == 1:
        nome = input('Digite o nome:')
        email = input('Digite o email:')
        senha = input('Digite a senha:')
        
        resultado = ControllerCadastro.cadastrar(nome=nome, email=email, senha=senha)
        
        if resultado == 2:
            print('O nome deve ter entre 4 e 50 caracteres')
        elif resultado == 3:
            print('O email deve conter menos de 200 caracteres')
        elif resultado == 4:
            print('A senha deve conter entre 6 e 100 caracteres')
        elif resultado == 5:
            print('Email já cadastrado')
        elif resultado == 6:
            print('Erro interno do sistema')
        elif resultado == 1:
            print('Cadastro realizado com sucesso')
            
    elif decisao == 2:
        email = input('Digite o email:')
        senha = input('Digite a senha:')
        resultado = ControllerLogin.login(email, senha)
        if not resultado:
            print('Email ou senha inválidos')
        else:
            print(resultado)
    else:
        break