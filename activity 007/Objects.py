from Classes import Smartphone, Battery

# Criação das instâncias
S10PlusBattery = Battery("S10KENB2537", 5000, 10)
POCOF6Battery = Battery("S20KENB4567", 4000, 50)
GalaxyM54Battery = Battery("S21KENB7890", 6000, 80)

S10Plus = Smartphone("SDAF258", S10PlusBattery)
POCOF6 = Smartphone("SDAF259")
GalaxyM54 = Smartphone("SDAF260", GalaxyM54Battery)

# Teste dos métodos para S10Plus
print("Teste S10Plus:")
S10Plus.onOff()  # Deve ligar e mostrar a carga
S10Plus.onOffWifi()  # Deve ligar o Wi-Fi
S10Plus.watchVideo(5)  # Deve descarregar a bateria
S10Plus.charge(20)  # Deve carregar a bateria
S10Plus.discharge(15)  # Deve descarregar a bateria
S10Plus.batteryOutput()  # Deve desconectar a bateria
S10Plus.onOff()  # Deve mostrar que a bateria está desconectada

# Teste dos métodos para POCOF6
print("\nTeste POCOF6:")
POCOF6.batteryInput(POCOF6Battery)  # Deve conectar a bateria
POCOF6.onOffWifi()  # Deve ligar o Wi-Fi
POCOF6.watchVideo(10)  # Deve descarregar a bateria
POCOF6.charge(30)  # Deve carregar a bateria
POCOF6.batteryOutput()  # Deve desconectar a bateria
POCOF6.onOff()  # Deve mostrar que a bateria está desconectada

# Teste dos métodos para GalaxyM54
print("\nTeste GalaxyM54:")
GalaxyM54.onOff()  # Deve ligar e mostrar a carga
GalaxyM54.onOffWifi()  # Deve ligar o Wi-Fi
GalaxyM54.watchVideo(2)  # Deve descarregar a bateria
GalaxyM54.charge(15)  # Deve carregar a bateria
GalaxyM54.discharge(25)  # Deve descarregar a bateria
GalaxyM54.batteryInput(GalaxyM54Battery)  # Deve conectar a bateria novamente
GalaxyM54.onOff()  # Deve ligar e mostrar a carga atual
