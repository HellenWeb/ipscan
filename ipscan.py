"""

  name: ipscan
  date: 24.08.22
  creator: HellenWeb
  github: https://github.com/HellenWeb/ipscan

"""

import requests
import sys
from rich.console import Console
import argparse
from time import sleep
from dataclasses import dataclass

# Logic

@dataclass
class Type:
    mac: str
    ip: str

class IPScan:
    def __init__(self, ip):
        self.ip = ip
    def getinfo_ip(self):
        try:
            ip = requests.get(f"http://ip-api.com/json/{self.ip}").json()
            with console.status("Show info...") as status:
              sleep(1)
            console.print(f'Country: {ip["country"]}\n', style="bold blue")
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
              "All information ip ([bold green]ip-info.txt[/bold green])\n",
              style="bold yellow",
            )
        except requests.exceptions.ConnectionError as e:
          console.print("[*] No internet connection", style="bold red")
          sys.exit(1)

    def getinfo_mac(self, mac):
         try:
             r = requests.get(f"https://api.maclookup.app/v2/macs/{mac}").json()
             with console.status("Show info...") as status:
               sleep(1)
             console.print(f'Country: {r["country"]}\n', style="bold blue")
             console.print(f'Company: {r["company"]}\n', style="bold blue")
             console.print(f'Address: {r["address"]}\n', style="bold blue")
             with open("mac-info.txt", "w") as f:
                f.write(
                  f'Country: {r["country"]}\nCompany: {r["company"]}\nAddress: {r["address"]}'
                )
             console.print(
               "All information mac ([bold green]mac-info.txt[/bold green])",
               style="bold yellow",
             )
         except requests.exceptions.ConnectionError as e:
            console.print("[*] No internet Connection", style="bold red")
            sys.exit(1)


if __name__ == "__main__":

    console = Console()

    logo = """

    █  ██████╗░░██████╗░█████╗░░█████╗░███╗░░██╗
    ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║
    ██║██████╔╝╚█████╗░██║░░╚═╝███████║██╔██╗██║
    ██║██╔═══╝░░╚═══██╗██║░░██╗██╔══██║██║╚████║
    ██║██║░░░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║
    ╚═╝╚═╝░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝ v. 0.2.0

               Copyright by. Hellen
    """

    console.print(logo, style="red")

    # Parser

    parser = argparse.ArgumentParser()

    parser.add_argument("--ip", help="IP address", type=str, dest="ip")
    parser.add_argument("--mac", help="Mac address", type=str, dest="mac")

    args = parser.parse_args()

    # Class

    ips = IPScan(args.ip)

    if (args.ip): ips.getinfo_ip()

    if (args.mac): ips.getinfo_mac(args.mac)

    sys.exit(1)
