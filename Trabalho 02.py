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


# Exemplo de uso
while True:
    print("\nEscolha uma opção:")
    print("1. Movimentar estoque")
    print("2. Exibir produtos")
    print("3. Sair")
    opcao = input("Digite a opção desejada (1/2/3): ")

    if opcao == '1':
        movimentar_estoque()
    elif opcao == '2':
        exibir_produtos()
    elif opcao == '3':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Por favor, escolha 1, 2 ou 3.")