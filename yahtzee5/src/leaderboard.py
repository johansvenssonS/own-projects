"""
Modul till leaderboard
"""
from src.unorderedlist import UnorderedList
from src.sort import recursive_insertion
class Leaderboard():
    """Klass för leaderboard till yahtzee spel."""
    def __init__(self, user_data = None):
        self.entries = UnorderedList()
        if user_data is not None:
            for data in user_data:
                self.entries.append(data)
    @classmethod
    def load(cls, filename):
        """Metod för att ladda filen där användares poäng sparas."""
        loaded_leaderboard = cls()
        with open(filename, "r", encoding="utf8") as filehandler:
            for line in filehandler:##läsa linjer
                line = line.strip()
                user_entry = line.split(",")
                name = user_entry[0]
                points = int(user_entry[1])
                loaded_leaderboard.entries.append((name, points))
            return loaded_leaderboard
    def save(self, filename):
        """Metod för att spara användarens namn och poäng i fil."""
        with open(filename, "w", encoding="utf8") as filehandler:
            for index in range(self.entries.size()):
                user_data = self.entries.get(index)
                filehandler.write(f"{user_data[0]},{user_data[1]}\n")

    def add_entry(self, name, score):
        """Metod för att lägga till användares prestation."""
        self.entries.append((name, score))

    def remove_entry(self, index):
        """Metod för att ta bort användare och deras prestation."""
        remove_value = self.entries.get(index)
        self.entries.remove(remove_value)
    def sort(self):
        """Metod för att sortera leaderboard."""
        recursive_insertion(self.entries, self.entries.size())
