# Boas Vindas
print('Bem-vindo a Livraria Krajezar! Meu nome é Caique Krajezar, em que posso ajudar')

# Lista de livros (lista de dicionários)
lista_livro = []
id_global = 0

# Cadstro de Livros
def cadastrar_livro(id):
    print(f'\nID do livro: {id}')
    nome = input('Digite o nome do livro: ')
    autor = input('Digite o nome do autor: ')
    editora = input('Digite o nome da editora: ')
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)
    print('Livro cadastrado com sucesso!')

# Consultar livros
def consultar_livro():
    while True:
        print('\nMenu de Consulta')
        print('1. Consultar Todos')
        print('2. Consultar por Id')
        print('3. Consultar por Autor')
        print('4. Retornar ao menu')
        opcao = input('Escolha a opção desejada: ')
        if opcao == '1':
            print('\nLista de todos os livros:')
            for livro in lista_livro:
                print(f"ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}")
        elif opcao == '2':
            id_busca = input('Digite o ID do livro: ')
            encontrado = False
            for livro in lista_livro:
                if str(livro['id']) == id_busca:
                    print(f"ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}")
                    encontrado = True
            if not encontrado:
                print('Livro não encontrado.')
        elif opcao == '3':
            autor_busca = input('Digite o nome do autor: ')
            encontrados = [livro for livro in lista_livro if livro['autor'].lower() == autor_busca.lower()]
            if encontrados:
                for livro in encontrados:
                    print(f"ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}")
            else:
                print('Nenhum livro encontrado para este autor.')
        elif opcao == '4':
            break
        else:
            print('Opção inválida')

# Remover livro
def remover_por_id():
    while True:
        remover_por_id = input('Digite o ID do livro a ser removido: ')
        for livro in lista_livro:
            if str(livro['id']) == remover_por_id:
                lista_livro.remove(livro)
                print('Livro removido com sucesso!')
                return
        print('Id inválido')

# Estrutura principal do menu
while True:
    print('\nMenu Principal')
    print('1. Cadastrar Livro')
    print('2. Consultar Livro')
    print('3. Remover Livro')
    print('4. Encerrar Programa')
    opcao = input('Escolha a opção desejada: ')
    if opcao == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover_por_id()
    elif opcao == '4':
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida')