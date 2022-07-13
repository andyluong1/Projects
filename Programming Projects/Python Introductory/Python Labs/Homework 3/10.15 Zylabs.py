# Andy Luong 1525166
# Zylabs 10.15

class Team:
    def __init__(self, team_name = None, team_wins = 0, team_losses = 0):
        self.team_name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses

    def The_team_name(self, team_name):
        self.team_name = team_name

    def The_team_wins(self, team_wins):
        self.team_wins = team_wins

    def The_team_losses(self, team_losses):
        self.team_losses = team_losses

    def get_win_percentage(self):
        formula = self.team_wins / (self.team_wins + self.team_losses)
        return formula

if __name__ == "__main__":
    team1 = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team1.The_team_name(team_name)
    team1.The_team_wins(team_wins)
    team1.The_team_losses(team_losses)

    if team1.get_win_percentage() >= .5:
        print("Congratulations, Team " + team1.team_name + " has a winning average!")
    else:
        print("Team " + team1.team_name + " has a losing average.")