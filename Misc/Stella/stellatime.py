import os
import webbrowser
import subprocess
# open brave browser on linux


# open website
command = ["flatpak", "run", "com.brave.Browser", "https://www.google.com"]
result = subprocess.run(command, capture_output=True, text=True, check=True)