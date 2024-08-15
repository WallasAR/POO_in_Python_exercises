class Battery:
  # Constructor
  def __init__(self, code, capacity, chargePercentage):
    self.__code = code # Identifier
    self.__capacity = capacity # In mAh
    self.__chargePercentage = chargePercentage # Currently charge value. limit 0% at 100% 
  
  # Methods
  def ChargeBattery(self, percentage):  # Update atribute chargePercentage. Criticize so as not to exceed 100%.
    if (percentage + self.chargePercentage <= 100 and percentage > 0):
      self.chargePercentage += percentage
      print(f"Carga atual: { self.chargePercentage }%")
    else:
      print("O valor não pode ultrapassar o limite de carga(100%)") 
  
  def DischargeBattery(self, percentage):
    if (percentage - self.chargePercentage >= 0 and percentage > 0):
      self.chargePercentage += percentage
      print(f"Carga atual: { self.chargePercentage }%")
    else:
      print("O valor não pode ultrapassar o limite mínimo de carga(0%)") 
  
  # getter and setter for percentage
  @property
  def chargePercentage(self):
    return self.__chargePercentage
  
  @chargePercentage.setter
  def chargePercentage(self, val):
    self.__chargePercentage = val  

class Smartphone:
  # Constructor
  def __init__(self, mei, battery=None):
    self.__mei = mei
    self.__battery = battery
    self.__wifi = False
    self.__status = False
    
  # Methods
  def onOff(self):
    if (self.battery):
      if (self.battery.chargePercentage > 0):
        self.status = not self.status
        print(f"Carga atual: { self.battery.chargePercentage }%")
      else:
        print("Bateria insuficiente.")
    else:
      print("Bateria desconectada")
      
  def batteryInput(self, battery):
    if (not self.battery):
      self.battery = battery
      print("Bateria OK")
    else:
      print("Bateria já conectada.")
      
  def batteryOutput(self):
    if (self.battery):
      self.battery = None
      self.status = False
      print("Bateria desconectada.")
    else:
      print("Nenhuma bateria conectada.")
  
  def onOffWifi(self):
    if (self.battery):
      self.wifi = not self.wifi
      print("Wi-Fi: ", "ligado" if self.wifi else "desligado")
    else:
      print("Nenhuma bateria conectada.")
      
  def watchVideo(self, time):
    if (self.battery):
      if (self.battery.chargePercentage > 0):  
        if (self.wifi):
          dischargePercent = time * 5
          if (self.battery.chargePercentage >= dischargePercent):
            self.battery.chargePercentage -= dischargePercent
            print(f"Consumiu { dischargePercent }% de bateria")
            print(f"Carga atual: { self.battery.chargePercentage }%")
          else:
            print("Sem bateria suficiente para assistir o vídeo.")
        else:
          print("Wi-Fi desligado.")
      else:
        print("Bateria insuficiente.")
    else:
      print("Bateria desconectada.")
      
  def charge(self, val):
    if (self.battery):
      self.battery.chargePercentage += val
      print(f"Carga atual: { self.battery.chargePercentage }%")
    else:
      print("Bateria desconectada.")
      
  def discharge(self, val):
    if (self.battery):
      self.battery.chargePercentage -= val
      print(f"Carga atual: { self.battery.chargePercentage }%")
    else:
      print("Bateria desconectada.")
  
  # getters and setters for all attributes
  @property
  def mei(self):
    return self.__mei
  
  @mei.setter
  def mei(self, val):
    self.__mei = val
  
  @property
  def battery(self):
    return self.__battery
  
  @battery.setter
  def battery(self, val):
    self.__battery = val
  
  @property
  def wifi(self):
    return self.__wifi
  
  @wifi.setter
  def wifi(self, val):
    self.__wifi = val
  
  @property
  def status(self):
    return self.__status;
  
  @status.setter
  def status(self, val):
    self.__status = val;