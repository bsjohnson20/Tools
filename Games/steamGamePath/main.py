# CLI app to find Steam game paths with Compatdata
from rich import print
from prompt_toolkit import prompt
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

import vdfparser as vd
import compat as comp
class SteamGamePathTool:
    def __init__(self):
        self.steam_path = vd.fetch_steam_path()
        self.steam_vdf_path = vd.fetch_steam_vdf()

        if self.steam_vdf_path is None:
            print("Steam VDF file not found")
            # Add user input to attempt to find
            self.steam_vdf_path = prompt("Enter the path to the Steam VDF file: ", default=self.steam_path)

        self.steam_vdf = vd.parse_vdf(self.steam_vdf_path)
        self.steam_library_locations = vd.find_extra_locations(self.steam_vdf)

        # for library in self.vdf_json["libraryfolders"]:
        #     print(f"Library {library}: {self.vdf_json['libraryfolders'][library]['apps']}")
        for library in self.steam_library_locations:
            print(f"[+] Found Steam library at: {library}")

        games = vd.fetchall_vdfs(self.steam_vdf)
        games = self.sort_games(games)
        # for game in games:
        #     print("Game:", game['name'], "ID:", game['appid'], "Vcf path:", f"[link=file://{game['true_path']}]vcf_path[/link]")

        console = Console()
        game_rend = [Panel(self.get_game_content(game), expand=True) for game in games]
        console.print(Columns(game_rend))

    def sort_games(self, games):
        return sorted(games, key=lambda x: x['name'])

    def get_game_content(self, game):
        return f"""[b]{game['name']}[/b]
        [white]Game ID: [yellow]{game['appid']}
        [white]Game Path: [green][link=file://{game['true_path']}]vcf_path[/link][/green]
        [white]Game Size: [red]{int(game['SizeOnDisk'])/(1024*1024)/1024:.2f} GB[/red]
        [white]Compat dir: [blue][link=file://{comp.fetch_compat_dir(game['appid'], game['root_steam_folder'])}]comp_folder[/link][/blue]"""
if __name__ == "__main__":
    steam_path_tool = SteamGamePathTool()
