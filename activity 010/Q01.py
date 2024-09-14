# Classe base Produto, que representa produtos em geral
class Product:
    def __init__(self, name, price):
        # Atributos protegidos: nome e preço do produto
        self._name = name
        self._price = price
    
    # Getters
    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price
    
    # Método para calcular o desconto (deve ser implementado nas subclasses)
    def discount(self):
        raise NotImplementedError("Desconto não implementado!")

# Classe Eletrônicos, que herda de Produto e implementa um desconto de 10%
class Electronics(Product):
    def discount(self):
        priceDiscount = self._price - (self._price * 0.1) # 10% de desconto
        return priceDiscount

# Classe Móveis, que herda de Produto e implementa um desconto de 15%
class Furniture(Product):
    def discount(self):
        priceDiscount = self._price - (self._price * 0.15) # 15% de desconto
        return priceDiscount

# Classe Vestuário, que herda de Produto e implementa um desconto de 5%
class Clothing(Product):
    def discount(self):
        priceDiscount = self._price - (self._price * 0.05) # 5% de desconto
        return priceDiscount

# Classe Carrinho de Compras que contém uma lista de produtos
class Card:
    def __init__(self):
        # Lista privada que armazena os produtos no carrinho
        self.__products = []
    
    # Método para adicionar produtos ao carrinho
    def addToCard(self, product):
        # Verifica se o objeto é uma instância da classe Produto
        if isinstance(product, Product):
            self.__products.append(product)  # Adiciona o produto à lista
        else:
            raise ValueError("O produto deve ser um objeto da classe Product!")  # Levanta exceção se o produto não for da classe correta
    
    # Método para limpar o carrinho
    def clearCard(self):
        self.__products.clear()  # Limpa a lista de produtos do carrinho
    
    # Método para calcular o preço total sem descontos
    def priceWithoutDiscount(self):
        price = 0
        # Soma os preços originais dos produtos no carrinho
        for product in self.__products:
            price += product.price
        return price  # Retorna o total sem desconto

    # Método para gerar a descrição do carrinho, com detalhes de cada produto
    def description(self):
        description = ""  # String para armazenar a descrição dos produtos
        total = 0  # Variável para o total com desconto

        # Verifica se há produtos no carrinho
        if (len(self.__products) > 0):
            # Para cada produto, adiciona detalhes à descrição e soma os valores
            for product in self.__products:
                description += (
                    f"Nome do produto: {product._name}\n"
                    f"Preço bruto: R$ {product._price:.2f}\n\n"
                )
                total += product.discount()
        else:
            return "\nCarrinho Vazio"  # Retorna se o carrinho estiver vazio
        
        # Retorna a descrição com o total com desconto e sem desconto
        return description.strip() + f"\nTotal com desconto : R$ {total:.2f}\nTotal sem desconto : R$ {self.priceWithoutDiscount():.2f}"

    # Método especial __str__ para imprimir a descrição do carrinho
    def __str__(self):
        return self.description()  # Chama o método description para gerar a string


# ----------------------------------------------------------------
# Instanciando produtos de diferentes tipos
p1 = Electronics("Galaxy K10", price=1299.99)  
p2 = Furniture("Espelho", price=865.42)  
p3 = Clothing("Calça", price=120) 

# Instanciando o carrinho de compras
card = Card()

# Adicionando os produtos ao carrinho
card.addToCard(p1)
card.addToCard(p2)
card.addToCard(p3)

# Imprimindo a descrição do carrinho com os produtos e seus descontos
print(card)

# Limpando o carrinho
card.clearCard()

# Imprimindo o carrinho vazio
print(card)
