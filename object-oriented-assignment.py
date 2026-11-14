"""
Smashmouth Football
Demonstrates Python OOP by creating Player objects and an NFLTeam object
that holds a list of those players.
"""


class Player:
    """Represents a single football player."""

    VALID_POSITIONS = {
        "QB": "Quarterback",
        "RB": "Running Back",
        "WR": "Wide Receiver",
        "K": "Kicker",
    }

    def __init__(self, playerName, playerPosition):
        if playerPosition not in Player.VALID_POSITIONS:
            raise ValueError(f"Invalid position: {playerPosition}")
        self.playerName = playerName
        self.playerPosition = playerPosition

    def __str__(self):
        full = Player.VALID_POSITIONS[self.playerPosition]
        return f"{self.playerName:<16} {self.playerPosition:<3} ({full})"


class NFLTeam:
    """Represents an NFL team with a name and a list of players."""

    def __init__(self, teamName, playerList=None):
        self.teamName = teamName
        self.playerList = list(playerList) if playerList else []

    def addPlayer(self, player):
        self.playerList.append(player)

    def printTeam(self):
        print(f"Team: {self.teamName}")
        print("-" * 40)
        for player in self.playerList:
            print(player)
        print("-" * 40)
        print(f"Total players: {len(self.playerList)}")


def main():
    # Create the four players
    player1 = Player("Joe Montana", "QB")
    player2 = Player("Barry Sanders", "RB")
    player3 = Player("Jerry Rice", "WR")
    player4 = Player("Graham Gano", "K")

    # Add players to a list
    playerList = [player1, player2, player3, player4]

    # Create the team with a team name and the list of players
    team = NFLTeam("Smashmouth Football", playerList)

    # Output the team name and all of its players
    team.printTeam()


if __name__ == "__main__":
    main()