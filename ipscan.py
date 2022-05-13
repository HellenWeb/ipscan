
# Modules

import requests
import sys
from rich.console import Console
import argparse
from time import sleep

# Default Variebles

console = Console()

parser = argparse.ArgumentParser()

parser.add_argument ("--ip", help= "IP address", type=str, dest='target', required=True )

args = parser.parse_args()

addr = args.target

# Logo

logo = """

██╗██████╗░░██████╗░█████╗░░█████╗░███╗░░██╗
██║██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║
██║██████╔╝╚█████╗░██║░░╚═╝███████║██╔██╗██║
██║██╔═══╝░░╚═══██╗██║░░██╗██╔══██║██║╚████║
██║██║░░░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║
╚═╝╚═╝░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝ v. 0.1.0
"""

console.print(logo, style="red")

# Logic

try:
    ip = requests.get(f"http://ip-api.com/json/{addr}").json()
    with console.status("Show info...") as status:
        sleep(1)
    console.print(f'\n\nCountry: {ip["country"]}\n', style="bold blue")
    console.print(f'Region: {ip["regionName"]}\n', style="bold blue")
    console.print(f'City: {ip["city"]}\n', style="bold blue")
    console.print(f'Time Zone: {ip["timezone"]}\n', style="bold blue")
    with open("ipInfo.txt", "w") as f:
        f.write(f'Country: {ip["country"]}\nRegion: {ip["regionName"]}\nCity: {ip["city"]}\nTime Zone: {ip["timezone"]}')
    console.print("All information ip ([bold green]ipInfo.txt[/bold green])", style="bold red")
except requests.exceptions.ConnectionError as e:
    console.print("[*] No internet connection", style="bold red")
