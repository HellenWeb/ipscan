# Modules

import requests
import sys
from rich.console import Console
import argparse
from time import sleep

# Logic


class IPScan:
    def __init__(self, addr):
        self.ip = addr

    def start(self):
        try:
            ip = requests.get(f"http://ip-api.com/json/{self.ip}").json()
            with console.status("Show info...") as status:
                sleep(1)
            console.print(f'\n\nCountry: {ip["country"]}\n', style="bold blue")
            console.print(f'Region: {ip["regionName"]}\n', style="bold blue")
            console.print(f'City: {ip["city"]}\n', style="bold blue")
            console.print(f'Time Zone: {ip["timezone"]}\n', style="bold blue")
            console.print(f'ISP: {ip["isp"]}\n', style="bold blue")
            console.print(f'Organization: {ip["org"]}\n\n', style="bold blue")
            with open("ip-info.txt", "w") as f:
                f.write(
                        f'Country: {ip["country"]}\nRegion: {ip["regionName"]}\nCity: {ip["city"]}\nTime Zone: {ip["timezone"]}\nISP: {ip["isp"]}\nOrganization: {ip["org"]}'
                )
                console.print(
                    "All information ip ([bold green]ip-info.txt[/bold green])",
                    style="bold yellow",
                )
        except requests.exceptions.ConnectionError as e:
            console.print("[*] No internet connection", style="bold red")
            sys.exit(1)


if __name__ == "__main__":

    console = Console()

    logo = """

    █  ██████╗░░██████╗░█████╗░░█████╗░███╗░░██╗
    ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║
    ██║██████╔╝╚█████╗░██║░░╚═╝███████║██╔██╗██║
    ██║██╔═══╝░░╚═══██╗██║░░██╗██╔══██║██║╚████║
    ██║██║░░░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║
    ╚═╝╚═╝░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝ v. 0.1.0

               Copyright by. Hellen
    """

    console.print(logo, style="red")

    # Parser

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ip", help="IP address", type=str, dest="target", required=True
    )
    args = parser.parse_args()
    addr = args.target

    # Class

    ipscan = IPScan(addr)
    ipscan.start()
    sys.exit(1)
