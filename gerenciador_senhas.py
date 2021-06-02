'''
PASSWORD STORAGE
Terá uma senha principal, só consigo rodar o script com ela
a senha vai ser guardada em um banco de dados sqlite
estas senhas poderão ser recuperadas depois
'''

import sqlite3

MASTER_PASSWORD = '515253' #não se usa definição de senhas dentro do código, desta forma como está sendo feito não
#apresente segurança alguma, isto somente está sendo utilizado assim para fins de APRENDIZADO!!

senha = input('Insira sua senha: ')
if senha != MASTER_PASSWORD:
    print('Senha Inválida! Encerrando ...')
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print('****************************************')
    print('*       i: inserir nova senha          *')
    print('*       l: listar serviços salvos      *')
    print('*       r: recuperar uma senha         *')
    print('*       s: sair                        *')
    print('****************************************')

def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users 
        WHERE service = '{service}'
        ''')

    if cursor.rowcount == 0:
        print('Serviço não cadastrado, use \"l\" para verificar os serviços')
    else:
        for user in cursor.fetchall():
            print(user)


def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
        ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)


while True:
    menu()
    op = input("O que você deseja fazer? ")
    if op not in ['i', 'l', 'r', 's']:
        print('Opção inválida! Verifique as opções disponíveis e digite novamente!')
        continue
    
    if op == 's':
        print('Encerrando o programa...')
        break

    if op == 'i':
        service = input('Digite o nome do serviço: ')
        username = input('Digite o nome de usuário: ')
        password = input('Digite a senha: ')
        insert_password(service, username, password)

    if op == 'l':
        show_services()
    
    if op == 'r':
        service = input('Qual o serviço para o qual você deseja recuperar a senha?')
        get_password(service)

conn.close()

