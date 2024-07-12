from datetime import datetime, date, timedelta
import time
import sys 
import os

# função para limpar tela
clear = lambda: os.system("cls")

# função para deletar ultima linha no console(apenas para visualização mais agradável).
def deleteLastLines(n=1): 
    for _ in range(n): 
        sys.stdout.write('\x1b[1A') 
        sys.stdout.write('\x1b[2K') 

class MedicAppointment:
    # Construtor
    def __init__(self, dateQuery, pacient, doctor):
        # Atributos private
        self.__isPay = False # pago
        self.__doctor = doctor # Médico
        self.__isCancel = False # cancelado
        self.__pacient = pacient # paciente
        self.__dateReturn = None # data de retorno
        self.__queryDate = self.validation(dateQuery) # data de consulta

    # Método para validar data de consulta
    def validation(self, dateQuery):
        try:
            d = datetime.strptime(dateQuery, "%d/%m/%Y").date()
            if (d <= date.today() or d.weekday() in [5,6]):
                clear()
                print("[-] Data inválida. Deve ser maior que a data atual e precisa ser em dia util.")
                return None
            return d  
        except:
            clear()
            raise ValueError("[?] Formato ou data inválida. Utilize o formato dd/mm/aaaa.")

    # Método para pagar consulta agendada
    def payConsultation(self):
        if (self.__isCancel):
          print("[?] Não é possível pagar uma consulta cancelada.")
        elif (self.__isPay):
          print("[?] Não é possível pagar uma consulta já paga.")
        else:
            self.__isPay = True
            print(f"[+] Consulta do paciente {self.__pacient} paga com sucesso.")

    # Método para cancelar consulta agendada
    def cancelConsultation(self):
        if (self.__isCancel):
            print("[?] Não é possível cancelar uma consulta já cancelada.")
        elif (self.__isPay):
            self.__isCancel = True
            self.__isPay = False
            print("[?] A consulta foi paga. O cancelamento irá ser realizado e o debito será estornado")
        else:
            self.__isCancel = True
            print(f"[+] Consulta do paciente {self.__pacient} cancelada com sucesso.")

    # Método que marca a data de retorno do paciente
    def scheduleReturn(self, dateReturnPacient):
        if (self.__isCancel):
            if (self.__isPay):
                limitDate = self.__queryDate + timedelta(days=30)
                dateReturnChosen = datetime.strptime(dateReturnPacient, "%d/%m/%Y").date()
                
                if (dateReturnChosen <= limitDate and dateReturnChosen != self.__dateReturn and dateReturnChosen >= date.today()):
                    if (dateReturnChosen.weekday() not in [5,6]):
                        self.__dateReturn = dateReturnChosen
                        print(f"[+] Retorno agendado para o dia {self.__dateReturn}.")
                    else:
                        print("[-] O dia escolhido não é um dia util.")
                else:
                    print("[-] O prazo de retorno ultrapaça os 30 dias úteis ou a data de retorno é inválida")
            else:
                print("[-] Só é possível agendar retorno para consultas pagas.")
        else:
            print("[-] Não é possivel agendar retorno, a consulta foi cancelada.")
            
    # Interface do Sistema
    # Funcionalidade que permite definir métodos que podem ser chamados em uma classe sem a necessidade de uma instância da classe.
    @staticmethod 
    def interface():
        # Array que salva as consultas feitas
        appoimentReportArray = []
        
        # Menu
        while True:
            # Pequeno timeout para visualização das operações
            if (appoimentReportArray or appoimentReportArray == []):
                time.sleep(2) # Delay de 2 segundos

            print('''
                  
                                                                                  

                                                                
                     +-++++++++++++++++++-+                     
                   ++..+++++++++++++++++-.-+                    
                  ++.  .++++++++++++++++.  -+                   
                 +-.    -++++++++++++++.    .-+                 
               +-.      .-++++++++++++-       .-+               
            ++-.         .+++++++++++-.         .-+             
         ++--.            .++++++++++.            .--+          
         +-..              -++++++++.              ..-+         
        +++++--..          .-++++++-           ..--++++         
         ++++++++--...      .+++++-.      ..--+++++++++         
         +++++++++++++--..   .+++-.   ..--+++++++++++++         
         +++++++++++++++++--..-++..---++++++++++++++++          
         +++++++++++++++++++++++++++++++++++++++++++++          
         ++++++++++++++++++----++---++++++++++++++++++          
         ++++++++++++++--..  .-++-.  ..--++++++++++++++         
         +++++++++---..      -++++-      ..--++++++++++         
        ++++++--..          -++++++.          ..--+++++         
        ++--..             .++++++++.             ..--+         
         +--.             .-++++++++-.            ..-++         
           ++-..          -++++++++++-          .--+            
              +--.       -++++++++++++.       .-++              
                +-.     .+++++++++++++-.     -++                
                  +-.  .-++++++++++++++-   .-+                  
                   +-. -++++++++++++++++- .++                   
                    +--++++++++++++++++++-++                    
                      ++++           ++++                       
                                                                
                                                            Version. 1.0-Alpha 
                                                            UmbrellaCorporation© All rights reserved     
                                                                
                                                                
        ----------Sistema gerador de consultas---------- 
        | Options
        ↳ 1 - Nova consulta (agendamento)
        ↳ 2 - Pagar Consulta
        ↳ 3 - Cancelar consulta
        ↳ 4 - Agendar retorno
        ↳ 5 - Relatório de consultas realizadas no mês por médico
        ↳ 6 - Relatório de faturamento da Clinica por mês                                         
        ''')
            
            try:  
                # Escolha do user
                choice = int(input("☐ "))
            
                # Apagando do console a escolha feita
                if (choice):
                    deleteLastLines()
                
            
                if (choice == 1):
                    print("☑ 1 - Nova consulta (agendamento)")
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                # tratamento de erro try/except
                    try:
                        queryDate = str(input("• Data da consulta (dd/mm/aaaa): "))
                        pacient = str(input("• Nome do paciente: "))
                        doctor = str(input("• Nome do médico: "))

                        newQuery = MedicAppointment(queryDate, pacient, doctor) # Criação de objeto

                        # Verifica se a consulta foi criada com base na data
                        if (newQuery.__queryDate):
                            # Adiciona o objeto ao array
                            appoimentReportArray.append(newQuery)
                            clear()
                            print(f"[+] Consulta agendada para o dia {newQuery.__queryDate} com o(a) Dr(a). {newQuery.__doctor}")
                    except ValueError as e:
                        print(e)

                elif (choice == 2):
                    print("☑ 2 - Pagar Consulta Selecionado")
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    pacient = str(input("• Nome do paciente: "))

                    queryPayment = next(
                    (query for query in appoimentReportArray  # Itera sobre cada consulta "query" na lista "appoimentReportArray"
                    if query.__pacient == pacient),  # Verifica se o paciente da consulta é o paciente especificado
                    None  # Retorna "None" se nenhuma consulta atender às condições
                    )

                    # Verifica se o objeto(cumprindo todas as condições) foi encontrado
                    if (queryPayment):
                        clear()
                        # Chama o método para cancelar a consulta
                        queryPayment.payConsultation()
                    else:
                        clear()
                        print("[-] Paciente não encontrado.")

                elif (choice == 3):
                    print("☑ 3 - Cancelar consulta Selecionado")
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    pacient = str(input("• Nome do paciente: "))

                    queryCancel = next(
                        (c for c in appoimentReportArray
                        if c.__pacient == pacient),
                        None
                    )
                    # Verifica se a opção retornou resultados para a chamada do método
                    if (queryCancel):
                        clear()
                        queryCancel.cancelConsultation()
                    else:
                        clear()
                        print("[-] Paciente não encontrado.")

                elif (choice == 4):
                    print("☑ 4 - Agendar retorno Selecionado")
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    pacient = str(input("• Nome do paciente: "))
                    queryReturn = str(input("• Data do retorno (válido por até 30 dias): "))

                    queryDateReturn = next(
                        (query for query in appoimentReportArray
                        if query.__pacient == pacient),
                        None
                    )
                
                    if (queryDateReturn):
                        clear()
                        queryDateReturn.scheduleReturn(queryReturn)
                    else:
                        clear()
                        print("[-] Paciente não encontrado.")
                        
                elif (choice == 5):
                    print("☑ 5 - Relatório de consultas realizadas no mês por médico")
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    doctor = str(input("• Nome do médico: "))
                    
                    doctorQuery = [
                        query for query in appoimentReportArray
                        if query.__doctor == doctor 
                        and query.__queryDate.month == date.today().month # Verifica se a data corresponde ao mês atual
                        ]
                        
                    if (doctorQuery):  
                        clear()  
                        print(f"[+] Consultas realizadas no mês pelo médico {doctor}: ")
                        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    
                        for queryReport in doctorQuery:
                            print(f"| {queryReport.__queryDate} ↦ Paciente {queryReport.__pacient}")
                        time.sleep(2)
                    else:
                        clear()
                        print("[-] Medico não encontrado.")
                        
                elif (choice == 6): 
                    print("☑ 6 - Relatório de faturamento da Clinica por mês")
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    # A cada consulta encontrada suprindo todas as condições irá ser adicionado +100, após percorrer todo o array de objects irá fazer a soma
                    billingReport = sum(
                        100 for query in appoimentReportArray 
                        if query.__isPay 
                        and query.__queryDate.month == date.today().month 
                        )
                    
                    if (billingReport):
                        print("//////////////////////////////////////////////////////////////")
                        print(f"| Mês \n ↳ {date.today().strftime("%B")}")
                        print(f"| Lucro bruto total \n ↳ R$ {(billingReport * 3):.2f}")
                        print(f"| Pagamento dos médicos \n ↳ - R$ {(billingReport * 2):.2f}")
                        print(f"| Total \n ↳ R$ {billingReport:.2f}")
                        time.sleep(5)
                    else:
                        clear()
                        print("[-] Não há registros sobre o faturamento da clinica no momento.")
                        
                else:
                    clear()
                    print("☒ Opção inválida")
            except:
                raise ValueError("[-] A resposta deve ser um numero inteiro correspondente a opção.")
# Função principal, chama o metodo estático "interface" para inicialização do sistema
def main():
    MedicAppointment.interface()

if __name__ == "__main__":
    main()