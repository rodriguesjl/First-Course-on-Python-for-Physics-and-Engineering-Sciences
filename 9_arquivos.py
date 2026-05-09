#1) Total de linhas em um arquivo

arquivo = open('data.csv')

linhas = 0
for linha in arquivo:
    linhas+=1
print('total de linhas {}\n'.format(linhas))

# 2) Crie um sistema de controle de acesso, solicitando login e senha para usuários que desejam acessar. As informações de login e senha devem ser armazenadas no arquivo “usuarios.txt”. Seu programa deve conter o seguinte menu:

   # a. Cadastrar usuário: solicita o login e senha que o usuário deseja cadastrar e
   #verifica se o login está disponível (se não existe no arquivo “usuarios.txt”).
   #Em caso positivo, salva o novo usuário em arquivo, caso contrário, solicita
   #novo login e senha até que o usuário digite uma entrada válida.
    
    #b. Fazer login: solicita o login e a senha do usuário, e verifica se existe no
    #arquivo. Em caso positivo imprima “login efetuado com sucesso”, caso
    #contrário imprima uma mensagem de erro.

marcador = True
while marcador:
    escolha = input('Escolha:\nDigite 0 para sair\nDigite 1 para cadastrar\n'
                    'Digite 2 para fazer login\nResposta:\n')
    if escolha == '0':
        marcador = False
        break
        
    elif escolha == '1':
        
        usuario_cad = input('Digite o usuario')
        
        with open('dados.csv','r') as arquivo:
            for linha in arquivo:
                if usuario_cad in linha:
                    while usuario_cad in linha:
                        usuario_cad = input('Usuário existente, escolha outro:\n')
                    continue
        with open('dados.csv','a') as arquivo:
            senha_cad = input('Digite a senha')
            arquivo.write(usuario_cad+';'+senha_cad+'\n')
            
    elif escolha == '2':

        usuario = input('Digite seu nome de usuario\n')
        senha = input('Digite a senha:\n')
        with open('dados.csv','r') as arquivo:
            if (usuario+';'+senha+'\n') in arquivo:
                print('Login concedido')
            else:
                print('usuário ou senha não encontrados')
