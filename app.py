import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='cadastro_livros'

)  #substitua com as suas credenciais do MySQL para poder estar utilizando as funcionalidades do código

cursor = conexao.cursor()

tabela = """CREATE TABLE IF NOT EXISTS livros(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_livro VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    valor_venda DECIMAL(10, 2) NOT NULL
);
"""

cursor.execute(tabela)

def cadastrar():
    
    nome_livro = input('Nome do livro: ')
    autor = input('Nome do autor: ')
    valor_venda = float(input('Valor de venda: '))
    sql = 'INSERT INTO livros (nome_livro, autor, valor_venda) VALUES (%s, %s, %s)'
    valores = (nome_livro, autor, valor_venda)
    cursor.execute(sql, valores)
    conexao.commit()

def consulta():
    consultar = 'SELECT * FROM livros'
    cursor.execute(consultar)
    resultado = cursor.fetchall()
    print(resultado)

def alterar():
    nome_alterado = input('Digite o título do livro que deseja alterar: ')
    valor_alterado = float(input('Digite a alteração de preço: '))

    alteracao = 'UPDATE livros SET valor_venda = %s WHERE nome_livro = %s'
    cursor.execute(alteracao, (valor_alterado, nome_alterado))
    conexao.commit()

def deletar():
    id_delet = input('Digite o id do livro que você quer apagar: ')
    excluir = 'DELETE FROM livros WHERE id = %s'
    cursor.execute(excluir, (id_delet,))
    conexao.commit()

    

def menu():
    while True:
        print("\n===MENU===")
        print('1 - Cadastrar Novo Livro')
        print('2 Lista de livros')
        print('3 Alterar cadastro')
        print('4 Deletar livro')
        print('5 Sair')

        opcao = (input('Escolha uma opção: '))

        if opcao == '1':
            cadastrar()

        elif opcao == '2':
            consulta()

        elif opcao == '3':
            alterar()
        
        elif opcao == '4':
            deletar()
        
        elif opcao == '5':
            break
        
        else:
            print('Opção Inválida!')

menu()




cursor.close()
conexao.close()



    
