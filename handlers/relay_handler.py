from rich.console import Console
from services.relay_service import RelayService

console = Console()

def handle_relay_reboot():

    console.print("\n[yellow]Rebooting relay...[/yellow]\n")

    relay_service = RelayService()
    result = relay_service.reboot_relay("relay0",3)

    if result["success"]:
        console.print("[green]Relay reboot command sent successfully[/green]")
    else:
        console.print(f"[red]Error: {result['error']}[/red]")
