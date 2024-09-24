import pandas as pd

class Pessoa:
    def __init__(self, codigo, nome, idade, telefone):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

def salvar_arquivo_excel(df, file_path):
    df.to_excel(file_path, index=False, engine='openpyxl')

def cadastrar_pessoa(df):
    codigo = int(input("Informe o código da pessoa: "))
    nome = input("Informe o nome da pessoa: ")
    idade = int(input("Informe a idade da pessoa: "))
    telefone = input("Informe o telefone da pessoa: ")

    if telefone in df['telefone'].values:
        print("Não é permitido cadastrar pessoas com o mesmo telefone.")
        return df

    novo_registro = {'código': codigo, 'nome': nome, 'idade': idade, 'telefone': telefone}
    df = pd.concat([df, pd.DataFrame([novo_registro])], ignore_index=True)
    print("Pessoa cadastrada com sucesso!")

    return df

def consultar_pessoas(df):
    if df.empty:
        print("Nenhuma pessoa cadastrada.")
    else:
        print("\nLista de Pessoas:")
        print(df.to_string(index=False))

def editar_pessoa(df, codigo):
    if codigo in df['código'].values:
        nome = input("Informe o novo nome da pessoa: ")
        idade = int(input("Informe a nova idade da pessoa: "))
        telefone = input("Informe o novo telefone da pessoa: ")

        df.loc[df['código'] == codigo, ['nome', 'idade', 'telefone']] = [nome, idade, telefone]
        print("Pessoa editada com sucesso!")
    else:
        print("Pessoa não encontrada.")

    return df

def excluir_pessoa(df, codigo):
    if codigo in df['código'].values:
        df = df[df['código'] != codigo]
        print("Pessoa excluída com sucesso!")
    else:
        print("Pessoa não encontrada.")

    return df

def main():
    df = pd.DataFrame(columns=['código', 'nome', 'idade', 'telefone'])

    while True:
        print("\nMENU:")
        print("1 - Cadastrar uma nova pessoa")
        print("2 - Consultar todas as pessoas")
        print("3 - Editar uma pessoa da base de dados")
        print("4 - Excluir uma pessoa da base de dados")
        print("5 - Sair e gerar novo arquivo 'novo.xlsx'")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            df = cadastrar_pessoa(df)
        elif opcao == '2':
            consultar_pessoas(df)
        elif opcao == '3':
            codigo = int(input("Informe o código da pessoa a ser editada: "))
            df = editar_pessoa(df, codigo)
        elif opcao == '4':
            codigo = int(input("Informe o código da pessoa a ser excluída: "))
            df = excluir_pessoa(df, codigo)
        elif opcao == '5':
            salvar_arquivo_excel(df, 'novo.xlsx')
            print("Novo arquivo 'novo.xlsx' gerado. Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
