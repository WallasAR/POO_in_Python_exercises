class Person:

    # Construtor
    def __init__(self, nome, idade, peso, altura, sexo):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.sexo = sexo
        self.__estado = True # true: "vivo" && false: "morto"
        self.__estado_civil = "solteiro" # solteiro/casado/viúvo
        self.__conjugue = None

    # - Crescer: somar à altura atual da pessoa o valor que está no argumento do método, somente se a pessoa tiver até 21 anos de idade.
    def crescer(self, cm = 5):
        if (self.__estado):
            if (self.__idade < 21):
                self.__altura += cm
            else:
                print(f"\n - {self.__nome} não pode mais crescer pois está com 21 anos ou mais.")    
        else:
            print(f"\n - Operação não realizada. {self.__nome} está morto(a).")

    # - Envelhecer: atualizar em um ano a idade da pessoa. A cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm
    def envelhecer(self):
        if (self.__estado):
            self.__idade += 1
            self.crescer()
            print(f"\n - {self.__nome} está com {self.__idade} anos e {self.__altura} cm de altura.")
        else:
            print(f"\n - A operação não pode ser concluida, pois {self.__nome} está morto(a).")

    # Engordar: somar o peso atual da pessoa ao argumento valor do método
    def engordar(self, peso):
        if (self.__estado):
            self.__peso += peso
        else:
            print(f"\n - Operação não realizada. {self.__nome} está morto(a).")

    # Emagrecer: subtrair o peso atual da pessoa ao argumento valor do método
    def emagrecer(self, peso):
        if (self.__estado):
            self.__peso -= peso
            print(f"\n- {self.__nome} perdeu {self.__peso} Kilogramas.")
        else:
            print(f"\n - Operação não realizada. {self.__nome} está morto(a).")
    
    # Casar: mudar o estado civil da pessoa (self) para “casado(a)” e atribuir ao valor do atributo conjuge o objeto (pessoa) com quem a pessoa está se casando; Não permitir que pessoas casadas se casem novamente e não permitir que pessoas menores de idade se casem.
    def casar(self, conjugue):
        if (self.__estado): 
            if (self.__estado_civil in ["solteiro", "viúvo"]):
                if (self.__idade >= 18):
                    self.__estado_civil = "casado"
                    self.__conjugue = conjugue
                    conjugue.__conjugue = self
                    print(f"\n - {self.__nome} está casado(a) com {conjugue.__nome}.")
                else:
                    print(f"\n - Casamento não permitido. {self.__nome} é de menor.")
            else:
                print(f"\n - Casamento não realizado. {self.__nome} é casado.")
        else:
            print(f"\n - Casamento não realizado. {self.__nome} está morto(a).")

    #  Morrer: mudar o atributo estado da pessoa para “morto”. Nenhum dos métodos anteriores poderá ser executado se a pessoa estiver morta.
    def morrer(self):
        self.__estado = False
        print(f"\n - {self.__nome} morreu.")

    # getters e setters
    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade if (self.__estado) else f"\n - {self.__nome} está morto."

    @property
    def peso(self):
        return self.__peso

    @property
    def altura(self):
        return self.__altura

    @property
    def estado(self):
        return "vivo" if self.__estado else "morto"

    @property
    def estado_civil(self):
        return self.__estado_civil

    @property
    def conjuge(self):
        return self.__conjugue
    
    @idade.setter
    def idade(self, idade):
        print("\n - Sem permissão.")
    
# ========================================================

# Criando os objetos
Maria = Person("Maria", 5, 20, 100, "F")
Joao = Person("João", 12, 40, 140, "M")
Pedro = Person("Pedro", 22, 65, 170, "M")
Bia = Person("Bia", 18, 55, 160, "F")
Julia = Person("Julia", 30, 65, 170, "F")
Carlos = Person("Carlos", 2, 11, 80, "M")
Jonas = Person("Jonas", 34, 70, 180, "M")

# Manipulando métodos
# a) atribua a idade de maria para o valor: 10
Maria.idade = 10

# b) Maria fez aniversário. Chame o método necessário.
Maria.envelhecer()

# c) Pedro quer crescer 2 cm. Chame o método necessário.
Pedro.crescer(2)

# d) Bia quer casar com Carlos. Chame o método necessário.
Carlos.casar(Bia)

# e) Pedro quer casar com Maria. Chame o método
Maria.casar(Pedro)

# f) Pedro quer casar com Júlia.
Pedro.casar(Julia)

# g) Pedro quer casar com Bia.
Pedro.casar(Bia)

# h) Maria morreu.
Maria.morrer()

# i) Maria quer engordar.
Maria.engordar(5)

# j) Bia quer casar com Jonas.
Bia.casar(Jonas)

# k) Bia morreu.
Bia.morrer()

# l) Pedro Morreu
Pedro.morrer()

# m) Jonas quer casar com Júlia
Jonas.casar(Julia)

# n) Pedro quer casar com Bia
Pedro.casar(Bia)

# o) Mostre a idade de Pedro.
print(Pedro.idade)

# p) Atribua a idade de João para: 50
Joao.idade = 50