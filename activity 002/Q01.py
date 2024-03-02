# 1. Exercitando o processo de abstração, modele uma classe Rádio com seus estados e comportamentos. Crie a respectiva classe em python e depois crie 2 objetos, imprima os valores de seus atributos e execute os métodos criados e imprima os estados finais destes objetos. Recomendação: criar estados que possam ter seus valores alterados por seus métodos.

class Radio:
    def __init__(self, marca, model, vol_at, vol_max, freq_at, bat, estado):
        self.marca = marca
        self.modelo = model
        self.vol_atual = vol_at
        self.vol_max = vol_max
        self.freq_atual = freq_at
        self.bateria = bat
        self.estado = estado

    def carregarBateria(self, porcentagem):
        if (self.bateria >= 100) or (self.bateria + porcentagem >= 100):
            print("A bateria está totalmente carregada!")
            self.bateria = 100
        else:
            print("Carregando...")
            self.bateria += porcentagem

    def ligar(self):
        if (self.estado):
            print("O aparelho está ligado!")
        else:
            self.estado = True
            print("Ligando...")

    def desligar(self):
        if (not self.estado):
            print("O aparelho está desligado!")
        else:
            self.estado = False
            print("Desligando...")

    def sintonizar(self, frequencia):
        if (self.estado):
            if (self.bateria > 0):
                if (frequencia != self.freq_atual):
                    self.freq_atual = frequencia
                    print(f"{self.freq_atual} MHz/kHz selecionada!")

                else:
                    print("Mesma frequência selecionada!")
                    
                self.bateria -= 10
            else:
                self.estado = False
                print("Aparelho descarregado, utilize do método ""carregarBateria()""")
        else:
            print("Ligue o aparelho primeiro!")

    def alterVol(self, vol):
        if (self.estado):
            if (self.bateria > 0):
                if (vol + self.vol_atual >= self.vol_max):
                    print("Volume maximo atingido!")
                    self.vol_atual = 100

                elif (vol + self.vol_atual <= 0):
                    print("Volume minimo atingido!")
                    self.vol_atual = 0

                else:
                    self.vol_atual += vol
                    print(f"Volume atual: {self.vol_atual}")

                self.bateria -= 10
            else:
                self.estado = False
                print("Aparelho descarregado, utilize do método carregarBateria()")
        else:
            print("Ligue o aparelho primeiro!")

    def status(self):
        print(f'''
        Marca:{self.marca}
        Modelo: {self.modelo}
        Volume: {self.vol_atual}
        Frequência: {self.freq_atual}
        Bateria: {self.bateria}
        Estado: {self.estado}
    ''')
        
# ========================================================
# Instância Objeto 01 
            # Marca, modelo, vol_at, vol_max, freq_at, bat, estado 
radio = Radio("Parasonic", "MK1", 0, 100, 0, 10, False)
# Teste de métodos
radio.ligar()
radio.sintonizar(97.4)
radio.alterVol(80)
radio.alterVol(90)
radio.status()
radio.carregarBateria(100)
radio.status()
radio.desligar()

# Instância Objeto 02
            
radio2 = Radio("Philco", "MK2", 25, 100, 89.8, 80, False)

radio2.status()
radio2.ligar()
radio2.alterVol(70)
radio2.alterVol(-60)
radio2.desligar()