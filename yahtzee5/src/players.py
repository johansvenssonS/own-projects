"""Modul för spelare i yahtzee(flerspelare)"""

class Player:
    """Klass för spelare i yahtzee(flerspelare)"""
    def __init__(self, player_id, hand, scoreboard):
        self.player_id = player_id
        self.hand = hand
        self.scoreboard = scoreboard
    def to_dict(self):
        """Metod för att konnvertera spelare till dict"""
        return {
            "Spelare": self.player_id,
            "Hand": self.hand,
            "Scoreboard": self.scoreboard
        }
    @classmethod
    def from_dict(cls, player_dict):
        """Metod för att konvertera dict till spelare"""
        return cls(
            player_dict["Spelare"],
            player_dict["Hand"],
            player_dict["Scoreboard"]
            
        )
