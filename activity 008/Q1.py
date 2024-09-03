from datetime import datetime

class Team:
    def __init__(self, name, state):
        self.__name = name
        self.__players = []
        self.__state = state


    def addPlayer(self, player): 
        if (player.age() >= 18):
            if (player.team == None):
                self.__players.append(player)
                player.team = self
                print(f"{player.name} adicionado ao time")
            else:
                print("jogador já está em um time!")
        else:
            print("jogador não é maior de idade!")

    def deletePlayer(self, player):
        if player in self.__players:
            player.team = None
            self.__players.remove(player)
            print(f"{player.name} removido do time {self.__name}")
        else:
            print("jogador não encontrado!")

    def transferPlayer(self, player, team):
        if (player.age() >= 18):
            if player in self.__players:
              print(f"Transferindo {player.name} para {team.__name}")
              self.deletePlayer(player)
              team.addPlayer(player)
            else:
              print("jogador não encontrado!")
        else:
            print("jogador não é maior de idade!")

    def showPlayer(self):
        return "\n".join([str(p) for p in self.__players]) if self.__players else None

    def __str__(self):
        print("-------------------------------------------")
        return f"Nome: {self.__name}\nEstado: {self.__state}\nLista de jogadores: \n-------------------\n{ "Vazio" if self.showPlayer() is None else self.showPlayer()}"

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, val):
        self.__name = val
    
class Player:
    def __init__(self, name, birthday, position, team=None):
        self.__name = name
        self.__birthday = birthday
        self.__position = position
        self.__team = team  

    
    def age(self):
        birthday = datetime.strptime(self.__birthday, "%d/%m/%Y")
        today = datetime.today()
        age = today.year - birthday.year
        if (today.month, today.day) < (birthday.month, birthday.day):
            age -= 1
        return age

    def __str__(self):
        return f"Jogador: {self.__name}\nPosição: {self.__position}\n"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, val):
        self.__position = val

    @property
    def team(self):
        return self.__team
    
    @team.setter
    def team(self, val):
        self.__team = val

class Championship:
    def __init__(self, teamAmount):
        self.__teamAmount = teamAmount
        self.__teams = {}
        self.__matches = []
        
    def addTeam(self, team):
        if team not in self.__teams:
            if team.name not in self.__teams:
                if (len(self.__teams) + 1 <= self.__teamAmount):
                    self.__teams[team.name] = 0
                    print(f"{team.name} adicionado ao campeonato")
                else:
                    print(f"Limite de times atingido!")
            else:
                print(f"{team.name} já existe no campeonato")
        else:
            print(f"{team.name} já está em um campeonato!")
            
    def match(self, homeTeam, awayTeam, homeTeamScoreboard, awayTeamScoreboard):
        if homeTeam.name in self.__teams and awayTeam.name in self.__teams:
            print("--------------------------")
            print(f"|{ homeTeam.name } x { awayTeam.name }|")
            print("--------------------------")
            
            if (homeTeamScoreboard > awayTeamScoreboard):
                self.__teams[homeTeam.name] += 3
                print(f"{homeTeam.name} venceu a partida contra {awayTeam.name} por {homeTeamScoreboard} a {awayTeamScoreboard}")
                
            elif (homeTeamScoreboard < awayTeamScoreboard):
                self.__teams[awayTeam.name] += 3
                print(f"{awayTeam.name} venceu a partida contra {homeTeam.name} por {homeTeamScoreboard} a {awayTeamScoreboard}")
                
            else:
                self.__teams[homeTeam.name] += 1
                self.__teams[awayTeam.name] += 1
                print(f"Empate na partida entre {homeTeam.name} e {awayTeam.name} por {homeTeamScoreboard} a {awayTeamScoreboard}")
            
            self.__matches.append({
                "homeTeam": homeTeam.name,
                "awayTeam": awayTeam.name,
                "homeTeamScoreboard": homeTeamScoreboard,
                "awayTeamScoreboard": awayTeamScoreboard,
            })
        else:
            print(f"{homeTeam.name} ou {awayTeam.name} não estão em um campeonato!")
    
    
    def showTeams(self):
        count = 1
        if (self.__teams):
            print("\nTimes:")
            print("-------------------------------------------")
        for team in self.__teams:
            print(f"{count}. {team}")
            count += 1
    
    def showMatches(self):
        if (self.__matches):
            print("\nJogos:")
            print("-------------------------------------------")
            for match in self.__matches:
                print(f"{match["homeTeam"]} x {match["awayTeam"]} \nScore: {match["homeTeamScoreboard"]} a {match["awayTeamScoreboard"]}\n")
        else:
            print("Nenhum jogo foi marcado!")
    
    def showClassification(self):
        if (self.__teams):
            print("\nClassificação do Campeonato")
            print("="*40)
            print(f"{'Posição':<10}{'Time':<20}{'Pontos':>10}")
            print("-"*40)
            
            for i, (team, points) in enumerate(sorted(self.__teams.items(), key=lambda item: item[1], reverse=True), start=1):
                print(f"{i:<10}{team:<20}{points:>10}")
            
            print("="*40)
        else:
            print("Nenhum time está em um campeonato!")
# -----------------------------------------

def main():
    t1 = Team("Flamengo", "RJ")
    t2 = Team("Vasco da Gama", "RJ")
    t3 = Team("Santos", "SP")
    t4 = Team("Botafogo", "RJ")

    p1 = Player("Pedro", "02/02/1990", "Goleiro")
    p2 = Player("Maria", "15/05/1985", "Zagueiro")
    p3 = Player("João", "25/08/1995", "Lateral")
    p4 = Player("Marcos", "10/07/1992", "Meio-Campo")
    p5 = Player("José", "03/06/1988", "Atacante")

    # Adiciona jogadores aos times
    t1.addPlayer(p1)
    t1.addPlayer(p2)
    t1.addPlayer(p3)
    t1.addPlayer(p4)
    t1.addPlayer(p5)

    # Criação de novos jogadores
    p6 = Player("Lucas", "15/12/2005", "Goleiro")
    p7 = Player("Ana", "22/11/2004", "Meio-Campo")

    # Adiciona jogadores sem vínculo ao time
    t2.addPlayer(p6)
    t2.addPlayer(p7)

    # Transfere um jogador de um time para outro
    t1.transferPlayer(p1, t3)

    # Exclui um jogador
    t3.deletePlayer(p1)

    # Exibe os jogadores de cada time
    print(t1)
    print(t3)
    
    # Criação de Campeaonato
    championshipSeriesA = Championship(4)
    
    # Adiciona times ao campeonato
    championshipSeriesA.addTeam(t1)
    championshipSeriesA.addTeam(t2)
    championshipSeriesA.addTeam(t3)
    championshipSeriesA.addTeam(t4)
    
    # Mostrar times no campeonato
    championshipSeriesA.showTeams()

    # Mostrar classificação dos times antes das partidas
    championshipSeriesA.showClassification()

    # Marca partidas entre times
    championshipSeriesA.match(t1, t2, 1, 3)
    championshipSeriesA.match(t4, t3, 2, 0)
    championshipSeriesA.match(t2, t4, 1, 0)
    
    # Mostrar partidas que aconteceram
    championshipSeriesA.showMatches()
    
    # Mostrar classificação dos times após as partidas
    championshipSeriesA.showClassification()
    
if (__name__ == "__main__"):
    main()