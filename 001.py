# Minha primeira classe/objeto
# Utilizando a linguagem python, implemente a classe e o objeto que você pensou na aula passada.
# Dica: 
# 1.A classe tem que ter pelo menos um atributo mutável.
# 2. Os métodos devem ter relação com algum atributo mutável.

class Console:
    # Atributos da classe
    marca = None  # Marca do console
    nome = None  # Nome do console
    formato = None  # Formato do console (por exemplo, "portátil" ou "de mesa")
    status = False  # Status do console (ligado/desligado)
    midia_atual = False  # Indica se há uma mídia inserida no console no momento
    midia = ""  # Nome da mídia inserida no console
    joystick = False  # Indica se um joystick está conectado ao console

    # Método para ligar o console
    def on(self):
        if (self.status):
            print(f"O {self.nome} já está ligado!")
        else:
            self.status = True
            print(f"{self.nome} Ligado.")

    # Método para desligar o console
    def off(self):
        if (self.status):
            if (not self.midia_atual):
                self.status = False
                self.midia = ""
                print(f"{self.nome} Desligado.")
            else:
                print("Por favor, retire a mídia antes de desligar!")
        else:
            print(f"O {self.nome} já está desligado!")

    # Método para conectar um joystick ao console
    def connectJoystick(self):
        if self.joystick:
            print("Joystick já está conectado!")
        else:
            self.joystick = True
            print("Joystick conectado!")

    # Método para inserir uma mídia no console
    def inputMidia(self, midia):
        if (self.status):
            if not (self.midia_atual):
                if (self.joystick):
                    self.midia_atual = True
                    print(f"Abrindo {midia}...")
                    self.midia = midia
                else:
                    print("Conecte o controle primeiro!")
            else:
                print(f"Já existe uma mídia de nome {self.midia} no console, retire-a!")
        else:
            print(f"Ligue o {self.nome} primeiro!")

    # Método para retirar a mídia do console
    def outputMidia(self):
        if (self.status):
            if (self.midia_atual):
                self.midia_atual = False
                print(f"Retirando {self.midia}...")
                self.midia = ""
            else:
                print("Não existe nenhuma mídia inserida no console!")
        else:
            print(f"Ligue o {self.nome} primeiro!")

    def statusConsole(self):
        print(f'''
        - Marca: {self.marca}
        - Nome/Modelo: {self.nome}
        - Formato: {self.formato}
        - Status: {self.status}
        - Mídia instalada: {self.midia_atual}
        - Nome da midia instalada: {self.midia}
        - Controle conectado: {self.joystick}\n''')

# ============================================================================================
            
console01 = Console()
console01.marca = "Nintendo"
console01.nome = "Nintendo 64"
console01.formato = "De mesa"


# Ligando o objeto console
console01.on()
# Conectando o controle
console01.connectJoystick()
# Tentando retirar uma midia inexistente do console
console01.outputMidia()
# Colocando a midia no console
console01.inputMidia("The Legend of Zelda: Ocarina of Time")
# Tentando colocar outra midia sem retirar a ultima colocada
console01.inputMidia("Mario 64")
# Retirando a midia anterior
console01.outputMidia()
# Novamente tentando colocar outra midia
console01.inputMidia("Mario 64")
# Tentando desligar o console
console01.off()
# Retirando a midia
console01.outputMidia()
# Tentando novamente desligar o console
console01.off()
# Verificando status atual do objeto
console01.statusConsole()