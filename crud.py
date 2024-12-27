import os
from time import sleep

# Classe para representar um usuário com nome e idade.
class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome  # Nome do usuário
        self.idade = idade  # Idade do usuário


# Classe para gerenciar as operações de CRUD sobre os usuários.
class GerenciadorUsuarios:
    def __init__(self):
        # Define o caminho do arquivo onde os dados serão armazenados.
        self.arquivo = os.path.join(os.path.dirname(__file__), 'usuarios.txt')

        # Verifica se o arquivo já existe. Se não existir, cria um arquivo vazio.
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'w'):
                pass

    # Método para adicionar um novo usuário.
    def adicionar_usuario(self, nome, idade):
        # Abre o arquivo no modo de adição e escreve os dados do usuário.
        with open(self.arquivo, 'a') as f:
            f.write(f"{nome}, {idade}\n")
            print("Usuário adicionado com sucesso!")

    # Método para listar todos os usuários cadastrados.
    def listar_usuarios(self):
        if os.path.exists(self.arquivo):  # Verifica se o arquivo existe.
            with open(self.arquivo, 'r') as f:
                print("=" * 100)
                print("Lista de usuários:")
                print("-" * 100)

                # Lê cada linha do arquivo e exibe os dados formatados.
                for linha in f:
                    nome, idade = linha.strip().split(',')
                    print("*" * 100)
                    print(f'Nome: {nome}, Idade: {idade}')
                    print('*' * 100)

                print('=' * 100)
        else:
            print('Nenhum usuário cadastrado.')

    # Método para atualizar os dados de um usuário existente.
    def atualizar_usuario(self, nome, novo_nome, nova_idade):
        with open(self.arquivo, 'r') as f:
            linhas = f.readlines()  # Lê todas as linhas do arquivo.

        with open(self.arquivo, 'w') as f:
            atualizado = False  # Flag para verificar se o usuário foi atualizado.

            for linha in linhas:
                nome_usuario, idade = linha.strip().split(',')

                # Se encontrar o usuário pelo nome, atualiza os dados.
                if nome_usuario == nome:
                    f.write(f'{novo_nome},{nova_idade}\n')
                    atualizado = True
                else:
                    f.write(f'{nome_usuario},{idade}\n')

            # Mensagens de feedback para o usuário.
            if atualizado:
                print("✅ Usuário atualizado com sucesso!")
            else:
                print('❌ Usuário não encontrado.')

    # Método para excluir um usuário.
    def excluir_usuario(self, nome):
        with open(self.arquivo, 'r') as f:
            linhas = f.readlines()  # Lê todas as linhas do arquivo.

        with open(self.arquivo, 'w') as f:
            excluido = False  # Flag para verificar se o usuário foi excluído.

            for linha in linhas:
                nome_usuario, idade = linha.strip().split(',')

                # Se o nome não for o buscado, mantém o registro.
                if nome_usuario != nome:
                    f.write(f'{nome_usuario},{idade}\n')
                else:
                    excluido = True  # Marca que o usuário foi excluído.

            # Mensagens de feedback para o usuário.
            if excluido:
                print("🗑 Usuário excluído com sucesso!")
            else:
                print('❌ Usuário não encontrado.')


# Função para exibir o menu principal.
def exibir_menu():
    print("\nMENU:")
    print("1. Adicionar Usuário")
    print("2. Listar Usuários")
    print("3. Atualizar Usuário")
    print("4. Excluir Usuário")
    print("5. Sair")


# Função principal que controla o programa.
def main():
    gerenciador = GerenciadorUsuarios()  # Cria uma instância do gerenciador.

    while True:
        exibir_menu()  # Exibe o menu de opções.
        opcao = input("Escolha uma opção:\n>>> ")

        if opcao == "1":  # Adicionar usuário.
            nome = input("Digite o nome:\n>>> ")
            idade = input("Digite a idade:\n>>> ")
            gerenciador.adicionar_usuario(nome, idade)

        elif opcao == "2":  # Listar usuários.
            gerenciador.listar_usuarios()

        elif opcao == "3":  # Atualizar usuário.
            nome_antigo = input("Digite o nome a ser atualizado:\n>>> ")
            novo_nome = input("Digite o novo nome:\n>>> ")
            nova_idade = input("Digite a nova idade:\n>>> ")
            gerenciador.atualizar_usuario(nome_antigo, novo_nome, nova_idade)

        elif opcao == "4":  # Excluir usuário.
            nome = input("Digite o nome do usuário a ser excluído:\n>>> ")
            gerenciador.excluir_usuario(nome)

        elif opcao == "5":  # Sair do programa.
            print("Saindo...")
            sleep(3)
            break

        else:  # Opção inválida.
            print("Opção inválida. Tente novamente!")


# Ponto de entrada do programa.
if __name__ == "__main__":
    main()
