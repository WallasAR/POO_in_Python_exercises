from random import randint

class Bank:
    def __init__(self):
        self.accounts = []
        self.total_value = 0

    def add_account(self, account):
        if isinstance(account, CurrentAccount):
            self.accounts.append(account)
            self.total_value += account.balance
            print(f"Conta {account.number} adicionada com sucesso!")
        else:
            print("Error: Invalid account type.")

    def calculate_total_value(self):
        self.total_value = sum(account.balance for account in self.accounts)
        return self.total_value

    def __str__(self):
        return f"Banco possui {len(self.accounts)} contas cadastradas e um valor total de R${self.calculate_total_value()}"


class CurrentAccount:
    def __init__(self, balance):
        self._number = randint(1000, 9999)
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    @property
    def number(self):
        return self._number

    def credit(self, amount):
        self._balance += amount

    def debit(self, amount):
        if amount <= self.balance:
            self._balance -= amount
        else:
            print("Insufficient balance")
            
    def transfer(self, amount, destination_account):
        if amount <= self.balance:
            self.debit(amount)
            destination_account.credit(amount)
        else:
            print("Saldo insuficiente para transferência")

    def __str__(self):
        return f"\nConta Corrente\n--------------\nNúmero da conta: {self.number}\nSaldo: R${self.balance}\n"


class SavingsAccount(CurrentAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self._interest_rate = interest_rate

    def accrue_interest(self):
        self._balance += self._balance * self._interest_rate

    def __str__(self):
        return f"\nConta Poupanca\n--------------\nNúmero da conta: {self.number}\nSaldo: R${self.balance}\nTaxa de juros: {self._interest_rate * 100}%\n"
    

class TaxAccount(CurrentAccount):
    def __init__(self, balance, tax_percentage):
        super().__init__(balance)
        self._tax_percentage = tax_percentage

    def calculate_tax(self):
        tax = self.balance * self._tax_percentage
        self._balance -= tax

    def __str__(self):
        return f"\nConta Imposto\n--------------\nNúmero da conta: {self.number}\nSaldo: R${self.balance}\nPercentual de imposto: {self._tax_percentage * 100}%\n"

    
# ---------------------------------
def main():
    # Criar instâncias
    account1 = CurrentAccount(balance=1000)
    account2 = SavingsAccount(balance=2000, interest_rate=0.05)  # 5% de juros
    account3 = TaxAccount(balance=3000, tax_percentage=0.1)  # 10% de imposto

    # Criar instância do Banco
    bank = Bank()
    
    # Adicionar contas ao banco
    bank.add_account(account1)
    bank.add_account(account2)
    bank.add_account(account3)
    
    # Mostrar estado do banco e o valor total nas contas
    print(bank)
    
    # Testar métodos de ContaCorrente
    print("Antes de creditar e debitar:")
    print(account1)
    
    account1.credit(500)
    account1.debit(200)
    print("Após creditar e debitar:")
    print(account1)

    # Testar transferência
    print("Antes da transferência:")
    print(account1)
    print(account2)
    account1.transfer(300, account2)
    print("Após transferência:")
    print(account1)
    print(account2)

    # Testar ContaPoupanca
    print("Antes de render juros:")
    print(account2)
    account2.accrue_interest()
    print("Após render juros:")
    print(account2)

    # Testar ContaImposto
    print("Antes de calcular imposto:")
    print(account3)
    account3.calculate_tax()
    print("Após calcular imposto:")
    print(account3)

    # Mostrar estado do banco e o valor total nas contas
    print(bank)
    
if __name__ == "__main__":
    main()
