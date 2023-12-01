cor_vermelha = '\033[91m'
cor_amarela = '\033[93m'
cor_ciano = '\033[96m'
cor_verde = '\033[92m'
cor_reset = '\033[0m'


def realizar_login():

    print(cor_ciano + "==================== Área de Login ====================\n\n" + cor_reset)
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    try:
        
        with open('usuarios.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

            
            for linha in linhas:
                usuario_arquivo, senha_arquivo = linha.strip().split(',')
                if usuario == usuario_arquivo and senha == senha_arquivo:
                    print(cor_verde + "\nLogin bem-sucedido!" + cor_reset)
                    return True
                
        print(cor_vermelha + "\nUsuário ou senha incorretos." + cor_reset)
        print("\nVamos para área de cadastro")

        cadastrar_usuario_senha(usuario,senha)
        return False
        

    except FileNotFoundError:
        
        with open('usuarios.txt', 'w') as arquivo:
            pass  

        cadastrar_usuario_senha(usuario,senha)  
        return True
    
def cadastrar_usuario_senha(usuario = None, senha = None ):

    print(cor_ciano + "==================== Área de cadastro ====================\n\n" + cor_reset)
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    try:
        with open('usuarios.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                usuario_arquivo, _ = linha.strip().split(',')
                if usuario == usuario_arquivo:
                    print(cor_amarela + "\nUsuário já cadastrado!" + cor_reset)
                    menu_principal()
                    return

        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write(f"{usuario},{senha}\n")

        print(cor_verde + "\nUsuário cadastrado com sucesso!" + cor_reset)
        print("Agora realize o Login!\n")

    except FileNotFoundError:
       
        with open('usuarios.txt', 'w') as arquivo:
            arquivo.write(f"{usuario},{senha}\n")

        print(cor_verde + "\nUsuário cadastrado com sucesso!" + cor_reset)
        print("Agora realize o Login!\n")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    
def menu_acessibilidade():
        
        print(cor_ciano + "==================== Bem-vindo a área de Acessibilidade! ==================" + cor_reset)
        while True:
            print("\nEscolha oque você deseja fazer:")
            print("1. Aumentar o tamanho da fonte")
            print("2. Alterar o contraste")
            print("3. Ler o conteúdo da página")
            print("4. Sair do site")

            escolha = input("Digite o número da escolha desejada: ")

            if escolha == "1":
                aumentar_tamanho_fonte()
            elif escolha == "2":
                alterar_contraste()
            elif escolha == "3":
                ler_conteudo_pagina()
            elif escolha == "4":
                print("Saindo do site.")
                break
            else:
                print("Escolha inválida. Por favor, digite um número válido.")

def aumentar_tamanho_fonte():
        
        print("Tamanho da fonte aumentado com sucesso.")
        resumo_operacao("Aumentar o tamanho da fonte")

def alterar_contraste():
        
        print("Contraste alterado com sucesso.")
        resumo_operacao("Alterar o contraste")

def ler_conteudo_pagina():
        
        print("Lendo o conteúdo da página...")
        resumo_operacao("Ler o conteúdo da página")

def resumo_operacao(acao):
        opcao = input(f"Deseja realizar outra operação? (S/N): ").lower()
        if opcao != "s":
            print(f"Obrigado por usar a area de Acessibilidade. {acao} finalizado.")
        else:
            print(f"Retornando ao menu...")


def menu_principal():

    print(cor_ciano + "\n\n============================== Bem vindo! ==============================" + cor_reset + "\nPara acessar a área de acessibilidade faça login ou cadastre-se.")

    while True:
        try:
            op = int(input("\n\nEscolha uma das opções abaixo e digite o número correspondente: \n[1] para login \n[2] para se cadastrar \n[3] para sair\n"))
            
            if op == 1:
                logado = realizar_login() 
                if logado:
                    menu_acessibilidade()
            elif op == 2:
                cadastrar_usuario_senha()
            elif op == 3:
                break
            else:
                print(cor_vermelha + "\nOperação inválida. Escolha uma opção válida!" + cor_reset)
        except ValueError:
            print(cor_vermelha + "\nErro: Por favor, digite apenas números para escolher uma opção!" + cor_reset)
            