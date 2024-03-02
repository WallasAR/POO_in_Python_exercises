# 2. Melhore a classe Bicicleta, colocando limites máximos e mínimos para os estados: veloc_atual, altura_cela e calibragem_pneus através de seus respectivos métodos. Altere os métodos: regular_cela e calibrar_pneus para permitirem as mudanças caso a bicicleta esteja parada (veloc_atual=0). Execução: Criar pelo menos 2 objetos, imprimir seus estados iniciais, executar os métodos e imprimir seus estados finais.

class Bike:
    def __init__(self, peso, altura, veloc_atual, veloc_max, cor, aro, altura_cela, altura_cela_max, calibr_pneus, capac_ar_max):  
        self.peso = peso
        self.altura = altura
        self.veloc_atual = veloc_atual
        self.veloc_max = veloc_max
        self.cor = cor
        self.aro = aro
        self.altura_cela = altura_cela
        self.altura_cela_max = altura_cela_max
        self.calibragem_pneus = calibr_pneus
        self.capac_max_ar_pneus = capac_ar_max

    # Método para pedalar a bicicleta aumentando a velocidade
    def pedalar(self, veloc):
        if (veloc + self.veloc_atual <= self.veloc_max):
            self.veloc_atual += veloc 
            print(f"Velocidade atual: {self.veloc_atual} km")
        else:
            print("Velocidade máxima atingida")
            self.veloc_atual = self.veloc_max
        
    # Método para frear a bicicleta
    def frear(self, temp_freio):
        if (self.veloc_atual > 0):
            if (temp_freio < self.veloc_atual):
                self.veloc_atual -= temp_freio
                print(f"Velocidade atual: {self.veloc_atual} km")
            else:
                self.veloc_atual = 0
                print(f"Velocidade atual: {self.veloc_atual} km")
        else:
            print("A bicicleta está parada!")

    # Método para ajustar a altura da cela
    def regular_cela(self, medida):
        if (self.veloc_atual == 0):
            if (medida + self.altura_cela <= self.altura_cela_max):
                self.altura_cela += medida 
                print(f"Altura atual da cela: {self.altura_cela} cm")
            else:
                print("A medida ultrapassa a capacidade máxima!")
        else:
            print("Você está em movimento!")

    # Método para calibrar os pneus
    def calibrar_pneus(self, quant_ar):
        if (self.veloc_atual == 0):
            if (quant_ar + self.calibragem_pneus <= self.capac_max_ar_pneus):
                self.calibragem_pneus += quant_ar
                print(f"Calibragem atual: {self.calibragem_pneus} lib")
            else:
                print("A quantidade de ar ultrapassa a capacidade máxima!")
        else:
            print("Você está em movimento!")

    # Método para exibir o status da bicicleta
    def status(self):
        print(f'''
        Peso: {self.peso} kg
        Altura: {self.altura} cm
        Velocidade atual: {self.veloc_atual} km
        Velocidade máxima: {self.veloc_max} km
        Cor: {self.cor}
        Aro: {self.aro} 
        Altura da cela: {self.altura_cela} cm
        Altura máxima da cela: {self.altura_cela_max} cm
        Calibragem dos pneus: {self.calibragem_pneus} lib
        Calibragem máxima dos pneus: {self.capac_max_ar_pneus} lib
    ''')
# =====================================================
# Instância Objeto 01     
bike01 = Bike(13, 110, 0, 50, "Branca", 24, 5, 20, 20, 50)
# Teste de métodos
bike01.status()
bike01.pedalar(10)
bike01.frear(10)
bike01.regular_cela(15)
bike01.calibrar_pneus(25)
bike01.status()

# Instância Objeto 02    
bike02 = Bike(8, 145, 0, 70, "Vermelha", 26, 10, 15, 25, 40)

bike02.status()
bike02.frear(10)
bike02.pedalar(80)
bike02.frear(70)
bike02.regular_cela(15)
bike02.calibrar_pneus(25)
bike02.status()