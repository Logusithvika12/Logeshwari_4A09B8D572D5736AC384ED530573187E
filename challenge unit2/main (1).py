class Batsman:
    def __init__(self, name):
        self.name = name

    def play(self):
        return f"{self.name} is batting"

class Bowler:
    def __init__(self, name):
        self.name = name

    def play(self):
        return f"{self.name} is bowling"

# Creating objects of Batsman and Bowler classes
batsman = Batsman("John")
bowler = Bowler("Alice")

# Calling the play() method for each object
print(batsman.play())  # John is batting
print(bowler.play())   # Alice is bowling