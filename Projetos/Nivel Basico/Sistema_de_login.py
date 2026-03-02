tentativas = 0
max_tentativas = 3
login_correto = 'admin'
senha_correta = 'zxc123'

while tentativas < max_tentativas:
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    if login == login_correto and senha == senha_correta:
        print('Login efetuado com sucesso!.')
        break
    else:
        tentativas += 1
        print(f'Tentativa {tentativas} de {max_tentativas}')
else:
    print('Número máximo de tentativas atingido.')
