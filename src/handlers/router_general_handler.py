from rich.console import Console
from rich.table import Table
from src.services.router_general_service import router_general_service

console = Console()

def handle_get_firmware():

    console.print("\n[yellow]Fetching router info...[/yellow]\n")

    result = router_general_service.get_router_info()

    if not result["success"]:
        console.print(f"[red]Error : {result['error']}[/red]")
        return

    data = result["data"]

    device = data.get("hostname", "Unknown")
    kernel = data.get("kernel", "Unknown")
    model = data.get("model", "Unknown")
    firmware = data.get("release", {}).get("version", "Unknown")

    table = Table()

    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    table.add_row("Device", device)
    table.add_row("Firmware", firmware)
    table.add_row("Kernel", kernel)
    table.add_row("Model", model)

    console.print(table)


