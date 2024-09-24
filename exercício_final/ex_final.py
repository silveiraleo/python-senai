import pandas as pd
from datetime import datetime

def carregar_dados():
    try:
        return pd.read_excel("ex_final_python.xlsx")
    except FileNotFoundError:
        return pd.DataFrame(columns=["ID do produto", "Nome do produto", "Quantidade em estoque", "Preço compra", "Preço venda", "Data da compra"])

def salvar_dados(df):
    df.to_excel("ex_final_python.xlsx", index=False)

def realizar_login():
    usuario = input("Usuário (e-mail): ")
    senha = input("Senha: ")
    if usuario == "leodsilveira@hotmail.com" and senha == "python":
        print("Login bem-sucedido!")
        return True
    else:
        print("Credenciais incorretas. Tente novamente.")
        return False

def adicionar_produto(df):
    print("\nAdicionar um novo produto:")
    id_produto = int(input("ID do produto: "))
    nome_produto = input("Nome do produto: ")
    quantidade_estoque = int(input("Quantidade em estoque: "))
    preco_compra = float(input("Preço de compra: "))
    preco_venda = float(input("Preço de venda: "))
    while True:
        data_compra = input("Data da compra (AAAA-MM-DD): ")
        try:
            datetime.strptime(data_compra, "%Y-%m-%d")
            break
        except ValueError:
            print("Formato de data inválido. Tente novamente.")
    
    if preco_compra <= 0 or preco_venda <= 0 or quantidade_estoque <= 0:
        print("Erro: Valores de preço ou quantidade inválidos.")
    else:
        novo_produto = pd.DataFrame([{
            "ID do produto": id_produto,
            "Nome do produto": nome_produto,
            "Quantidade em estoque": quantidade_estoque,
            "Preço compra": preco_compra,
            "Preço venda": preco_venda,
            "Data da compra": data_compra
        }])
        df = pd.concat([df, novo_produto], ignore_index=True)
        print("Produto adicionado com sucesso!")
    return df

def listar_produtos(df):
    if df.empty:
        print("Nenhum produto cadastrado.")
    else:
        print(df)

def alterar_produto(df):
    listar_produtos(df)
    nome_produto = input("Digite o nome do produto que deseja alterar: ")
    produto_existente = df[df["Nome do produto"] == nome_produto]
    if not produto_existente.empty:
        print("\nProduto encontrado. Insira as novas informações:")
        df = df[df["Nome do produto"] != nome_produto]
        df = adicionar_produto(df)
        print("Produto alterado com sucesso!")
    else:
        print("Produto não encontrado.")
    return df

def excluir_produto(df):
    listar_produtos(df)
    nome_produto = input("Digite o nome do produto que deseja excluir: ")
    if "Nome do produto" in df.columns:
        df = df[df["Nome do produto"] != nome_produto]
        print("Produto excluído com sucesso!")
    else:
        print("Erro: 'Nome do produto' não encontrado.")
    return df

def exportar_dados(df):
    print("\nOpções de exportação:")
    print("1. Exportar para .xlsx")
    print("2. Exportar para .json")
    print("3. Exportar para .csv")
    escolha = input("Escolha o formato de exportação (1/2/3): ")
    if escolha == "1":
        df.to_excel("produtos_exportados.xlsx", index=False)
        print("Dados exportados para produtos_exportados.xlsx")
    elif escolha == "2":
        df.to_json("produtos_exportados.json", orient="records")
        print("Dados exportados para produtos_exportados.json")
    elif escolha == "3":
        df.to_csv("produtos_exportados.csv", index=False)
        print("Dados exportados para produtos_exportados.csv")
    else:
        print("Opção de exportação inválida.")

def main():
    df = carregar_dados()
    logado = False
    exportacao_realizada = False
    
    while not logado:
        logado = realizar_login()

    while True:
        print("\nOpções disponíveis:")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Alterar produto")
        print("4. Excluir produto")
        print("5. Exportar dados")
        print("6. Sair")
        escolha = input("Escolha a opção desejada: ")
        
        if escolha == "1":
            df = adicionar_produto(df)
        elif escolha == "2":
            listar_produtos(df)
        elif escolha == "3":
            df = alterar_produto(df)
        elif escolha == "4":
            df = excluir_produto(df)
        elif escolha == "5":
            exportar_dados(df)
            exportacao_realizada = True
        elif escolha == "6":
            if not exportacao_realizada:
                opcao_exportar = input("Você ainda não exportou os dados. Deseja exportar antes de sair? (S/N): ")
                if opcao_exportar.lower() == "s":
                    exportar_dados(df)
            salvar_dados(df)
            print("Dados salvos em ex_final_python.xlsx")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
