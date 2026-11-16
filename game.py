from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from rich import print

from players import PlayerCharacter, LoadAllCharcters
from rooms import RoomObject

print("[green bold]Welcome to the game![/]")

player_list = LoadAllCharcters()

print(f"Character List: \n{player_list}")


entryway = RoomObject("Entryway", "You see big doors")
print(f"{entryway}")