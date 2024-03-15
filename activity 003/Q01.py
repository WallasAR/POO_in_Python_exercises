# Utilizando o processo de abstração, implemente uma classe em python que represente uma carteira de habilitação. Identifique atributos mutáveis e imutáveis, implemente um construtor da classe e métodos para manipulação dos atributos mutáveis. Faça todas as validações possíveis. Crie objetos para testar os métodos implementados.

from datetime import datetime

class CNH:
    seq = 0  # Atributo de classe para sequência de números de CNHs

    def __init__(self, data_emissao, data_vencimento, nome):
        CNH.seq += 1
        self.numero = CNH.seq  # Atributo numérico sequencial para o número da CNH
        self.data_emissao = self.validar_data(data_emissao)  # Data de emissão validada
        self.data_vencimento = self.valida_vencimento(data_vencimento)  # Data de vencimento validada
        self.nome = nome  # Nome do titular da CNH

    def validar_data(self, data_validade):
    
        # Método para validar a data de emissão.

        try:
            data = datetime.strptime(data_validade, '%d/%m/%Y')  # Tenta converter a string para um objeto de data
            return data  # Se bem sucedido, retorna a data

        except ValueError:
            raise ValueError("Formato ou data inválida. Utilize o formato dd/mm/aaaa.")  # Caso contrário, levanta um erro

    def valida_vencimento(self, data):

        # Método para validar a data de vencimento.
        d = self.validar_data(data)  # Valida a data
        if d.date() > datetime.now().date():  # Verifica se a data de vencimento é futura
            return d  # Se for, retorna a data
        else:
            raise ValueError("Data de vencimento inválida!")  # Caso contrário, levanta um erro

    def __str__(self):

        # Método especial para retornar uma representação em string do objeto CNH.
        return f'Numero do registro: {self.numero}\nData de emissão: {self.data_emissao.strftime("%d/%m/%Y")}\nData Vencimento: {self.data_vencimento.strftime("%d/%m/%Y")}'

# ===========================
    
cnh1 = CNH('05/03/2019', '05/04/2024', "Jose Antonio Santana")

atual_data = datetime.now().date()  # Data atual
print(type(atual_data))  # Imprime o tipo da data
print("Data atual:", atual_data)  # Imprime a data atual

diferenca_tempo = atual_data - cnh1.data_emissao.date()  # Calcula a diferença de tempo
print("Dias desde emissão:", diferenca_tempo.days)  # Imprime os dias desde a emissão

data_vencimento_nova = cnh1.data_emissao + diferenca_tempo  # Calcula a nova data de vencimento
print("Nova data de vencimento:", data_vencimento_nova.strftime("%d/%m/%Y"))  # Imprime a nova data de vencimento
