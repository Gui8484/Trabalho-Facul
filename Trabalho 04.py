class Produto:
    def __init__(self, codigo, nome, categoria, quantidade, localizacao):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.localizacao = localizacao

    def __str__(self):
        return (f"Código: {self.codigo} | Produto: {self.nome} | Categoria: {self.categoria} "
                f"| Quantidade: {self.quantidade} | Localização: {self.localizacao}")


# Categorias de produtos
categoria_mercearia = "Mercearia"
categoria_eletrodomesticos = "Eletrodomésticos"
categoria_vestuarios = "Vestuários"

# Lista de produtos
produtos = [
    Produto(codigo=101, nome="Arroz", categoria=categoria_mercearia, quantidade=50, localizacao="A1"),
    Produto(codigo=102, nome="Feijão", categoria=categoria_mercearia, quantidade=30, localizacao="A2"),
    Produto(codigo=103, nome="Liquidificador", categoria=categoria_eletrodomesticos, quantidade=15, localizacao="B1"),
    Produto(codigo=104, nome="Camiseta", categoria=categoria_vestuarios, quantidade=100, localizacao="C1"),
    Produto(codigo=105, nome="Fogão", categoria=categoria_eletrodomesticos, quantidade=10, localizacao="B2"),
    Produto(codigo=106, nome="Calça Jeans", categoria=categoria_vestuarios, quantidade=70, localizacao="C2")
]


# Função para exibir os produtos de forma organizada no terminal
def exibir_produtos():
    print("\n================= Produtos no Estoque =================")
    print(f"{'Código':<10} {'Produto':<20} {'Categoria':<20} {'Quantidade':<10} {'Localização':<15}")
    print("------------------------------------------------------")
    for produto in produtos:
        print(
            f"{produto.codigo:<10} {produto.nome:<20} {produto.categoria:<20} {produto.quantidade:<10} {produto.localizacao:<15}")
    print("=======================================================")


# Função para movimentar estoque (entrada ou saída)
def movimentar_estoque():
    # Exibe os produtos antes da movimentação
    exibir_produtos()

    try:
        # Solicita ao usuário o código do produto
        codigo_produto = int(input("\nDigite o código do produto para movimentação: "))

        # Solicita ao usuário o tipo de movimentação (entrada ou saída)
        tipo_movimentacao = input("Digite o tipo de movimentação (entrada/saida): ").strip().lower()

        if tipo_movimentacao not in ['entrada', 'saida']:
            print("Tipo de movimentação inválido! Por favor, escolha 'entrada' ou 'saida'.")
            return

        # Solicita a quantidade de movimentação
        quantidade = int(input(f"Digite a quantidade de {tipo_movimentacao} para o produto: "))

        # Processa a movimentação com base no tipo
        for produto in produtos:
            if produto.codigo == codigo_produto:
                if tipo_movimentacao == 'entrada':
                    produto.quantidade += quantidade
                    print(f"Entrada de {quantidade} unidades de {produto.nome}. Novo estoque: {produto.quantidade}")
                elif tipo_movimentacao == 'saida':
                    if produto.quantidade >= quantidade:
                        produto.quantidade -= quantidade
                        print(f"Saída de {quantidade} unidades de {produto.nome}. Novo estoque: {produto.quantidade}")
                    else:
                        print(f"Estoque insuficiente para {produto.nome}. Quantidade disponível: {produto.quantidade}")
                return

        print("Produto não encontrado!")

    except ValueError:
        print("Entrada inválida! Certifique-se de inserir números inteiros.")


# Função para cadastrar novos produtos
def cadastrar_produto():
    try:
        # Solicita as informações do novo produto
        codigo = int(input("\nDigite o código do novo produto: "))

        # Verifica se o código já existe
        for produto in produtos:
            if produto.codigo == codigo:
                print(f"Erro: Já existe um produto com o código {codigo}. Tente novamente.")
                return

        nome = input("Digite o nome do novo produto: ").strip()
        categoria = input("Digite a categoria do produto (ex: Mercearia, Eletrodomésticos, Vestuários): ").strip()
        quantidade = int(input("Digite a quantidade do novo produto: "))
        localizacao = input("Digite a localização do produto no estoque: ").strip()

        # Cria o novo produto e adiciona à lista
        novo_produto = Produto(codigo=codigo, nome=nome, categoria=categoria, quantidade=quantidade,
                               localizacao=localizacao)
        produtos.append(novo_produto)

        print(f"\nProduto '{nome}' cadastrado com sucesso!")

    except ValueError:
        print("Erro: Digite valores válidos. O código e a quantidade devem ser números inteiros.")


# Função para gerar um relatório de produtos por categoria
def relatorio_categoria():
    categoria = input("\nDigite a categoria para o relatório (ex: Mercearia, Eletrodomésticos, Vestuários): ").strip()
    print(f"\nRelatório de produtos da categoria: {categoria}")
    print(f"{'Código':<10} {'Produto':<20} {'Categoria':<20} {'Quantidade':<10} {'Localização':<15}")
    print("------------------------------------------------------")
    for produto in produtos:
        if produto.categoria.lower() == categoria.lower():
            print(
                f"{produto.codigo:<10} {produto.nome:<20} {produto.categoria:<20} {produto.quantidade:<10} {produto.localizacao:<15}")
    print("=======================================================")


# Função para gerar um relatório de produtos com baixo estoque
def relatorio_estoque_baixo():
    try:
        limite = int(input("\nDigite o limite mínimo de quantidade para o relatório de baixo estoque: "))
        print(f"\nRelatório de produtos com estoque abaixo de {limite}:")
        print(f"{'Código':<10} {'Produto':<20} {'Categoria':<20} {'Quantidade':<10} {'Localização':<15}")
        print("------------------------------------------------------")
        for produto in produtos:
            if produto.quantidade < limite:
                print(
                    f"{produto.codigo:<10} {produto.nome:<20} {produto.categoria:<20} {produto.quantidade:<10} {produto.localizacao:<15}")
        print("=======================================================")
    except ValueError:
        print("Erro: O limite de estoque deve ser um número inteiro.")


# Função para gerar um relatório de quantidade total de todos os produtos
def relatorio_quantidade_total():
    total_produtos = sum(produto.quantidade for produto in produtos)
    print(f"\nQuantidade total de produtos no estoque: {total_produtos}")


# Função para consultar produto por código
def consultar_produto():
    try:
        codigo_produto = int(input("\nDigite o código do produto para consulta: "))
        for produto in produtos:
            if produto.codigo == codigo_produto:
                print(f"\nProduto encontrado: {produto}")
                return
        print("Produto não encontrado!")
    except ValueError:
        print("Erro: Digite um código válido.")


# Exemplo de uso
while True:
    print("\nEscolha uma opção:")
    print("1. Movimentar estoque")
    print("2. Exibir produtos")
    print("3. Cadastrar novo produto")
    print("4. Relatório de produtos por categoria")
    print("5. Relatório de produtos com estoque baixo")
    print("6. Relatório de quantidade total de produtos")
    print("7. Consultar produto por código")
    print("8. Sair")
    opcao = input("Digite a opção desejada (1/2/3/4/5/6/7/8): ")

    if opcao == '1':
        movimentar_estoque()
    elif opcao == '2':
        exibir_produtos()
    elif opcao == '3':
        cadastrar_produto()
    elif opcao == '4':
        relatorio_categoria()
    elif opcao == '5':
        relatorio_estoque_baixo()
    elif opcao == '6':
        relatorio_quantidade_total()
    elif opcao == '7':
        consultar_produto()
    elif opcao == '8':
        break
