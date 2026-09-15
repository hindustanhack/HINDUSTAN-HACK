#!/usr/bin/env python3
# Nub To Info — HINDUSTAN Ultimate Edition
# Owner: @Rolexseller1 | Channel: @Hindustanhack

import requests
import os
import time
import sys
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.box import DOUBLE, ROUNDED
from rich.align import Align
from rich.table import Table

try:
    import pyfiglet
except ImportError:
    pyfiglet = None

API_URL = "https://tfqdeadlo-1-78bapi.hf.space/search"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10)",
    "Accept": "application/json",
}

console = Console()

# ============================================================
# BANNER
# ============================================================
def display_banner():
    try:
        banner_text = pyfiglet.figlet_format("HINDUSTAN", font="big")
    except:
        banner_text = "=== HINDUSTAN ==="

    colored_banner = Text(banner_text, style="bold red")

    console.print(Panel(
        Align.center(colored_banner),
        box=DOUBLE,
        border_style="red",
        title="[bold white]🔥 ULTIMATE NUMBER TO INFO v2.0 🔥[/bold white]",
        subtitle="[bold yellow]⚡ Developer: @Rolexconfigyt | Channel: @Hindustanhack ⚡[/bold yellow]"
    ))

# ============================================================
# API CALL
# ============================================================
def lookup_number(number):
    try:
        params = {"mobile": number}
        r = requests.get(API_URL, headers=HEADERS, params=params, timeout=20)
        if r.status_code == 200:
            return r.json()
        return {"status": "error", "msg": f"HTTP {r.status_code}"}
    except Exception as e:
        return {"status": "error", "msg": str(e)}

# ============================================================
# PRINT INFO
# ============================================================
def print_info(num, data):
    console.print()
    console.print(Panel(
        f"[bold cyan]🔍 QUERY :[/bold cyan] [bold white]{num}[/bold white]",
        box=ROUNDED,
        border_style="cyan",
        title="[bold yellow] Searching... [/bold yellow]"
    ))

    if data.get("status") != "success":
        console.print(Panel(
            f"[bold red]❌ Error:[/bold red] {data.get('msg', 'Unknown error')}",
            border_style="red"
        ))
        return

    rec = data.get("data", {})
    if not rec:
        console.print(Panel(
            "[bold red]❌ No record found.[/bold red]",
            border_style="red"
        ))
        return

    console.print(f"[bold green]📊 Total Records :[/bold green] [bold white]1[/bold white]")

    table = Table(show_header=False, box=ROUNDED, border_style="green", title=f"[bold yellow]📄 Result #1[/bold yellow]")
    table.add_column("Field", style="bold cyan", width=22)
    table.add_column("Value", style="bold white")

    table.add_row("1 📱 Registered Mobile", str(rec.get("mobile", "N/A")))
    table.add_row("2 👤 Full Name",         str(rec.get("name", "N/A")))
    table.add_row("3 🔒 Aadhaar Number",    str(rec.get("id", "N/A")))
    table.add_row("4 ✉  Registered Email",  str(rec.get("email", "N/A") or "N/A"))
    table.add_row("5 👔 Father/Guardian",   str(rec.get("fname", "N/A")))
    table.add_row("6 ☎  Alternate Number",  str(rec.get("alt", "N/A")))
    table.add_row("7 📡 Telecom Circle",    str(rec.get("circle", "N/A")))
    table.add_row("8 📍 Address",           str(rec.get("address", "N/A")))
    table.add_row("9 🆔 Reference ID",      f"REF-{num[-4:]}-01")

    console.print(table)

    console.print(Panel(
        "[bold magenta]👨‍💻 Developer :[/bold magenta] [bold white]ROLEX[/bold white]\n"
        "[bold magenta]💎 Credits   :[/bold magenta] [bold white]HINDUSTAN HACK[/bold white]\n"
        f"[dim]🕒 {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}[/dim]",
        box=ROUNDED,
        border_style="magenta"
    ))

# ============================================================
# y/n LOOP
# ============================================================
def ask_continue():
    while True:
        ch = console.input("\n[bold cyan]🔁 Aur check kare? (y/n) :[/bold cyan] ").strip().lower()
        if ch in ("y", "yes"):
            return True
        elif ch in ("n", "no"):
            return False
        console.print("[bold red]❌ Sirf y ya n daalo![/bold red]")

# ============================================================
# MAIN
# ============================================================
def main():
    os.system("clear")
    display_banner()
    while True:
        raw = console.input("[bold green]🔗 Number daalo :[/bold green] ").strip()
        if not raw:
            console.print("[bold red]❌ Koi number nahi diya.[/bold red]")
        else:
            numbers = [n.strip() for n in raw.split(",") if n.strip()]
            console.print(f"\n[bold cyan]⚡ {len(numbers)} number check ho rahe...[/bold cyan]")
            time.sleep(0.3)
            for num in numbers:
                data = lookup_number(num)
                print_info(num, data)

        if not ask_continue():
            console.print("\n[bold green]👋 Bye — HINDUSTAN HACK 🔥[/bold green]\n")
            sys.exit(0)

if __name__ == "__main__":
    main()
