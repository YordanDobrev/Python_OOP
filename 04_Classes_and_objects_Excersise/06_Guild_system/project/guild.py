from typing import List

from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {self.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {player.guild}"

    def kick_player(self, player_name: str) -> str:
        if player_name not in self.players:
            return f"Player {player_name} is not in the guild."

        player = next(filter(lambda p: p.name == player_name, self.players))
        self.players.remove(player)
        player.guild = "Unaffiliated"
        return f"layer {player_name} has been removed from the guild."

    def guild_info(self) -> str:
        result = [f"Guild: {self.name}"]

        for playr in self.players:
            result.append(playr.player_info())

        return "\n".join(result) or "[]"
