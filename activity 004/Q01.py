estacoes = {89.5:"Cocais", 91.5:"Mix", 94.1:"Boa", 99.1:"Clube"}

class RadioFM:
    # Construtor
    def __init__(self, vol_max, estacoes):
        self.vol_min = 0
        self.vol_max = vol_max
        self.freq_min = 88
        self.freq_max = 108
        self.estacoes = estacoes
        self.vol = None
        self.ligado = False
        self.estac_atual = None
        self.freq_atual = None
        self.antena_hab = False

    # Metodos
    def hab_desab_antena(self):
        if (self.antena_hab):
            self.antena_hab = False
            print("Desabilitando antena...")
        else:
            self.antena_hab = True
            print("Habilitando antena..")

    
    # No método ligar, atualizar o atributo ligado para True, o volume do rádio deverá ser inicializado com o volume mínimo do rádio. Se a antena estiver habilitada (antena_habilitada=True), a frequencia deverá ser inicializada com a frequencia da primeira estação de rádio definida no dicionário e a estação atual deverá ser inicializada com seu respectivo nome.
    def lig_desl(self):
        if (self.ligado):
            self.ligado = False
            print("Desligando")

            self.vol = None
            self.freq_atual = None
            self.estac_atual = None
        else:
            self.ligado = True
            print("Ligando")

            self.vol = self.vol_min

            if (self.antena_hab):
                self.freq_atual = 89.5
                self.estac_atual = estacoes.get(89.5)
                print(f"Estação atual: {self.freq_atual}\nVocê está na {self.estac_atual} FM!")


    # O método aumentar_volume deverá receber um atributo opcional com valor inicial igual a 1. Caso este valor seja passado na chamada do argumento, atualizar o volume com o valor do argumento (fazer a crítica para não ultrapassar os valores permitidos para o volume). Caso o argumento fique vazio na chamada, o atributo volume deverá ser incrementado de uma unidade. (Fazer a crítica para não ultrapassar o valor máximo permitido)
    def aumentar_volume(self, vol = 1):
        if (self.ligado):
            if (vol + self.vol >= self.vol_max):
                print("Volume maximo atingido!")
                self.vol = self.vol_max
            else:
                self.vol += vol
                print(f"Volume atual: {self.vol}")
        else:
            print("Ligue o aparelho primeiro!")
    
    def diminuir_volume(self, vol = -1):
        if (self.ligado):
            if (vol + self.vol <= 0):
                print("Volume minimo atingido!")
                self.vol = self.vol_min
            else:
                self.vol += vol
                print(f"Volume atual: {self.vol}")

    # O método mudar_frequencia deverá receber um atributo opcional com valor inicial igual a 0. Caso seja passado um valor para a frequencia na chamada deste método, atualizar o atributo frequencia_atual para o valor passado no argumento. Se o valor da frequencia estiver presente no dicionário, atualizar o atributo: estação_atual com o nome da respectiva frequencia que se encontra no dicionário, caso contrário atualizar com o valor: ‘estação inexistente’. Caso este método seja chamado sem argumentos, atualizar a frequencia_atual com a frequência referente ao próximo elemento do dicionário e atualizar o atributo: estação_atual com seu respectivo nome. Se a frequencia atual for igual ao último elemento do dicionário, mudar os atributos: frequencia e estação para os respectivos valores referentes ao primeiro elemento do dicionário.
    def mudar_frequencia(self, freq = 0):
        if (self.ligado):
            if (self.antena_hab):
                if (freq in estacoes):
                    self.freq_atual = freq
                    self.estac_atual = estacoes.get(freq)
                    print(f"\n[+] Estação atual: {self.freq_atual}\nVocê está na {self.estac_atual} FM!\n")

                elif (freq == 0):
                    keys = list(estacoes.keys()) #  lista de todas as chaves do dicionário 
                    current_index = keys.index(self.freq_atual) # ncontra o índice da frequência atual, diz onde na lista de frequências estamos atualmente.
                    next_index = (current_index + 1) % len(keys) # determina o proxima frequencia da lista, a operação com o modulo garante que ele irá voltar a primeira estação
                    self.freq_atual = keys[next_index]
                    self.estac_atual = estacoes[self.freq_atual]
                    print(f"\n[+] Estação atual: {self.freq_atual}\nVocê está na {self.estac_atual} FM!\n")

                else:
                    print("estação inexistente")
            else:
                  print("Habilite a antena para esta operação!")
        else:
            print("Ligue o aparelho primeiro!")

    def __str__(self):
        return f"\nSTATUS\n - Ligado: {self.ligado}\n - Antena: {self.antena_hab}\n - Volume máximo: {self.vol_max}\n - Volume Atual: {self.vol}\n - Frequencia atual: {self.freq_atual}\n - Estação atual: {self.estac_atual}"
# =====================================================
# Criar pelo menos 3 objetos e testar os métodos implementados.
    
# Rádio 01
r1 = RadioFM(20, estacoes)
r1.hab_desab_antena()

r1.lig_desl()
r1.aumentar_volume()
r1.diminuir_volume()
r1.mudar_frequencia(99.9)

print(f"{r1}\n")

# Rádio 02
r2 = RadioFM(15, estacoes)
r2.hab_desab_antena()

r2.lig_desl()
r2.lig_desl()
r2.aumentar_volume()
r2.diminuir_volume(-6)
r2.mudar_frequencia(100.0)

print(f"{r2}\n")

# Rádio 03
r3 = RadioFM(10, estacoes)

r3.hab_desab_antena()
r3.lig_desl()
r3.aumentar_volume(15)
r3.diminuir_volume(-3)
r3.mudar_frequencia(94.1)
r3.mudar_frequencia()
r3.mudar_frequencia(91.5)

print(f"{r3}\n")