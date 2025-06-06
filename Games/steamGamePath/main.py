# CLI app to find Steam game paths with Compatdata

import os
import re
from prompt_toolkit import prompt
import vdf
import json

class SteamGamePathTool:
    def __init__(self):
        self.steam_path = self.fetch_steam_path()
        self.steam_vdf = self.fetch_steam_vdf()

        if self.steam_vdf is None:
            print("Steam VDF file not found")
            # Add user input to attempt to find
            self.steam_vdf = prompt("Enter the path to the Steam VDF file: ", default=self.steam_path)

        self.steam_library_locations = self.find_extra_locations()
        self.parse_vdf()

        for library in self.vdf_json["libraryfolders"]:
            print(f"Library {library}: {self.vdf_json['libraryfolders'][library]['apps']}")
        # self.split_libraries(self.steam_library_locations)
        # self.fetch_all_game_ids()

    def run(self):
        steam_library_locations = self.find_extra_locations()
        print(steam_library_locations)

    def fetch_steam_path(self):
        apt_steam_path = os.path.expanduser(r"~/.steam/steam/steamapps/")
        flatpak_steam_path = os.path.expanduser(r"~/.var/app/com.valvesoftware.Steam/data/Steam/steamapps/")
        return apt_steam_path if os.path.exists(apt_steam_path) else flatpak_steam_path

    def fetch_steam_vdf(self) -> str|None:
        steam_vdf_path = os.path.join(self.steam_path, "libraryfolders.vdf")
        return steam_vdf_path if os.path.exists(steam_vdf_path) else None

    def validate_steam_path(self, path) -> bool:
        if not os.path.exists(path):
            print(f"Steam path does not exist (could be not mounted): {path}")
            return False
        return True

    # Scans vdf file for additional steam library paths... e.g. USB drive, external HDD
    def find_extra_locations(self):
        steam_library_locations = []
        # with open(self.steam_vdf, 'r') as steam_vdf_file:
        #     data = steam_vdf_file.read()

        # lines = data.split('\n')
        # for row in lines:
        #     if "path" in row:
        #         path = row.strip().split('\t')[2].replace('"', '')
        #         # Checks if the path is accessible otherwise excludes
        #         if self.validate_steam_path(path):
        #             steam_library_locations.append(path)

        return steam_library_locations

    # def split_libraries(self, library_path):
    #     """
    #     """
    #     with open(self.steam_vdf, 'r') as f:
    #         data = f.read()
    #     # split data based on 0, 1, 2, 3 etc
    #     # print(data)
    #     library_points = []
    #     for match in re.finditer(r'"\d"', data):
    #         matching, s_index, e_index = match.group(), match.start(), match.end()
    #         # Ignore mistaking total size if it's set to 0 for whatever reason
    #         if "totalsize" in data[s_index - 15:e_index]:
    #             continue
    #         library_points.append({"matching": matching, "start": s_index+5, "end": e_index-5})
    #     # print("matches found: ",library_points)
    #     # Split data based on starting points
    #     split_data = [data[start:end] for start, end in zip([0] + [point["start"] for point in library_points], [point["end"] for point in library_points] + [None])]

    #     # # Testing
    #     with open("./test.txt", "w") as f:
    #         for i, split in enumerate(split_data):
    #             f.write(f"############################\nSplit {i}:\n########################\n{split}\n")

    def parse_vdf(self):
        vdf_data = vdf.loads(open(self.steam_vdf, 'r').read())
        # json_string = json.dumps(vdf_data, indent=4)
        self.vdf_json = vdf_data

if __name__ == "__main__":
    steam_path_tool = SteamGamePathTool()
    steam_path_tool.run()
